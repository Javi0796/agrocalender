from django.db import models
from django.contrib.auth.models import User
from plants.models import PlantType

# Create your models here.
class Planting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="plantings")
    plant_type = models.ForeignKey(PlantType, on_delete=models.CASCADE)
    planting_date = models.DateField()

    def __str__(self):
        return f"{self.plant_type} planted by {self.user.username} on {self.planting_date}"