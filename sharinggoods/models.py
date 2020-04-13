from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Content(models.Model):
    goods_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    uploader_name = models.CharField(max_length=10)
    state = models.BooleanField(default=True)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(default='')

class Comment(models.Model):
    user_name = models.CharField(max_length=10)
    comments = models.TextField(max_length=400)
    pub_time = models.DateTimeField(default=timezone.now)    