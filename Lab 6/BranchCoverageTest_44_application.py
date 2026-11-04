
import pytest
from scholarship_awards import (
    award_amount,
    is_eligible,
    application_status
)


# Award amount: test all decision branches

def test_unknown_category():
    with pytest.raises(ValueError):
        award_amount("science", 90, "low", False)


def test_negative_marks():
    with pytest.raises(ValueError):
        award_amount("merit", -5, "low", False)


def test_renewal_merit():
    assert award_amount("merit", 80, "low", True) == 1000


def test_renewal_sports():
    assert award_amount("sports", 80, "high", True) == 2000


def test_non_renewal():
    assert award_amount("arts", 80, "low", False) == 1500


def test_at_cutoff():
    assert award_amount("merit", 75, "low", False) == 0


def test_high_income_rate():
    assert award_amount("merit", 80, "high", False) == 300


def test_low_income_large_bonus():
    assert award_amount("merit", 100, "low", False) == 4000


def test_high_income_large_bonus():
    assert award_amount("merit", 100, "high", False) == 2500


# Eligibility: test all decision branches

def test_special_quota_yes():
    assert is_eligible(50, 2, True) is True


def test_special_quota_no():
    assert is_eligible(90, 3, True) is False


def test_attendance_below_75():
    assert is_eligible(74, 0, False) is False


def test_attendance_75_backlogs_zero():
    assert is_eligible(75, 0, False) is True


def test_normal_quota_backlogs_one():
    assert is_eligible(90, 1, False) is True


def test_normal_quota_backlogs_two():
    assert is_eligible(90, 2, False) is False


# Application status: test all decision branches

def test_normal_open():
    assert application_status(20, False, False) == "open"


def test_normal_closing():
    assert application_status(10, False, False) == "closing"


def test_normal_closed():
    assert application_status(4, False, False) == "closed"


def test_renewal_open():
    assert application_status(30, True, False) == "open"


def test_renewal_closing():
    assert application_status(20, True, False) == "closing"


def test_renewal_closed():
    assert application_status(10, True, False) == "closed"


def test_paper_application_open():
    assert application_status(30, False, True) == "open"


def test_paper_application_closing():
    assert application_status(15, False, True) == "closing"


def test_paper_application_closed():
    assert application_status(4, False, True) == "closed"


def test_renewal_paper_open():
    assert application_status(40, True, True) == "open"
