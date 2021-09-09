from django.contrib import admin

from app import models

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    pass
