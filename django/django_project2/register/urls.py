from django.urls import path

from . import views

urlpatterns = [
    path('r', views.register, name="register"),
    path('hello', views.hello, name="hello"),
    path('hello-login', views.hello_login, name='hello_login')
]