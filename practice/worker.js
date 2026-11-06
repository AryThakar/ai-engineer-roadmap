// Runs Python (Pyodide) off the main page, so a stuck loop can be stopped by ending this worker.
// Messages in:  { id, kind: "run" | "check" | "speed", code, func, tests, setup }
// Messages out: { type: "ready", version } | { type: "out" | "err", text } | { id, type: "speed-start" }
//               | { id, type: "done", result } | { type: "fatal", text }
import { loadPyodide } from "../pyodide/314.0.7/pyodide.mjs";

let fns = null, sent = 0;
const MAX_OUT = 25000;   // the page shows at most 20,000 characters, so stop sending after this
const decoders = { out: new TextDecoder(), err: new TextDecoder() };
function send(type, bytes) {
  const text = decoders[type].decode(bytes, { stream: true });
  if (text && sent < MAX_OUT) { sent += text.length; postMessage({ type, text }); }
  return bytes.length;
}
const ready = (async () => {
  const py = await loadPyodide({ indexURL: new URL("../pyodide/314.0.7/", import.meta.url).href });
  const harness = await (await fetch(new URL("harness.py", import.meta.url))).text();
  py.runPython(harness);
  py.setStdout({ write: bytes => send("out", bytes), isatty: true });   // isatty: line by line, like a terminal
  py.setStderr({ write: bytes => send("err", bytes), isatty: true });
  const g = py.globals;
  fns = { run: g.get("run"), check: g.get("check"), prepare: g.get("speed_prepare"), time: g.get("speed_run") };
  postMessage({ type: "ready", version: py.runPython("import sys; sys.version.split()[0]") });
})().catch(e => postMessage({ type: "fatal", text: String((e && e.message) || e) }));

onmessage = async ({ data }) => {
  await ready;
  if (!fns) return;
  const { id, kind, code, func, tests, setup } = data;
  sent = 0;
  try {
    if (kind === "run") {
      fns.run(code);
      postMessage({ id, type: "done", result: {} });
    } else if (kind === "check") {
      postMessage({ id, type: "done", result: JSON.parse(fns.check(code, func, JSON.stringify(tests))) });
    } else if (kind === "speed") {
      const err = fns.prepare(code, func, setup);
      if (err) { postMessage({ id, type: "done", result: { error: err } }); return; }
      postMessage({ id, type: "speed-start" });
      postMessage({ id, type: "done", result: { seconds: fns.time() } });
    }
  } catch (e) {
    postMessage({ id, type: "done", result: { error: String((e && e.message) || e) } });
  }
};
