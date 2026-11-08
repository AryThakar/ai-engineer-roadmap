"""Checks the lesson notes in lessons/. Run from the repo root with a current Python (3.15):

    python tools/check-lessons.py

- lessons/index.json lists the lessons: {"version": 1, "topics": {"<topic id>": {"title": ..., "updated": "YYYY-MM-DD"}}}
- Each listed topic has lessons/<topic id>.md, starting with a "# " title line.
- Every ```python block that is followed (after blank lines) by an ```output block is run, and its
  output must match exactly (trailing spaces on a line are ignored). If the code ends in an exception,
  the last output line is "ErrorName: message", as in flashcards.json.
- ```python blocks without an output block are shown as they are (fragments) and are not run.
"""
import contextlib, io, json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
problems, ran = [], 0


def run(code, where):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(code, where, "exec"), {"__name__": "__main__"})
        except Exception as e:  # shown as the last output line, as a terminal shows it
            msg = e.msg if isinstance(e, SyntaxError) else e
            print(f"{type(e).__name__}: {msg}")
    return buf.getvalue()


def norm(text):
    return "\n".join(line.rstrip() for line in text.strip("\n").split("\n"))


def blocks(md):
    """Yield (lang, body, line number) for every fenced block."""
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r"^```(\w*)\s*$", lines[i])
        if not m:
            i += 1
            continue
        start, body = i + 1, []
        i += 1
        while i < len(lines) and not re.match(r"^```\s*$", lines[i]):
            body.append(lines[i])
            i += 1
        if i >= len(lines):
            problems.append(f"line {start}: a ``` block is never closed")
        yield m.group(1), "\n".join(body), start, i
        i += 1


index_path = root / "lessons" / "index.json"
index = json.loads(index_path.read_text(encoding="utf-8"))
if index.get("version") != 1 or not isinstance(index.get("topics"), dict):
    problems.append("lessons/index.json: needs version 1 and a topics object")
ids = {int(m) for m in re.findall(r'^\[(\d+),"[A-M]"', (root / "index.html").read_text(encoding="utf-8"), re.M)}
for tid, meta in sorted(index.get("topics", {}).items(), key=lambda kv: int(kv[0])):
    where = f"lessons/{tid}.md"
    if not tid.isdigit() or int(tid) not in ids:
        problems.append(f"{where}: {tid} is not a roadmap topic id")
        continue
    if not meta.get("title") or not re.match(r"^\d{4}-\d{2}-\d{2}$", meta.get("updated", "")):
        problems.append(f"lessons/index.json topic {tid}: needs a title and an updated date (YYYY-MM-DD)")
    path = root / "lessons" / f"{tid}.md"
    if not path.exists():
        problems.append(f"{where}: missing")
        continue
    md = path.read_text(encoding="utf-8")
    if not md.startswith("# "):
        problems.append(f"{where}: must start with a '# ' title line")
    found = list(blocks(md))
    lines = md.split("\n")
    for k, (lang, body, start, end) in enumerate(found):
        if lang not in ("python", "output", ""):
            problems.append(f"{where} line {start}: unknown block type {lang!r} (use python or output)")
        if lang != "python" or k + 1 >= len(found):
            continue
        nxt_lang, nxt_body, nxt_start, _ = found[k + 1]
        between = lines[end + 1:nxt_start - 1]
        if nxt_lang != "output" or any(l.strip() for l in between):
            continue
        got = norm(run(body, f"{where}:{start}"))
        ran += 1
        if got != norm(nxt_body):
            problems.append(f"{where} line {start}:\n  expected: {norm(nxt_body)!r}\n  got:      {got!r}")
for path in (root / "lessons").glob("*.md"):
    if path.stem not in index.get("topics", {}):
        problems.append(f"lessons/{path.name}: not listed in lessons/index.json")

print(f"Python {sys.version.split()[0]}: {len(index.get('topics', {}))} lessons, {ran} code examples run")
if problems:
    print("\n".join(problems))
    sys.exit(1)
print("All OK")
