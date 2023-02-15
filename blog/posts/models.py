from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100000)
    created_at = models.DateTimeField(default=datetime.datetime.now, blank=True)