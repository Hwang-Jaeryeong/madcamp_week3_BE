# peoples/models.py

from django.db import models
from django.conf import settings
from PIL import Image

class Person(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    date = models.DateField()
    exis = models.TextField()
    motto = models.TextField()
    introduction = models.TextField()
    picture_url = models.ImageField(upload_to='person_images/', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.picture_url:
            img = Image.open(self.picture_url.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.picture_url.path)
