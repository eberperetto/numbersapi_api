import requests
import datetime as dt
from django.http.request import QueryDict
from django.http.response import JsonResponse
from django.views import View

API_URL = "http://www.numbersapi.com/"


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
    # Always appends json as a get parameter
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


def join_numbersapi_get_url(get_parameters: dict) -> str:
    response = get_parameters["number"]
    if get_parameters["fact_type"] is not None:
        response += f"/{get_parameters['fact_type']}"
    return response


class GetFact(View):
    """ Main view, handles every request combining the possible get parameters """

    def get(self, request, *args, **kwargs):
        get_parameters = self.request.GET
        validated_get_parameters = get_validated_get_parameters(get_parameters)
        if validated_get_parameters.get("error", None) is not None:
            # TODO: format response
            return JsonResponse(validated_get_parameters)

        numbersapi_get_url = join_numbersapi_get_url(validated_get_parameters)

        numbersapi_get_parameters = join_numbersapi_get_parameters(self.request.GET)
        r = requests.get(f"{API_URL}{numbersapi_get_url}{numbersapi_get_parameters}")
        # TODO: format response
        return JsonResponse(r.json())
