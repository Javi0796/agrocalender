from django.db import models

# Create your models here.
class PlantType(models.Model):
    plantName = models.CharField(max_length=255)

    def __str__(self):
        return self.plantName
    
class PlantTypeEvent(models.Model):
    plant_type = models.ForeignKey(
        PlantType,
        on_delete=models.CASCADE,
        related_name="events"
    )