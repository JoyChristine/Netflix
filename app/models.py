from unicodedata import name
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    poster = models.ImageField(upload_to='movie_pic/')
    description = models.TextField()
