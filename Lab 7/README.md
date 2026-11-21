# Lab 7 — Fuzz Testing for Input Validation Bugs

## Objective
Use Hypothesis property-based fuzz testing to detect invalid-input crashes and harden the three scholarship-award processing functions.

## Files
- `scholarship_awards.py`: fixed Python application.
- `test_scholarship_awards.py`: Hypothesis no-crash fuzz tests for all three functions.
- `Lab7_Test_Report.md`: observations and recorded results.

## Run
```powershell
python -m pip install hypothesis pytest
python scholarship_awards.py
python -m pytest test_scholarship_awards.py -v
```

Example inputs: `merit:82`, `72,85,90`, `5000|500`.

Invalid inputs return `None` instead of raising unhandled exceptions. The initial Python app's award parser was observed crashing for input `500` (missing `|`). The first pytest attempt had a syntax/indentation error in the unfinished test file; this was not a Hypothesis test failure. After completing the tests and fixing the application, the user observed all three tests passing.
