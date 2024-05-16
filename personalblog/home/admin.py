from django.contrib import admin
from . import models
# Register your models here.

class Blog(admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(models.blog_data, Blog)