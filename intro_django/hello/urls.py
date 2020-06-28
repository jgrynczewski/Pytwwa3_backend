from django.urls import path
from . import views

urlpatterns = [
    path("foo", views.hello),
    path("bar", views.drugi),
    path("buz", views.trzeci)
]