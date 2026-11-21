import math


def parse_applicant(text):
    if not isinstance(text, str):
        return None

    try:
        category, marks = text.split(':')
        category = category.strip().title()
        marks = float(marks)

        if not category or not math.isfinite(marks):
            return None

        return category, marks
    except (ValueError, TypeError):
        return None


def marks_average(marks_csv):
    if not isinstance(marks_csv, str):
        return None

    try:
        values = [int(r.strip()) for r in marks_csv.split(',')]

        if not values:
            return None

        return sum(values) // len(values)
    except (ValueError, TypeError):
        return None


def payable_award(text):
    if not isinstance(text, str):
        return None

    try:
        award, deduction = text.split('|')
        award = float(award)
        deduction = float(deduction)

        if not math.isfinite(award) or not math.isfinite(deduction):
            return None

        if award < 0 or deduction < 0:
            return None

        total = award * 1.18 - deduction

        if not math.isfinite(total):
            return None

        return max(total, 0)
    except (ValueError, TypeError, OverflowError):
        return None


def main():
    print("==== Running parse_applicant ====")
    user_input = input("Enter category:marks (e.g. merit:82): ")
    result = parse_applicant(user_input)
    print("Category and Marks:", result)

    print("\n==== Running marks_average ====")
    user_input = input("Enter marks as CSV (e.g. 72,85,90): ")
    result = marks_average(user_input)
    print("Average Marks:", result)

    print("\n==== Running payable_award ====")
    user_input = input("Enter award|deduction (e.g. 5000|500): ")
    result = payable_award(user_input)
    print("Payable Award:", result)


if __name__ == "__main__":
    main()
