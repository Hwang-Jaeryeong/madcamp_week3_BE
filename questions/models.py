# questions/models.py
from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    exis = models.CharField(max_length=255)
    motto = models.CharField(max_length=255)
    introduction = models.TextField()
    picture_url = models.URLField()

