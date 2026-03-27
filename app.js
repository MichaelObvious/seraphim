// Register service worker
if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("service-worker.js")
        .then(() => console.log("Service Worker registered"));
}

const tabs = document.querySelectorAll(".tab");
const subtabs = document.querySelectorAll(".subtab");
const subnav = document.getElementById("subnav");
const content = document.getElementById("content");
const daytitle = document.getElementById("daytitle");
let daytitleHTML = "";
// const title = document.getElementById("maintitle");

// --- Helpers ---
function setActive(elements, activeEl) {
    elements.forEach(el => el.classList.remove("active"));
    activeEl.classList.add("active");
}

var cachedFetches = new Map();

async function cachedFetch(path) {
    if (!cachedFetches.has(path) || !cachedFetches.get(path).ok) {
        const res = await fetch(path);
        cachedFetches.set(path, {ok: res.ok, html: await res.text()});
    }
    return cachedFetches.get(path);
}

// Load external HTML
async function loadContent(path) {
    try {
        const {_, html} = await cachedFetch(path);
        content.innerHTML = html;
    } catch {
        content.innerHTML = "<p>Error loading content</p>";
    }
}

async function loadTitle(path) {
    try {
        const today = new Date();
        const path = `pages/titles/${today.getFullYear()}/${today.getMonth().toString().padStart(2, "0")}_${today.getDate().toString().padStart(2, "0")}-title.html`
        const {res, html} = await cachedFetch(path);
        daytitleHTML = html;
        daytitle.innerHTML = html;
    } catch {
        daytitle.innerHTML = "<p>Error loading title</p>";
    }
}

// --- Time logic ---
function getTimeOfDay() {
    const hour = new Date().getHours();
    if (hour < 11) return "morning";
    if (hour < 17) return "midday";
    return "evening";
}

var found_holy_hour_day = new Date();
async function loadHolyHour() {
    content.innerHTML = "";
    let today;
    today = found_holy_hour_day;
    if (new Date() > found_holy_hour_day) {
        today = new Date();
    }
    let i = 0;
    while (i < 10) {
        const path = `pages/holy_hours/${today.getFullYear()}_${today.getMonth().toString().padStart(2, "0")}_${today.getDate().toString().padStart(2, "0")}-holy_hour.html`;
        try {
            const {ok, html} = await cachedFetch(path);
            if (ok) {
                if content.innerHTML.length = 0 {
                    content.innerHTML = html;
                }
                found_holy_hour_day = today;
                return;
            }
        } catch {}
        today.setDate(today.getDate() + 1);
        i += 1;
    }
    content.innerHTML = "<p>Error loading holy hour</p>";
}

// --- Tab Logic ---Element
tabs.forEach(tab => {
    tab.addEventListener("click", () => {
        setActive(tabs, tab);
        const selected = tab.dataset.tab;

        if (selected === "oggi") {
            subnav.style.display = "flex"
            daytitle.innerHTML = daytitleHTML;

            const time = getTimeOfDay();
            document.querySelector(`[data-sub="${time}"]`).click();

        } else if (selected === "about") {
            subnav.style.display = "none";
            daytitle.innerHTML = `<h1><i>Seraphim</i></h1>`;

            content.innerHTML = `
        <h2>About</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
        <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip.</p>
      `;

        } else if (selected === "settimana") {
            subnav.style.display = "none";
            daytitle.innerHTML = daytitleHTML;

            loadHolyHour();
        }
    });
});

// --- Subtab Logic ---
subtabs.forEach(sub => {
    sub.addEventListener("click", () => {
        setActive(subtabs, sub);
        const selected = sub.dataset.sub;
        const today = new Date();
        loadContent(`pages/daytime/${today.getFullYear()}/${today.getMonth().toString().padStart(2, "0")}_${today.getDate().toString().padStart(2, "0")}-${selected}.html`);
    });
});

// --- Initial Load ---
window.addEventListener("load", () => {
    const currentTime = getTimeOfDay();
    loadTitle();
    document.querySelector(`[data-sub="${currentTime}"]`).click();
});

