from django.db import models
import uuid
import os


def path_and_rename(instance, filename):
    """
    This function is used in the image field to rename the image to a random name.
    """
    upload_to = ''  # Directory to upload to
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(str(uuid.uuid4()), ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


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
    image = models.ImageField(upload_to=path_and_rename, blank=True, null=True)


# class PostImage(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='store/images/', blank=True, null=True)
#     # image_url = models.CharField(max_length=255, blank=True, null=True)
