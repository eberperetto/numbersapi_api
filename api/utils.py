from django.http.request import QueryDict

from api.validators import (
    validate_date,
    validate_day,
    validate_fact_type,
    validate_month,
    validate_number,
)


def get_validated_get_parameters(get_parameters: QueryDict) -> dict:
    response = {
        "number": "random",
        "fact_type": None,
        "date": None,
        "error": None,
    }

    # Validate number
    if "number" in get_parameters:
        number = get_parameters["number"]
        if validate_number(number) == False:
            response[
                "error"
            ] = "Inform a valid number option: an integer or the word random"
            return response
        response["number"] = number

    # Validate fact type
    if "fact_type" in get_parameters:
        fact_type = get_parameters["fact_type"]
        if validate_fact_type(fact_type) == False:
            response[
                "error"
            ] = "Invalid fact type. Should be one of: trivia, math, date or year"
            return response
        response["fact_type"] = fact_type

    # Validate date request, which should have valid 'day' and 'month' parameters,
    # paired with the "date" 'fact_type' parameter
    if "month" in get_parameters:
        if "day" in get_parameters:
            month = get_parameters["month"]
            if validate_month(month) == False:
                response["error"] = "Invalid month. Should be a number from 1-12"
                return response

            day = get_parameters["day"]
            if validate_day(day) == False:
                response["error"] = "Invalid day. Should be a number from 1-31"
                return response

            date = f"{month}/{day}"
            if validate_date(date) == False:
                response["error"] = "Invalid date. Should be a valid month/day pair"
                return response

            if date is not None and response["fact_type"] != "date":
                response[
                    "error"
                ] = "Invalid date/fact type pair. Should be a valid month/day paired with the fact_type 'date'"
                return response
            response["number"] = date
    return response


def join_numbersapi_get_parameters(get_parameters: QueryDict) -> str:
    # Always appends json as a default get parameter
    response = "?json"
    if "fragment" in get_parameters:
        response += "&fragment"
    if "notfound" in get_parameters:
        response += f"&notfound={get_parameters['notfound']}"
    if "default" in get_parameters:
        response += f"&default={get_parameters['default']}"
    if "min" in get_parameters:
        if "max" in get_parameters:
            if get_parameters["min"] != "" and get_parameters["max"] != "":
                response += f"&min={get_parameters['min']}&max={get_parameters['max']}"
    return response


def join_numbersapi_get_url(get_parameters: dict) -> str:
    response = get_parameters["number"]
    if get_parameters["fact_type"] is not None:
        response += f"/{get_parameters['fact_type']}"
    return response
