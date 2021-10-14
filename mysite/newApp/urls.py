from django.urls import path
from newApp import views

urlpatterns = [
    path('', views.helloWorld, name='hello_world'),
]