
import pytest
from scholarship_awards import (
    award_amount,
    is_eligible,
    application_status
)


# 1. Award amount tests

def test_unknown_category():
    with pytest.raises(ValueError):
        award_amount("science", 90, "low", False)


def test_negative_marks():
    with pytest.raises(ValueError):
        award_amount("merit", -5, "low", False)


def test_merit_renewal_low_income():
    assert award_amount("merit", 100, "low", True) == 4800


def test_sports_high_income():
    assert award_amount("sports", 70, "high", True) == 600


def test_marks_equal_to_cutoff():
    assert award_amount("merit", 75, "low", False) == 0


# 2. Eligibility tests

def test_special_quota_eligible():
    assert is_eligible(50, 2, True) is True


def test_special_quota_not_eligible():
    assert is_eligible(90, 3, True) is False


def test_low_attendance():
    assert is_eligible(70, 0, False) is False


def test_normal_eligible():
    assert is_eligible(80, 1, False) is True


def test_normal_not_eligible():
    assert is_eligible(80, 2, False) is False


# 3. Application status tests

def test_normal_application_open():
    assert application_status(20, False, False) == "open"


def test_renewal_paper_open():
    assert application_status(40, True, True) == "open"


def test_application_closing():
    assert application_status(15, False, False) == "closing"


def test_application_closed():
    assert application_status(4, False, False) == "closed"
