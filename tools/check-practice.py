"""Checks practice/tasks.json against the reference answers in tools/practice_solutions.py.

    python tools/check-practice.py

For every task it confirms that:
  - the task has the fields the app needs, and its starter code runs and defines the function
  - the reference answer passes every test (so the tests themselves are right)
  - the starter code does NOT pass (so the tests actually test something)
  - the reference answer is fast on the big input (under a tenth of the limit)
  - a slow O(n²) answer takes more than twice the limit (so the speed check catches it,
    even on a device faster than this one)
Browser Python (Pyodide) runs these at a similar speed: on 6 Nov 2026 the references took
0.01-0.18 s there and the slow answers 13-45+ s, with a 4 s limit.
Speed runs happen in separate processes so a slow answer can be stopped.
"""
import json, pathlib, subprocess, sys, textwrap

root = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root / "practice"))
sys.path.insert(0, str(root / "tools"))
import harness  # noqa: E402
from practice_solutions import SOLUTIONS, SLOW  # noqa: E402

data = json.loads((root / "practice" / "tasks.json").read_text(encoding="utf-8"))
problems, seen = [], set()
NEEDED = {"id", "title", "func", "prompt", "starter", "tests", "target", "speed", "hint"}

SPEED_SCRIPT = textwrap.dedent("""
    import json, sys
    sys.path.insert(0, {practice!r})
    import harness
    task = json.loads(sys.stdin.read())
    err = harness.speed_prepare(task["code"], task["func"], task["setup"])
    if err:
        print("ERROR " + err)
    else:
        print(harness.speed_run())
""")


def timed(code, task, limit):
    payload = json.dumps({"code": code, "func": task["func"], "setup": task["speed"]["setup"]})
    try:
        r = subprocess.run([sys.executable, "-c", SPEED_SCRIPT.format(practice=str(root / "practice"))],
                           input=payload, capture_output=True, text=True, timeout=limit + 5)
    except subprocess.TimeoutExpired:
        return None
    out = r.stdout.strip()
    if out.startswith("ERROR") or r.returncode:
        return out or r.stderr.strip()
    return float(out)


for topic, tasks in data["topics"].items():
    if not topic.isdigit() or not 1 <= int(topic) <= 71:
        problems.append(f"topic {topic}: not a roadmap topic id")
    for t in tasks:
        tid = t.get("id", "?")
        if set(t) - NEEDED or NEEDED - set(t):
            problems.append(f"{tid}: fields should be {sorted(NEEDED)}")
            continue
        if tid in seen:
            problems.append(f"{tid}: duplicate id")
        seen.add(tid)
        def whole_floats(v):
            if isinstance(v, float):
                return v.is_integer()
            if isinstance(v, (list, tuple)):
                return any(whole_floats(x) for x in v)
            if isinstance(v, dict):
                return any(whole_floats(x) for x in v.values())
            return False
        if any(whole_floats(x["args"]) or whole_floats(x["expect"]) for x in t["tests"]):
            problems.append(f"{tid}: a test uses a whole-number float like 3.0; the app would show it as 3")
        if not any(x.get("show") for x in t["tests"]):
            problems.append(f"{tid}: mark at least one test with show=true (the examples)")
        if not {"time", "space", "why"} <= set(t["target"]):
            problems.append(f"{tid}: target needs time, space and why")
        start = json.loads(harness.check(t["starter"], t["func"], json.dumps(t["tests"])))
        if "error" in start:
            problems.append(f"{tid}: starter code fails: {start['error']}")
        elif all(r["ok"] for r in start["results"]):
            problems.append(f"{tid}: the starter code already passes every test")
        if tid not in SOLUTIONS:
            problems.append(f"{tid}: no reference answer in tools/practice_solutions.py")
            continue
        res = json.loads(harness.check(SOLUTIONS[tid], t["func"], json.dumps(t["tests"])))
        if "error" in res or not all(r["ok"] for r in res["results"]):
            problems.append(f"{tid}: reference answer fails the tests: {res}")
        limit = t["speed"]["limit"]
        fast = timed(SOLUTIONS[tid], t, limit)
        line = f"{tid:20} reference {fast if isinstance(fast, str) else (f'{fast:.3f}s' if fast is not None else 'TIMEOUT')}"
        if not isinstance(fast, float) or fast > limit / 10:
            problems.append(f"{tid}: reference answer should take under {limit / 10:.1f}s, got {fast}")
        if tid in SLOW:
            slow = timed(SLOW[tid], t, 2 * limit)
            line += f" | slow answer {'stopped after ' + str(2 * limit + 5) + 's' if slow is None else f'{slow:.1f}s'}"
            if isinstance(slow, float) and slow <= 2 * limit:
                problems.append(f"{tid}: the slow answer finished in {slow:.2f}s; it should take over twice the {limit}s limit")
            if isinstance(slow, str):
                problems.append(f"{tid}: the slow answer errored: {slow}")
            sres = json.loads(harness.check(SLOW[tid], t["func"], json.dumps(t["tests"])))
            if "error" in sres or not all(r["ok"] for r in sres["results"]):
                problems.append(f"{tid}: the slow answer should still be correct on the tests: {sres}")
        print(line)

print(f"Python {sys.version.split()[0]}: {len(seen)} tasks checked")
if problems:
    print("\n".join(problems))
    sys.exit(1)
print("All OK")
