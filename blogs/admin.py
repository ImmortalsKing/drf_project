from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    pass