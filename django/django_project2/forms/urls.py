from django.urls import path

from . import views

app_name = "forms"

urlpatterns = [
    path("form1", views.form1, name="form1"),
]