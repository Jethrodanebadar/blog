from django.db import models

# Create your models here.
class blog_data(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField()
    