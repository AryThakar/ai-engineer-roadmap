"""Checks flashcards.json: the shape of every flashcard and MCQ, and that every code example
prints exactly the output written next to it. Run from the repo root with a current Python:

    python tools/check-flashcards.py

If a snippet ends in an exception, the expected output's last line is "ErrorName: message".
For MCQs it also checks that the marked answer matches what the code really does:
  kind "error"  -> the correct option is the name of the error the code raises
  kind "output" -> for one-line output with no error, the correct option is that output
"""
import contextlib, io, json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((root / "flashcards.json").read_text(encoding="utf-8"))
problems, ran = [], 0
ERR = re.compile(r"^([A-Za-z_]\w*(?:Error|Exception|Warning)): ")


def run(code, where):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(code, where, "exec"), {"__name__": "__main__"})
        except Exception as e:  # shown as the last output line, as a terminal shows it
            msg = e.msg if isinstance(e, SyntaxError) else e
            print(f"{type(e).__name__}: {msg}")
    return buf.getvalue().rstrip("\n")


def check_topic(topic, where):
    if not topic.isdigit() or not 1 <= int(topic) <= 71:
        problems.append(f"{where}: {topic} is not a roadmap topic id (1-71)")


def check_code(item, where):
    global ran
    if ("code" in item) != ("out" in item):
        problems.append(f"{where}: code and out must come together")
        return None
    if "code" not in item:
        return None
    got = run(item["code"], where)
    ran += 1
    if got != item["out"]:
        problems.append(f"{where} ({item['q']}):\n  expected: {item['out']!r}\n  got:      {got!r}")
    return got


for topic, cards in data.get("topics", {}).items():
    check_topic(topic, "flashcards")
    for n, c in enumerate(cards, 1):
        where = f"flashcards topic {topic} #{n}"
        extra = set(c) - {"q", "a", "hook", "code", "out", "trap"}
        if extra:
            problems.append(f"{where}: unknown fields {sorted(extra)}")
        if not c.get("q", "").strip() or not c.get("a", "").strip():
            problems.append(f"{where}: needs both q and a")
        check_code(c, where)

for topic, qs in data.get("mcq", {}).items():
    check_topic(topic, "mcq")
    for n, m in enumerate(qs, 1):
        where = f"mcq topic {topic} #{n}"
        extra = set(m) - {"kind", "q", "code", "out", "options", "answer", "why", "trap"}
        if extra:
            problems.append(f"{where}: unknown fields {sorted(extra)}")
        if m.get("kind") not in ("output", "error", "concept"):
            problems.append(f"{where}: kind must be output, error or concept")
        opts = m.get("options", [])
        if not 3 <= len(opts) <= 4 or len(set(opts)) != len(opts):
            problems.append(f"{where}: needs 3-4 different options")
            continue
        if not isinstance(m.get("answer"), int) or not 0 <= m["answer"] < len(opts):
            problems.append(f"{where}: answer must be the index of the correct option")
            continue
        if not m.get("q", "").strip() or not m.get("why", "").strip():
            problems.append(f"{where}: needs q and why")
        got = check_code(m, where)
        if got is None:
            continue
        right = opts[m["answer"]].replace("`", "").strip()
        last = got.splitlines()[-1] if got else ""
        err = ERR.match(last)
        if m["kind"] == "error":
            if not err or err.group(1) != right:
                problems.append(f"{where}: marked answer {right!r} but the code gives {last!r}")
        elif m["kind"] == "output" and got and "\n" not in got and not err and right != got:
            problems.append(f"{where}: marked answer {right!r} but the code prints {got!r}")

cards = sum(len(c) for c in data.get("topics", {}).values())
mcqs = sum(len(q) for q in data.get("mcq", {}).values())
print(f"Python {sys.version.split()[0]}: {cards} flashcards, {mcqs} MCQs, {ran} code examples run")
if problems:
    print("\n".join(problems))
    sys.exit(1)
print("All OK")
