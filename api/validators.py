import datetime as dt


def validate_number(number: str) -> bool:
    if number == "random":
        return True
    try:
        number = int(number)
        return True
    except ValueError:
        return False


def validate_month(month: str) -> bool:
    try:
        month = int(month)
        return month >= 1 and month <= 12
    except ValueError:
        return False


def validate_day(day: str) -> bool:
    try:
        day = int(day)
        return day >= 1 and day <= 31
    except ValueError:
        return False


def validate_date(date: str) -> bool:
    try:
        # Validate date value using a leap year to ensure Feb. 29th validation
        date = dt.datetime.strptime(f"{date}/2000", "%m/%d/%Y")
        return True
    except ValueError:
        return False


def validate_fact_type(fact_type: str) -> bool:
    return fact_type in ["trivia", "math", "date", "year"]