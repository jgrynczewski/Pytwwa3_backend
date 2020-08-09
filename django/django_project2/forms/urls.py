from django.urls import path

from . import views

app_name = "forms"

urlpatterns = [
    path("form1", views.form1, name="form1"),
    path("form2", views.form2, name="form2"),
    path("form3", views.form3, name="form3"),
]