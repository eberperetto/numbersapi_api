import requests
from django.http.response import JsonResponse
from django.views import View

from api.utils import (
    get_validated_get_parameters,
    join_numbersapi_get_parameters,
    join_numbersapi_get_url,
)

API_URL = "http://www.numbersapi.com/"


class GetFact(View):
    """ Main view, handles every request combining the possible get parameters """

    # TODO: describe each possible parameter and combinations
    def get(self, request, *args, **kwargs):
        get_parameters = self.request.GET
        validated_get_parameters = get_validated_get_parameters(get_parameters)
        if validated_get_parameters.get("error", None) is not None:
            return JsonResponse({"error": validated_get_parameters["error"]})

        numbersapi_get_url = join_numbersapi_get_url(validated_get_parameters)
        numbersapi_get_parameters = join_numbersapi_get_parameters(get_parameters)
        # TODO: handle request timeout
        r = requests.get(f"{API_URL}{numbersapi_get_url}{numbersapi_get_parameters}")
        return JsonResponse(
            {
                "text": r.json().get("text", ""),
                "type": r.json().get("type", ""),
                "number": validated_get_parameters.get("number", ""),
                "error": "",
            }
        )
