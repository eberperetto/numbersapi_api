import requests
from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View

from api.utils import (
    get_validated_get_parameters,
    join_numbersapi_get_parameters,
    join_numbersapi_get_url,
)

API_URL = "http://www.numbersapi.com/"


class GetFact(View):
    """
    Handles every request combining the following possible get parameters:
    - number: the number whose fact will be retrieved, can be
        either an integer number or the word "random". Use the day and
        month parameters instead when requesting the "date" fact type.
        Default: "random"
    - fact_type: the type of the fact, should be one of the
        following: "trivia", "math", "year" and "date".
        Default: "trivia"
    - month: when the fact type is a "date", this needs to be
        informed, with a valid month from 1-12.
    - day: when the fact type is a "date", this needs to be
        informed, with a valid day from 1-31.
    - fragment: sets the fact text to return as a fragment
        to be used inside a sentence, no value needed.
    - default: text to be retrieved when the queried number
        is not found. Default: `n` is a boring number.
    - notfound: informs what should be done when the number
        is not found, should be one of the following: "default", "floor" (rounds
         the number to the next lowest found) and "ceil" (rounds the number
         to the next highest found). Default: the default parameter value
    - min: sets a lower integer threshold to the "random" number,
        should be used along with the max parameter.
    - max: sets a higher integer threshold to the "random" number,
        should be used along with the min parameter.
    """

    def get(self, request, *args, **kwargs):
        # Validate get parameters, returning the error message if not valid
        get_parameters = self.request.GET
        validated_get_parameters = get_validated_get_parameters(get_parameters)
        if validated_get_parameters.get("error", None) is not None:
            return JsonResponse({"error": validated_get_parameters["error"]})

        # Join the URL and parameters to form a valid request to NumbersAPI
        numbersapi_get_url = join_numbersapi_get_url(validated_get_parameters)
        numbersapi_get_parameters = join_numbersapi_get_parameters(get_parameters)
        try:
            # Performs the request and retrieve response
            r = requests.get(
                f"{API_URL}{numbersapi_get_url}{numbersapi_get_parameters}"
            )
            return JsonResponse(
                {
                    "text": r.json().get("text", ""),
                    "type": r.json().get("type", ""),
                    "number": validated_get_parameters.get("number", ""),
                    "error": "",
                }
            )
        except requests.exceptions.RequestException as e:
            # Handle request timeout and other possible errors
            return JsonResponse({"error": f"{e}"})


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html", {"domain": settings.DOMAIN})
