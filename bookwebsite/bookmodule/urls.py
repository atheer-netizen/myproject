from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('index/<int:val1>/', views.index),
]