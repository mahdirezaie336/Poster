from django.db import models


# Create your models here.
class Post(models.Model):
    STATE_CHOICE = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
    ]
    description = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255)
    state = models.CharField(max_length=255, choices=STATE_CHOICE, default='P')
    category = models.CharField(max_length=255, blank=True, null=True)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/images/', blank=True, null=True)
    # image_url = models.CharField(max_length=255, blank=True, null=True)
