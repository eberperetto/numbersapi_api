from django.contrib import admin
from django.urls import include, path
from api.views import Index

urlpatterns = [
    path("", Index.as_view()),
    path("api/", include("api.urls")),
    path("admin/", admin.site.urls),
]
