from django.db import models


# Create your models here.
class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    state = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
