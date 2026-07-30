#!/usr/bin/env python3
"""Regenerate product profiles from their trusted sources.

Reads ``sources/products.json``, fetches each product's trusted source pages,
and uses Claude to re-derive the structured facts + feature matrix, writing an
updated ``content/products/<slug>.md`` for each product. The feature keys come
from ``data/features.toml`` so the matrix stays consistent across products.

This never auto-commits; it writes files for a human to review (typically via
a pull request). Run with ``--check`` to see which products would change without
writing anything.

Usage:
    python scripts/regen.py                 # regenerate every product
    python scripts/regen.py webodm pix4d    # regenerate only these slugs
    python scripts/regen.py --check         # dry run, report diffs only

Requires ANTHROPIC_API_KEY (or an `ant auth login` profile) and the deps in
scripts/requirements.txt.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tomllib
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen

import anthropic

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources" / "products.json"
FEATURES = ROOT / "data" / "features.toml"
PRODUCTS_DIR = ROOT / "content" / "p"
MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-8")
MAX_SOURCE_CHARS = 40_000  # cap per source to keep prompts bounded


# --------------------------------------------------------------------------- #
# Fetching + HTML → text
# --------------------------------------------------------------------------- #
class _TextExtractor(HTMLParser):
    _SKIP = {"script", "style", "noscript", "svg", "head"}

    def __init__(self) -> None:
        super().__init__()
        self._chunks: list[str] = []
        self._skipping = 0

    def handle_starttag(self, tag, attrs):
        if tag in self._SKIP:
            self._skipping += 1

    def handle_endtag(self, tag):
        if tag in self._SKIP and self._skipping:
            self._skipping -= 1

    def handle_data(self, data):
        if not self._skipping and data.strip():
            self._chunks.append(data.strip())

    def text(self) -> str:
        return re.sub(r"\n{3,}", "\n\n", "\n".join(self._chunks))


def fetch_text(url: str) -> str:
    req = Request(url, headers={"User-Agent": "dronemappingsoftware-regen/1.0"})
    with urlopen(req, timeout=30) as resp:  # noqa: S310 (trusted, curated URLs)
        raw = resp.read().decode("utf-8", errors="replace")
    parser = _TextExtractor()
    parser.feed(raw)
    return parser.text()[:MAX_SOURCE_CHARS]


# --------------------------------------------------------------------------- #
# Schema (mirrors the [extra] front matter the templates expect)
# --------------------------------------------------------------------------- #
USE_CASES = [
    "Surveying & mapping", "Agriculture", "Construction", "Mining & aggregates",
    "Inspection & infrastructure", "Public safety & emergency response",
    "Cultural heritage & archaeology", "Environmental & forestry",
    "Film, VFX & games", "Research & education",
]

# Controlled vocabulary for primary_outputs, normalized across all products.
OUTPUTS = [
    "Orthomosaic", "DSM", "DTM", "Point cloud", "3D mesh", "3D tiles",
    "Gaussian splats", "Contours", "Index maps", "Floor plans",
]


def build_schema(feature_keys: list[str]) -> dict:
    feature_enum = ["yes", "no", "unknown"]  # never infer "no" from silence; default "unknown"
    str_arr = {"type": "array", "items": {"type": "string"}}
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "summary": {"type": "string"},
            "developer": {"type": "string"},
            "country": {"type": "string"},
            "license": {"type": "string"},
            "open_source": {"type": "boolean"},
            "price_model": {"type": "string"},
            "price_detail": {"type": "string"},
            "platforms": str_arr,
            "deployment": str_arr,
            "primary_outputs": {"type": "array", "items": {"type": "string", "enum": OUTPUTS}},
            "target_use_cases": {"type": "array", "items": {"type": "string", "enum": USE_CASES}},
            "latest_version": {"type": "string"},
            "first_release_year": {"type": "string"},
            "official_url": {"type": "string"},
            "key_features": str_arr,
            "pros": str_arr,
            "cons": str_arr,
            "typical_workflow": str_arr,
            "overview": str_arr,  # paragraphs
            "features": {
                "type": "object",
                "additionalProperties": False,
                "properties": {k: {"type": "string", "enum": feature_enum} for k in feature_keys},
                "required": feature_keys,
            },
            "feature_notes": {
                "type": "object",
                "additionalProperties": {"type": "string"},
            },
        },
        "required": [
            "summary", "developer", "country", "license", "open_source",
            "price_model", "platforms", "deployment", "primary_outputs",
            "target_use_cases", "official_url", "key_features", "pros", "cons",
            "typical_workflow", "overview", "features",
        ],
    }


def build_verdict_schema(feature_keys: list[str]) -> dict:
    verdict = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "verdict": {"type": "string", "enum": ["CONFIRMED", "REJECTED"]},
            "quote": {"type": "string"},
            "recommended": {"type": "string", "enum": ["yes", "no", "unknown"]},
        },
        "required": ["verdict", "recommended"],
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "verdicts": {
                "type": "object",
                "additionalProperties": False,
                "properties": {k: verdict for k in feature_keys},
                "required": feature_keys,
            }
        },
        "required": ["verdicts"],
    }


SYSTEM = """You are a meticulous research assistant maintaining an index of drone \
mapping / photogrammetry software. You are given the fetched text of a product's \
OFFICIAL trusted sources. Search that text EXHAUSTIVELY; a missed capability harms \
the site's credibility.

Rules:
- Use ONLY facts stated in the provided source text. Never invent facts and never \
infer from silence.
- Adopt a NEUTRAL, IMPARTIAL tone. Vendor sources are promotional, so discount their \
self-promotion: never repeat marketing superlatives or self-claims as fact (for \
example "best", "leading", "#1", "world's most accurate", "fastest", \
"industry-leading", "revolutionary", "cutting-edge"). Report only concrete, verifiable \
capabilities in plain wording; a superlative boast with no substance is not a feature. \
Do not compare the product favourably or unfavourably against others.
- Each feature value is exactly one of "yes", "no", or "unknown":
  - "yes": a source explicitly confirms the capability (including via a plugin, \
add-on, hosted service, or a specific paid edition; note the caveat).
  - "no": a source explicitly states the capability is NOT supported.
  - "unknown": the sources say nothing either way. This is the default. NEVER mark \
"no" just because a feature is undocumented.
  - "image_input" means the product accepts photographs or images as input (from any \
angle). Confirm it whenever the sources describe image-based / photogrammetric \
reconstruction from photos.
  - "tiles_3d" means OGC 3D Tiles output specifically (Cesium 3D Tiles, tileset.json, \
b3dm / pnts). A Potree octree, Esri i3s, OSGB, or a generic "tiled / streamable model" \
is NOT OGC 3D Tiles; mark it "unknown" unless OGC or Cesium 3D Tiles is explicitly named.
  - "self_hosted" means the software offers a server you can run on your own hardware \
(an on-premise / self-hosted server). A desktop app that merely runs locally, an \
SDK / library, or distributing compute across LAN machines does NOT qualify; mark those \
"unknown".
- Scan the sources thoroughly. Features are often documented only on feature, product, \
documentation, support, or pricing sub-pages, not the landing page; read the sub-pages \
before deciding, and do not conclude "unknown" from the home page alone.
- Add a concise feature_notes entry for every "yes" that carries a caveat (for \
example "Professional edition", "via plugin", or "hosted cloud service"), citing \
where you saw it.
- pros and cons must each be grounded in the sources. NEVER write a con that asserts \
a feature is missing or unsupported unless a source explicitly says so; do not report \
limitations you cannot confirm.
- Describe the product under its OWN name and branding; do not attribute it to an \
upstream or related project unless the sources explicitly do.
- Do not use em dashes anywhere in the output; use commas, colons, or parentheses.
- State every fact DIRECTLY. It is implied that all facts come from the sources, so do \
NOT attribute them in the text: never write "the README describes", "the docs state", \
"the documentation notes", "the page says", "the vendor states", "per the reviewed \
sources", "the reviewed pages say", "is documented as", "is described as", or similar. \
Write the capability itself, not that a source mentions it.
- license: for an open-source product, give ONE standard SPDX identifier only (for \
example MIT, BSD-3-Clause, GPL-3.0, AGPL-3.0, LGPL-3.0, MPL-2.0, Apache-2.0, CECILL-B) \
and set open_source true; do not add verbose descriptions or secondary/component \
licenses. For a proprietary product set open_source false and use "Freemium" as the \
price_model when there is a free tier plus paid plans (the license label is normalized \
automatically).
- For text fields not found in the sources, use "Unknown". Choose target_use_cases \
and primary_outputs ONLY from the provided controlled vocabularies, using the exact \
strings; map vendor wording onto the closest canonical term (for example a "tiled \
model" is "3D tiles", a "textured mesh" is "3D mesh"). Keep prose factual and \
neutral."""


# Pass 2. Every feature claim from the researcher is re-checked by this hostile
# skeptic against the same source text. Its default verdict is REJECTED; a claim
# survives only with an explicit verbatim quote. This is what makes the pipeline
# hard to fool: a gallery caption or marketing boast cannot carry a "yes".
SKEPTIC_SYSTEM = """You are a hostile skeptic fact-checker. You are given a product's \
trusted source text and a set of feature claims about it. For EACH claim your DEFAULT \
verdict is REJECTED. Ask "but is it really?" of every claim.

- Mark a claim CONFIRMED only if the source text contains an EXPLICIT statement that the \
product has or does that capability, and put that exact verbatim sentence or phrase in \
the quote field.
- The following NEVER confirm a claim (mark REJECTED): a gallery or example-project \
caption, a community showcase, a screenshot, a marketing superlative or vague boast, an \
inference or "it probably can", anything not present in the given text, and your own \
prior knowledge.
- recommended value: "yes" only when CONFIRMED with an explicit capability quote; "no" \
ONLY when the source text explicitly states the capability is NOT supported (put that \
denial in the quote field); otherwise "unknown". Never output "no" from mere absence.
- Do not use em dashes anywhere in your output."""


# --------------------------------------------------------------------------- #
# TOML front-matter emitter (small, dependency-free, only what we emit)
# --------------------------------------------------------------------------- #
def norm_license(license: str, open_source, price_model: str = "") -> str:
    """Normalize license names. Open-source keeps its SPDX name; any proprietary
    variant collapses to "Proprietary", except freemium -> "Proprietary (freemium)"."""
    if open_source:
        return license or "Open source"
    blob = f"{license} {price_model}".lower()
    return "Proprietary (freemium)" if "freemium" in blob else "Proprietary"


def _q(s: str) -> str:
    return '"' + s.replace("\\", "\\").replace('"', '\\"').replace("\n", " ") + '"'


def _arr(items) -> str:
    if not items:
        return "[]"
    return "[\n" + "".join(f"  {_q(str(i))},\n" for i in items) + "]"


def render_markdown(title: str, data: dict, features_meta: dict, sources: list[str],
                    weight: int, warning: str | None = None) -> str:
    e = dict(data)
    e["license"] = norm_license(e.get("license", ""), e.get("open_source"), e.get("price_model", ""))
    lines = [
        "+++", f"title = {_q(title)}", f"description = {_q(e.get('summary', title))}",
        f"weight = {weight}", "", "[extra]",
    ]
    scalar_keys = [
        "summary", "developer", "country", "license", "price_model",
        "price_detail", "latest_version", "first_release_year", "official_url",
    ]
    for k in scalar_keys:
        if e.get(k):
            lines.append(f"{k} = {_q(e[k])}")
    lines.append(f"open_source = {'true' if e.get('open_source') else 'false'}")
    # `warning` is editorial metadata from products.json, not model output.
    if warning:
        lines.append(f"warning = {_q(warning)}")
    for k in ["platforms", "deployment", "primary_outputs", "target_use_cases",
              "key_features", "pros", "cons", "typical_workflow"]:
        lines.append(f"{k} = {_arr(e.get(k, []))}")
    lines.append(f"sources = {_arr(sources)}")

    lines.append("\n[extra.features]")
    for group in features_meta["groups"]:
        for f in group["features"]:
            key = f["key"]
            lines.append(f"{key} = {_q(e['features'].get(key, 'unknown'))}")

    notes = e.get("feature_notes") or {}
    if notes:
        lines.append("\n[extra.feature_notes]")
        for key, note in notes.items():
            lines.append(f"{key} = {_q(note)}")

    lines.append("+++\n")
    lines.append("\n\n".join(e.get("overview", [])) + "\n")
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
def regenerate(product: dict, features_meta: dict, feature_keys: list[str],
               client: anthropic.Anthropic, schema: dict, weight: int) -> str:
    name = product["name"]
    corpus = []
    for url in product["sources"]:
        try:
            corpus.append(f"=== SOURCE: {url} ===\n{fetch_text(url)}")
        except Exception as exc:  # noqa: BLE001
            print(f"  ! failed to fetch {url}: {exc}", file=sys.stderr)
    prompt = (
        f"Product: {name}\n\n"
        f"Canonical feature keys (return a value for each): {', '.join(feature_keys)}\n\n"
        f"Trusted source text follows.\n\n" + "\n\n".join(corpus)
    )
    resp = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        system=SYSTEM,
        output_config={"format": {"type": "json_schema", "schema": schema}},
        messages=[{"role": "user", "content": prompt}],
    )
    text = next(b.text for b in resp.content if b.type == "text")
    data = json.loads(text)

    # Pass 2: hostile skeptic re-checks every claim against the same source text.
    data["features"] = skeptic_verify(name, data.get("features", {}), corpus,
                                      feature_keys, client)
    return render_markdown(name, data, features_meta, product["sources"], weight,
                           warning=product.get("warning"))


def skeptic_verify(name: str, claims: dict, corpus: list[str], feature_keys: list[str],
                   client: anthropic.Anthropic) -> dict:
    """Adversarially re-check each feature claim against the fetched source text.

    Returns a corrected feature map: any claim the skeptic cannot back with an
    explicit verbatim quote is downgraded (to "unknown", or "no" only when the
    source explicitly denies it). Prints every change it makes.
    """
    schema = build_verdict_schema(feature_keys)
    claim_lines = "\n".join(f"- {k}: {claims.get(k, 'unknown')}" for k in feature_keys)
    prompt = (
        f"Product: {name}\n\nFeature claims to audit (feature: claimed value):\n"
        f"{claim_lines}\n\n"
        "Only the source text below may be used as evidence. Confirm a claim ONLY "
        "with an explicit verbatim quote from it.\n\n" + "\n\n".join(corpus)
    )
    resp = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        system=SKEPTIC_SYSTEM,
        output_config={"format": {"type": "json_schema", "schema": schema}},
        messages=[{"role": "user", "content": prompt}],
    )
    verdicts = json.loads(next(b.text for b in resp.content if b.type == "text"))["verdicts"]
    corrected = {}
    for k in feature_keys:
        was = claims.get(k, "unknown")
        rec = verdicts.get(k, {}).get("recommended", was)
        corrected[k] = rec
        if rec != was:
            print(f"    skeptic downgrade: {k} {was} -> {rec}", file=sys.stderr)
    return corrected


def slug_for(product: dict) -> str:
    return product.get("slug") or re.sub(r"[^a-z0-9]+", "-", product["name"].lower()).strip("-")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("slugs", nargs="*", help="only regenerate these product slugs/names")
    ap.add_argument("--check", action="store_true", help="dry run; report changes, write nothing")
    args = ap.parse_args()

    products = json.loads(SOURCES.read_text())
    features_meta = tomllib.loads(FEATURES.read_text())
    feature_keys = [f["key"] for g in features_meta["groups"] for f in g["features"]]
    schema = build_schema(feature_keys)
    client = anthropic.Anthropic()

    wanted = {s.lower() for s in args.slugs}
    changed = 0
    # weight follows the order of products.json, so the table/matrix display order
    # matches the source file regardless of which subset is regenerated.
    for idx, product in enumerate(products):
        slug = slug_for(product)
        if wanted and slug not in wanted and product["name"].lower() not in wanted:
            continue
        print(f"• {product['name']} ({slug}) …")
        out = PRODUCTS_DIR / f"{slug}.md"
        new = regenerate(product, features_meta, feature_keys, client, schema, idx + 1)
        old = out.read_text() if out.exists() else ""
        if new.strip() == old.strip():
            print("  = no change")
            continue
        changed += 1
        if args.check:
            print("  ~ would update (run without --check to write)")
        else:
            out.write_text(new)
            print(f"  ✓ wrote {out.relative_to(ROOT)}")

    print(f"\n{changed} product(s) {'would change' if args.check else 'updated'}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
