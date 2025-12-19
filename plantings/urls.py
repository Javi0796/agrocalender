from django.urls import path
from . import views

urlpatterns = [
    path('planting', views.plantings, name='plantings'),
]
