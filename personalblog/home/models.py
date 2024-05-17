from django.db import models

# Create your models here.
class blog_data(models.Model):
    title = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    