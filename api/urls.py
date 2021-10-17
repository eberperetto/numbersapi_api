from django.urls import path

from api import views

urlpatterns = [
    path("", views.GetFact.as_view(), name="default"),
    path("get_fact", views.GetFact.as_view(), name="get_fact"),
    # TODO: get range of number facts using batch
    # path("get_facts", views.GetFacts.as_view(), name="get_facts"),
]