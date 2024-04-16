from django.urls import path
from .views import hello_webpack

urlpatterns = [
    path('hello-webpack/', hello_webpack, name='hello_webpack'),
]