from django.contrib import admin
from . import models

admin.site.register(models.UserProfile)
admin.site.register(models.PayementRecipe)
admin.site.register(models.Message)
