from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path("", views.index),
    path("register-task/", views.register, name="register")
]