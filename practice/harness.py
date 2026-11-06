"""Runs and checks practice code. The app loads this into Python in the browser (Pyodide),
and tools/check-practice.py imports it, so both judge code the same way.

run(code)                          run the code as a script; prints go to the screen
check(code, func, tests_json)      call func on each test; returns JSON results
speed_prepare(code, func, setup)   build the big input; returns an error text or None
speed_run()                        time one call on the big input; returns seconds
"""
import contextlib
import copy
import io
import json
import sys
import time

FILENAME = "your_code.py"


def _no_input(prompt=""):
    raise RuntimeError("input() doesn't work in the practice box. Put the value in your code instead.")


def error_text(e):
    """One short line: where it happened and what went wrong."""
    if isinstance(e, SyntaxError):
        where = f"Line {e.lineno}: " if e.lineno else ""
        return f"{where}{type(e).__name__}: {e.msg}"
    line, tb = None, e.__traceback__
    while tb is not None:
        if tb.tb_frame.f_code.co_filename == FILENAME:
            line = tb.tb_lineno
        tb = tb.tb_next
    where = f"Line {line}: " if line else ""
    return f"{where}{type(e).__name__}: {e}"


def _load(code, quiet):
    ns = {"__name__": "__main__", "input": _no_input}
    sink = io.StringIO() if quiet else sys.stdout
    with contextlib.redirect_stdout(sink):
        exec(compile(code, FILENAME, "exec"), ns)
    return ns


def same(got, expect):
    """Strict comparison: True must be True (not 1), and None must be None."""
    if expect is None:
        return got is None
    if isinstance(expect, bool):
        return got is expect
    if isinstance(expect, (int, float)):
        return isinstance(got, (int, float)) and not isinstance(got, bool) and got == expect
    return type(got) is type(expect) and got == expect


def run(code):
    try:
        _load(code, quiet=False)
    except BaseException as e:  # show every error, including SystemExit
        print(error_text(e), file=sys.stderr)
    finally:
        sys.stdout.flush()  # so a last line without a newline still shows up
        sys.stderr.flush()


def check(code, func, tests_json):
    tests = json.loads(tests_json)
    try:
        ns = _load(code, quiet=True)
    except BaseException as e:
        return json.dumps({"error": error_text(e)})
    f = ns.get(func)
    if not callable(f):
        return json.dumps({"error": f"Write a function named {func}(...)."})
    results = []
    for t in tests:
        args = copy.deepcopy(t["args"])
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                got = f(*args)
            results.append({"ok": same(got, t["expect"]), "got": repr(got)})
        except Exception as e:
            results.append({"ok": False, "error": error_text(e)})
    return json.dumps({"results": results})


_speed = {}


def speed_prepare(code, func, setup):
    try:
        ns = _load(code, quiet=True)
        f = ns.get(func)
        if not callable(f):
            return f"Write a function named {func}(...)."
        env = {}
        exec(setup, env)
        _speed["f"], _speed["args"] = f, env["args"]
    except BaseException as e:
        return error_text(e)
    return None


def speed_run():
    f, args = _speed.pop("f"), _speed.pop("args")
    t0 = time.perf_counter()
    with contextlib.redirect_stdout(io.StringIO()):
        f(*args)
    return time.perf_counter() - t0
