const root = document.documentElement;
const toggle = document.getElementById("theme-toggle");
const key = "mdview-theme";

function applyTheme(theme) {
  root.setAttribute("data-theme", theme);
}

function bootstrapTheme() {
  const stored = localStorage.getItem(key);
  if (stored === "light" || stored === "dark") {
    applyTheme(stored);
    return;
  }

  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  applyTheme(prefersDark ? "dark" : "light");
}

bootstrapTheme();

toggle.addEventListener("click", () => {
  const current = root.getAttribute("data-theme") || "light";
  const next = current === "light" ? "dark" : "light";
  applyTheme(next);
  localStorage.setItem(key, next);
});
