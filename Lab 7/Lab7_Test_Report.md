# Lab 7 — Fuzz Testing Evidence Report

**Repository:** SE-PES1UG24CS232  
**Application:** Scholarship Awards  
**Tools:** Python 3.13, pytest 8.3.4, Hypothesis 6.170.17

## Original application behavior
- `parse_applicant("merit:82")` returned `('Merit', 82.0)`.
- `marks_average("72,82")` returned `77`.
- `payable_award("500")` crashed with `ValueError: not enough values to unpack (expected 2, got 1)`. The function required `award|deduction` but did not validate the separator.

## Initial test execution
The unfinished `test_scholarship_awards.py` produced `IndentationError: expected an indented block after function definition on line 5`. Pytest reported `collected 0 items / 1 error`. This was a test collection error, **not** a Hypothesis-discovered counterexample.

## Changes made
- Completed `@given(st.text() | st.none())` Hypothesis tests for the three functions.
- Added type, separator, number, and finite-value validation to application functions.
- Invalid inputs return `None` instead of causing unhandled exceptions.

## Fixed application output
Inputs: `merit:82`, `72,85,90`, `5000|500`.

```text
Category and Marks: ('Merit', 82.0)
Average Marks: 82
Payable Award: 5400.0
```

## Final fuzz test results
```text
test_parse_applicant_no_crash PASSED
test_marks_average_no_crash PASSED
test_payable_award_no_crash PASSED

3 passed in 1.88s
```

The text above transcribes screenshots shared during the lab. The original screenshot-based PDF evidence report was prepared separately; this Markdown file does not embed those screenshots.
