from django.urls import path

from api import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("get_fact", views.GetFact.as_view(), name="get_fact"),
]