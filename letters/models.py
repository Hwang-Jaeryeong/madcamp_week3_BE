# letters/models.py
from django.conf import settings
from django.db import models

class Letter(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    is_public = models.BooleanField(default=False)

