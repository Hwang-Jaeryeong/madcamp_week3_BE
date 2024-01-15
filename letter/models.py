# letter/models.py

from django.db import models
from peoples.models import Person
from django.conf import settings

class Letter(models.Model):
    author = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Letter {self.id} - Author: {self.author}, Receiver: {self.receiver}"
