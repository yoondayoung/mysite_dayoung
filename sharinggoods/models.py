from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Content(models.Model):
    objects = models.Manager()
    goods_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    uploader_name = models.CharField(max_length=10)
    state = models.BooleanField(default=True)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(default='')
    image = models.ImageField(blank=True, upload_to="sharinggoods/products/%Y/%m/%d")

    def __str__(self):
        return self.goods_name

class Comment(models.Model):
    objects = models.Manager()
    post = models.ForeignKey('Content', on_delete=models.CASCADE)
    user = models.CharField(default='', max_length=10)
    text = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now)
