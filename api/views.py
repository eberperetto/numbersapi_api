import json, requests
from django.http.request import QueryDict
from django.http.response import JsonResponse
from django.views import View

API_URL = "http://www.numbersapi.com"


def join_valid_get_arguments(get_arguments: QueryDict) -> str:
    # Always appends json as a get argument
    response = "?json"
    if "fragment" in get_arguments:
        response += "&fragment"
    if "notfound" in get_arguments:
        response += f"&notfound={get_arguments['notfound']}"
    if "default" in get_arguments:
        response += f"&default={get_arguments['default']}"
    if "min" in get_arguments:
        if "max" in get_arguments:
            if get_arguments["min"] != "" and get_arguments["max"] != "":
                response += f"&min={get_arguments['min']}&max={get_arguments['max']}"
    return response


def validate_fact_type(fact_type: str) -> bool:
    return fact_type in ["trivia", "math", "year"]


class RandomTypeless(View):
    def get(self, request, *args, **kwargs):
        joined_valid_get_arguments = join_valid_get_arguments(self.request.GET)
        r = requests.get(f"{API_URL}/random{joined_valid_get_arguments}")
        # TODO: format response
        return JsonResponse(r.json())


class RandomTyped(View):
    def get(self, request, *args, **kwargs):
        fact_type = self.kwargs["fact_type"]
        if validate_fact_type(fact_type) is False:
            # TODO: format response
            return JsonResponse(
                {
                    "text": "",
                    "number": "random",
                    "type": fact_type,
                    "error": "Invalid fact type. Should be one of: trivia, math or year",
                }
            )
        joined_valid_get_arguments = join_valid_get_arguments(self.request.GET)
        r = requests.get(f"{API_URL}/random/{fact_type}{joined_valid_get_arguments}")
        # TODO: format response
        return JsonResponse(r.json())


class NumberTypeless(View):
    def get(self, request, *args, **kwargs):
        # TODO: validate number
        number = self.kwargs["number"]
        joined_valid_get_arguments = join_valid_get_arguments(self.request.GET)
        r = requests.get(f"{API_URL}/{number}{joined_valid_get_arguments}")
        # TODO: format response
        return JsonResponse(r.json())


class NumberTyped(View):
    def get(self, request, *args, **kwargs):
        # TODO: validate number
        number = self.kwargs["number"]
        fact_type = self.kwargs["fact_type"]
        if validate_fact_type(fact_type) is False:
            # TODO: format response
            return JsonResponse(
                {
                    "text": "",
                    "number": number,
                    "type": fact_type,
                    "error": "Invalid fact type. Should be one of: trivia, math or year",
                }
            )
        joined_valid_get_arguments = join_valid_get_arguments(self.request.GET)
        r = requests.get(f"{API_URL}/{number}/{fact_type}{joined_valid_get_arguments}")
        # TODO: format response
        return JsonResponse(r.json())


class DateTyped(View):
    def get(self, request, *args, **kwargs):
        # TODO: validate month and day
        month = self.kwargs["month"]
        day = self.kwargs["day"]
        joined_valid_get_arguments = join_valid_get_arguments(self.request.GET)
        r = requests.get(f"{API_URL}/{month}/{day}/date/{joined_valid_get_arguments}")
        # TODO: format response
        return JsonResponse(r.json())