# letters/models.py

from django.db import models
from peoples.models import Person
from django.conf import settings

class Letter(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    receiver = models.CharField(max_length=255)
    content = models.TextField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f"Letter {self.id} - Author: {self.author.username}, Receiver: {self.receiver}"
