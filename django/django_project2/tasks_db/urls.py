from django.urls import path

from . import views

app_name = 'tasks_db'

urlpatterns = [
    path("", views.index, name="index"),
    path("register-task/", views.register, name="register"),
    path("update/<int:task_id>", views.update, name="update"),
    path("delete/<int:task_id>", views.delete, name="delete")
]