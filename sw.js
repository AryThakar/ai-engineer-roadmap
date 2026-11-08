// Offline support for the AI Engineer Interview Roadmap.
const VERSION = "air-v4";
const PYODIDE_CACHE = "air-pyodide-314.0.7";   // big, never changes: kept across app updates
const SHELL = [
  "./",
  "index.html",
  "manifest.webmanifest",
  "flashcards.json",
  "practice/tasks.json",
  "lessons/index.json",
  "practice/harness.py",
  "practice/worker.js",
  "icons/icon-192.png",
  "icons/icon-512.png",
  "icons/icon-maskable-512.png",
  "icons/apple-touch-icon.png",
  "icons/favicon-64.png"
];

self.addEventListener("install", event => {
  event.waitUntil(caches.open(VERSION).then(cache => cache.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", event => {
  const keep = [VERSION, VERSION + "-fonts", PYODIDE_CACHE];
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => !keep.includes(k)).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// Try the network first so updates show up; fall back to the saved copy offline.
function networkFirst(req, key) {
  return fetch(req).then(res => {
    if (res.ok) { const copy = res.clone(); caches.open(VERSION).then(c => c.put(key, copy)); }
    return res;
  }).catch(() => caches.match(key));
}

self.addEventListener("fetch", event => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);

  if (req.mode === "navigate") {
    event.respondWith(networkFirst(req, "index.html"));
    return;
  }

  // Google Fonts: serve the saved copy, refresh it in the background.
  if (url.hostname === "fonts.googleapis.com" || url.hostname === "fonts.gstatic.com") {
    event.respondWith(
      caches.open(VERSION + "-fonts").then(cache =>
        cache.match(req).then(hit => {
          const net = fetch(req).then(res => { cache.put(req, res.clone()); return res; }).catch(() => hit);
          return hit || net;
        })
      )
    );
    return;
  }

  if (url.origin !== self.location.origin) return;
  const path = url.pathname;

  // Python in the browser: download once on first use, then always serve the saved copy.
  if (path.includes("/pyodide/")) {
    event.respondWith(
      caches.open(PYODIDE_CACHE).then(cache =>
        cache.match(req, { ignoreSearch: true }).then(hit => hit || fetch(req).then(res => {
          if (res.ok) cache.put(req, res.clone());
          return res;
        }))
      )
    );
    return;
  }

  // Cards, lessons, tasks and the practice runner change often.
  if (path.endsWith("/flashcards.json")) { event.respondWith(networkFirst(req, "flashcards.json")); return; }
  if (path.includes("/lessons/")) { event.respondWith(networkFirst(req, "lessons/" + path.split("/lessons/")[1])); return; }
  if (path.includes("/practice/")) { event.respondWith(networkFirst(req, "practice/" + path.split("/practice/")[1])); return; }

  // Other own files: saved copy first.
  event.respondWith(caches.match(req).then(hit => hit || fetch(req)));
});
