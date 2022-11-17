from django.db import models


# Create your models here.
class Post(models.Model):
    CATEGORY_CHOICE = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
    ]
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255)
    state = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, null=True, choices=CATEGORY_CHOICE, default='P')
