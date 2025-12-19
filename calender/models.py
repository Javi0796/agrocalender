from django.db import models

from plantings.models import Planting

# Create your models here.
class CalendarEvent(models.Model):
    planting = models.ForeignKey(Planting, on_delete=models.CASCADE)
    date = models.DateField()
    action = models.CharField(max_length=100)