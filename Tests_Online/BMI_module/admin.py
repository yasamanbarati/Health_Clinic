from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.BMIModels)
admin.site.register(models.DiseaseGroupModels)
admin.site.register(models.FoodModels)
admin.site.register(models.BodyMassModels)
admin.site.register(models.Comment)
admin.site.register(models.VideoResultModels)
