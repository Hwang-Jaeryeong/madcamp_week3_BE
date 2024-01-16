# letter/models.py

from django.db import models
from peoples.models import Person

class Letter(models.Model):
    author = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='received_letters')

    def __str__(self):
        return f"Letter {self.id} - Author: {self.author}, Receiver: {self.receiver}"
