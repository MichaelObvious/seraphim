// Register service worker
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("service-worker.js")
    .then(() => console.log("Service Worker registered"));
}

const tabs = document.querySelectorAll(".tab");
const subtabs = document.querySelectorAll(".subtab");
const subnav = document.getElementById("subnav");
const content = document.getElementById("content");

// --- Helpers ---
function setActive(elements, activeEl) {
  elements.forEach(el => el.classList.remove("active"));
  activeEl.classList.add("active");
}

// Load external HTML
async function loadContent(path) {
  try {
    const res = await fetch(path);
    const html = await res.text();
    content.innerHTML = html;
  } catch {
    content.innerHTML = "<p>Error loading content</p>";
  }
}

// --- Time logic ---
function getTimeOfDay() {
  const hour = new Date().getHours();
  if (hour < 11) return "mattino";
  if (hour < 17) return "mezzogiorno";
  return "sera";
}

function getWeekType() {
  const day = new Date().getDay(); // 0 = Sunday
  return (day === 0 || day === 6) ? "weekend" : "weekday";
}

// --- Tab Logic ---Element
tabs.forEach(tab => {
  tab.addEventListener("click", () => {
    setActive(tabs, tab);
    const selected = tab.dataset.tab;

    if (selected === "oggi") {
      subnav.style.display = "flex";

      const time = getTimeOfDay();
      document.querySelector(`[data-sub="${time}"]`).click();

    } else if (selected === "about") {
      subnav.style.display = "none";

      content.innerHTML = `
        <h2>About</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
        <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip.</p>
      `;

    } else if (selected === "settimana") {
      subnav.style.display = "none";

      const type = getWeekType();
      loadContent(`settimana/${type}.html`);
    }
  });
});

// --- Subtab Logic ---
subtabs.forEach(sub => {
  sub.addEventListener("click", () => {
    setActive(subtabs, sub);
    const selected = sub.dataset.sub;
    loadContent(`oggi/${selected}.html`);
  });
});

// --- Initial Load ---
window.addEventListener("load", () => {
  const currentTime = getTimeOfDay();
  document.querySelector(`[data-sub="${currentTime}"]`).click();
});

