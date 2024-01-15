# gallery/models.py

from django.db import models
from peoples.models import Person
from django.conf import settings

class Gallery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    receiver = models.CharField(max_length=255)
    picture = models.URLField()
    content = models.TextField(blank=True)

    def __str__(self):
        return f"Gallery {self.id} - User: {self.user.username}, Receiver: {self.receiver}"
