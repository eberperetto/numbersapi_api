from django.urls import path

from api import views

urlpatterns = [
    path("", views.RandomTypeless.as_view(), name="default"),
    path("random", views.RandomTypeless.as_view(), name="random"),
    path("random/<str:fact_type>", views.RandomTyped.as_view(), name="random_typed"),
    path("<int:number>", views.NumberTypeless.as_view(), name="number"),
    path("<int:month>/<int:day>", views.DateTyped.as_view(), name="date"),
    path(
        "<int:number>/<str:fact_type>", views.NumberTyped.as_view(), name="number_typed"
    ),
]