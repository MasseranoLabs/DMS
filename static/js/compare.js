/* Progressive enhancement for the comparison table: click-to-sort + live filter.
   The table is fully usable without JS; this only layers on interactivity. */
(function () {
  "use strict";

  /* ---- Sortable tables ---- */
  document.querySelectorAll("table.sortable").forEach(function (table) {
    var headers = table.querySelectorAll("thead th");
    headers.forEach(function (th, colIndex) {
      th.setAttribute("tabindex", "0");
      th.setAttribute("role", "columnheader");

      function sort() {
        var tbody = table.tBodies[0];
        var rows = Array.prototype.slice.call(tbody.rows);
        var current = th.getAttribute("aria-sort");
        var asc = current !== "ascending"; // toggle

        headers.forEach(function (h) { h.setAttribute("aria-sort", "none"); });
        th.setAttribute("aria-sort", asc ? "ascending" : "descending");

        rows.sort(function (a, b) {
          var av = cellText(a.cells[colIndex]);
          var bv = cellText(b.cells[colIndex]);
          var an = parseFloat(av.replace(/[^0-9.\-]/g, ""));
          var bn = parseFloat(bv.replace(/[^0-9.\-]/g, ""));
          var bothNum = !isNaN(an) && !isNaN(bn) && av.match(/\d/) && bv.match(/\d/);
          var cmp = bothNum ? an - bn : av.localeCompare(bv, undefined, { sensitivity: "base" });
          return asc ? cmp : -cmp;
        });

        rows.forEach(function (r) { tbody.appendChild(r); });
      }

      th.addEventListener("click", sort);
      th.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); sort(); }
      });
    });
  });

  function cellText(cell) {
    return cell ? (cell.textContent || "").trim() : "";
  }

  /* ---- Live filter ---- */
  document.querySelectorAll(".filter-input").forEach(function (input) {
    var target = document.getElementById(input.getAttribute("data-target"));
    if (!target) return;
    input.addEventListener("input", function () {
      var q = input.value.trim().toLowerCase();
      var rows = target.tBodies[0].rows;
      var shown = 0;
      Array.prototype.forEach.call(rows, function (row) {
        var match = q === "" || (row.textContent || "").toLowerCase().indexOf(q) !== -1;
        row.hidden = !match;
        if (match) shown++;
      });
      announce(target, shown);
    });
  });

  function announce(table, n) {
    var live = table.parentNode.querySelector(".filter-count");
    if (!live) {
      live = document.createElement("p");
      live.className = "filter-count muted";
      live.setAttribute("aria-live", "polite");
      live.style.margin = ".6rem 0 0";
      live.style.fontSize = ".85rem";
      table.parentNode.appendChild(live);
    }
    live.textContent = n + (n === 1 ? " match" : " matches");
  }
})();
