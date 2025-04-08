from django.urls import path
from .views import web

urlpatterns = [
    path("catalog/", web, name="web"),
]