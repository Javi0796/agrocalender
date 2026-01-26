from django.urls import path
from . import views

urlpatterns = [
    path('plantings/', views.plantings, name='plantings'),
]
