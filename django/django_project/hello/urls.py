from django.urls import path

from . import views

urlpatterns = [
    path("", views.hello),
    path("3/", views.hello3),
    path("4/", views.hello4),
    path('<str:name>/', views.hello2)
]