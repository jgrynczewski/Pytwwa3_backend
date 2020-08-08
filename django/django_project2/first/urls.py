from django.urls import path

from . import views

urlpatterns = [
    path("", views.hello),
    path("test/<int:num>/c", views.test),
    path("<str:foo>/", views.read)
]
