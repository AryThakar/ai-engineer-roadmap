# Pyodide (Python in the browser)

The files in `314.0.7/` are copied unchanged from the npm package `pyodide@314.0.7`
(Python 3.14.2 compiled to WebAssembly). The app's code practice screen uses them to run
Python on the device, in `practice/worker.js`, so nothing is sent to a server.

- Project and source code: https://github.com/pyodide/pyodide
- License: Mozilla Public License 2.0 (MPL-2.0), https://www.mozilla.org/en-US/MPL/2.0/
- `python_stdlib.zip` holds the Python standard library, under the Python Software
  Foundation License: https://docs.python.org/3/license.html

Only the files the app needs are kept (about 13 MB): `pyodide.mjs`, `pyodide.asm.mjs`,
`pyodide.asm.wasm`, `python_stdlib.zip` and `pyodide-lock.json`.

To update: `npm pack pyodide@<version>`, copy those five files into a new folder named after the
version, change the version in `practice/worker.js` and `PYODIDE_CACHE` in `sw.js`, then run
`python tools/check-practice.py` and test the screen in a browser.
