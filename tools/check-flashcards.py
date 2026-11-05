"""Checks flashcards.json: the shape of every card, and that every code example prints
exactly the output written on its card. Run from the repo root with a current Python:

    python tools/check-flashcards.py

If a snippet ends in an exception, the expected output's last line is "ErrorName: message".
"""
import contextlib, io, json, pathlib, sys

root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((root / "flashcards.json").read_text(encoding="utf-8"))
allowed = {"q", "a", "hook", "code", "out", "trap"}
problems, checked = [], 0

for topic, cards in data["topics"].items():
    if not topic.isdigit() or not 1 <= int(topic) <= 71:
        problems.append(f"topic {topic}: not a roadmap topic id (1-71)")
    for n, card in enumerate(cards, 1):
        where = f"topic {topic} card {n}"
        if set(card) - allowed:
            problems.append(f"{where}: unknown fields {sorted(set(card) - allowed)}")
        if not card.get("q", "").strip() or not card.get("a", "").strip():
            problems.append(f"{where}: needs both q and a")
        if ("code" in card) != ("out" in card):
            problems.append(f"{where}: code and out must come together")
        if "code" not in card:
            continue
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            try:
                exec(compile(card["code"], where, "exec"), {"__name__": "__main__"})
            except Exception as e:  # the card shows the error as its last output line
                print(f"{type(e).__name__}: {e}")
        got = buf.getvalue().rstrip("\n")
        checked += 1
        if got != card["out"]:
            problems.append(f"{where} ({card['q']}):\n  expected: {card['out']!r}\n  got:      {got!r}")

total = sum(len(c) for c in data["topics"].values())
print(f"Python {sys.version.split()[0]}: {total} cards, {checked} code examples run")
if problems:
    print("\n".join(problems))
    sys.exit(1)
print("All cards OK")
