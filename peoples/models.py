# peoples/models.py

from django.db import models
from django.conf import settings
import uuid


class Person(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    date = models.DateField()
    exis = models.TextField()
    motto = models.TextField()
    introduction = models.TextField()
    picture_url = models.URLField()

    def __str__(self):
        return self.name
