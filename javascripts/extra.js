// Track selected filters across clicks
const activeFilters = new Set();

document.addEventListener("click", function(e) {
  const chip = e.target.closest(".chip");
  if (!chip) return;

  const selectedFilter = chip.getAttribute("data-filter");

  // Handle "All" button logic vs individual tags
  if (selectedFilter === "all") {
    activeFilters.clear();
    document.querySelectorAll(".chip").forEach(c => c.classList.remove("active"));
    chip.classList.add("active");
  } else {
    // Uncheck "All" button
    const allChip = document.querySelector('.chip[data-filter="all"]');
    if (allChip) allChip.classList.remove("active");

    // Toggle selected filter in active set
    if (activeFilters.has(selectedFilter)) {
      activeFilters.delete(selectedFilter);
      chip.classList.remove("active");
    } else {
      activeFilters.add(selectedFilter);
      chip.classList.add("active");
    }

    // Reset to "All" if no filters remain selected
    if (activeFilters.size === 0 && allChip) {
      allChip.classList.add("active");
    }
  }

  // 1. Show/Hide items (places must match ALL active filters)
  const items = document.querySelectorAll(".place-item");
  items.forEach(item => {
    const rawTags = item.getAttribute("data-tags") || "";
    const itemTags = rawTags.split(" ");
    
    // Check if the item has every currently active filter tag
    const matchesAll = Array.from(activeFilters).every(filter => itemTags.includes(filter));

    if (activeFilters.size === 0 || matchesAll) {
      item.style.display = "block";
    } else {
      item.style.display = "none";
    }
  });

  // 2. Hide neighborhood headings with 0 visible items
  const placeLists = document.querySelectorAll("ul.place-list");
  placeLists.forEach(list => {
    const visibleItems = list.querySelectorAll('.place-item[style*="display: block"], .place-item:not([style*="display: none"])');
    const header = list.previousElementSibling;

    if (visibleItems.length === 0 && activeFilters.size > 0) {
      list.style.display = "none";
      if (header && header.tagName === "H3") header.style.display = "none";
    } else {
      list.style.display = "block";
      if (header && header.tagName === "H3") header.style.display = "block";
    }
  });
});