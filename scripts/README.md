# Data regeneration

Product profiles in `content/products/*.md` are **generated from each product's
trusted sources** listed in `sources/products.json`. The comparison table and the
feature matrix on the home page are built from those files plus the canonical
feature list in `data/features.toml`.

`regen.py` re-fetches every product's sources and asks Claude to re-derive the
structured facts + feature matrix, writing updated content files **for review**.
It never commits; a human reviews the diff (locally or in a PR).

### Two-pass validation (researcher, then skeptic)

Every feature value goes through two independent LLM passes against the same
fetched source text:

1. **Researcher** derives an initial `yes` / `no` / `unknown` for each feature.
2. **Skeptic** is a hostile fact-checker whose default verdict is *REJECTED*. For
   each claim it must find an **explicit verbatim quote** in the source text, or the
   claim is downgraded. A gallery caption, marketing boast, screenshot, or inference
   does not count. Anything it cannot prove becomes `unknown` (or `no` only when the
   source explicitly denies the capability). Downgrades are printed to stderr.

This is why undocumented capabilities are never marked supported, and why a claim
like "change detection" backed only by a gallery example gets rejected. The same
rule holds by hand: mark `yes` only with an explicit source statement; never infer
`no` from silence.

## Run it locally

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r scripts/requirements.txt

export ANTHROPIC_API_KEY=sk-ant-...   # or: ant auth login

python scripts/regen.py --check       # dry run, show what would change
python scripts/regen.py               # write updates for all products
python scripts/regen.py webodm        # just one product (by slug or name)
```

Then review with `git diff`, run `zola build` to confirm it still builds, and
commit only if the changes look right. Facts not found in the sources are marked
`Unknown` (text) or `unknown` (features) rather than guessed. A feature is only
marked `no` when a source explicitly states it is not supported; otherwise it is
`unknown`, never assumed absent. Spot-check any changed feature value against the
source before trusting it.

## Adding a software

1. Add an entry to `sources/products.json` (`name` + trusted `sources` URLs).
2. Run `python scripts/regen.py "<name>"` to generate its profile page.
3. Review and commit `content/products/<slug>.md`.

## Adding a comparison feature

Add one entry under a group in `data/features.toml` (a `key` + `label`). The
column appears automatically; re-run `regen.py` so each product gets a value for
the new key.

## On-demand refresh in CI

`.github/workflows/refresh.yml` runs this on `workflow_dispatch` and opens a pull
request with any changes. It needs an `ANTHROPIC_API_KEY` repository secret.
There is **no** scheduled trigger; refreshes are always human-initiated.
