from django.contrib import admin

# Register your models here.
from .models import PlantType, PlantTypeEvent

# Register your models here.
admin.site.register(PlantType)
admin.site.register(PlantTypeEvent)