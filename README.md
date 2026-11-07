# AI Engineer Interview Roadmap

71 topics an AI/ML engineer fresher interview can test, grouped into 13 sections and 6 study stages, each tagged by how deep it gets tested (live coding, concept, or MCQ), with 84 checked learning and practice resources.

**Open it:** https://arythakar.github.io/ai-engineer-roadmap/

## Install on your phone

- **Android (Chrome):** open the link, then tap **Install app** on the page, or menu ⋮ → **Add to Home screen** / **Install app**.
- **iPhone (Safari):** open the link, tap **Share**, then **Add to Home Screen**.

The installed app opens full screen and works offline after the first visit. Progress is saved on the device; use **Back up or move progress** to copy it between devices.

## Flashcards and MCQs

Tap **Flashcards & MCQs** to revise everything taught so far, or **Cards** / **MCQ** inside a topic.

- **Flashcards**: the questions interviewers ask out loud. Tap to flip, then **Got it** or **Again**.
- **MCQ**: predict the output, find the error, concept checks. Options are shuffled each time; you get a score and can retry the ones you missed.

## LeetCode problems

Topics 16, 17 and 18 have a **LeetCode problems** box: free problems in pattern order, Easy first, with direct links. Solve them on LeetCode and tick each one you solved on your own. The ticks are saved in your progress backup.

## Code practice

For Python skills LeetCode doesn't test (decorators, generators, files, classes), tasks will appear here as those topics are reached. Tap **Code practice**, or **Code** inside a topic, to write Python and check it right in the app. Python runs on your device; the first time it downloads about 13 MB, and after that it works offline.

- Each task shows examples and the target, like **Time O(n) · Space O(1)**.
- **Run** shows what your code prints. **Check** runs the tests, then times your function on a big input. If it's too slow (probably O(n²)), it tells you so.
- Your code is saved on the device. **Stop** ends a loop that never finishes.

## Files

- `index.html`: the whole app (HTML, CSS and JavaScript in one file)
- `flashcards.json`: the flashcards and MCQs, by topic id
- `practice/`: the coding tasks (`tasks.json`), the code that judges answers (`harness.py`) and the worker that runs Python (`worker.js`)
- `pyodide/`: Python for the browser ([Pyodide](https://github.com/pyodide/pyodide), MPL-2.0), see `pyodide/README.md`
- `manifest.webmanifest`, `sw.js`, `icons/`: what makes it installable and available offline
- `CLAUDE.md`: handoff notes so a new Claude chat can continue the prep
- `tools/`: `check-flashcards.py` (runs every code example and checks its output and marked answer), `check-practice.py` (checks every task against a correct and a slow answer), `practice_solutions.py` (those answers; spoilers) and `update-claude-md.js`
