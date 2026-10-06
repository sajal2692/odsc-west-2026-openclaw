"""Workshop setup check.

Confirms that Python is recent enough and that the task-summary skill script
runs on the sample data and produces the expected output.

Usage (from the repository root):
    python3 setup_check.py
"""

import json
import subprocess
import sys
from pathlib import Path

MIN_PYTHON = (3, 9)
here = Path(__file__).resolve().parent
script = here / "skills" / "task-summary" / "scripts" / "task_summary.py"
tasks_file = here / "skills" / "task-summary" / "sample-tasks.md"
expected_file = here / "skills" / "task-summary" / "expected-output.json"

failures = []

# Check 1: Python version
version = ".".join(str(n) for n in sys.version_info[:3])
if sys.version_info[:2] >= MIN_PYTHON:
    print(f"[ok]   Python {version}")
else:
    failures.append(f"Python {version} is too old; need {MIN_PYTHON[0]}.{MIN_PYTHON[1]} or newer")
    print(f"[fail] {failures[-1]}")

# Check 2: the skill script runs on the sample data
result = subprocess.run(
    [sys.executable, str(script), str(tasks_file), "--today", "2026-10-27"],
    capture_output=True, text=True,
)
if result.returncode != 0:
    failures.append(f"task_summary.py exited with code {result.returncode}: {result.stderr.strip()}")
    print(f"[fail] {failures[-1]}")
else:
    print("[ok]   task_summary.py runs")

    # Check 3: its output matches the expected output
    try:
        actual = json.loads(result.stdout)
    except json.JSONDecodeError:
        actual = None
    expected = json.loads(expected_file.read_text(encoding="utf-8"))
    if actual == expected:
        print(f"[ok]   Output matches expected-output.json ({actual['open_count']} open tasks)")
    else:
        failures.append("Output does not match skills/task-summary/expected-output.json")
        print(f"[fail] {failures[-1]}")

print()
if failures:
    print("FAIL")
    sys.exit(1)
print("PASS")
