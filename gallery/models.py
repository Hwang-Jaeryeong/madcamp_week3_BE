# gallery/models.py

from django.db import models
from peoples.models import Person
from django.conf import settings
from PIL import Image

class Gallery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    receiver = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='gallery_images/', null=True, blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return f"Gallery {self.id} - User: {self.user.username}, Receiver: {self.receiver}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.picture:
            self.save_picture_url()

    def save_picture_url(self):
        img = Image.open(self.picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)

