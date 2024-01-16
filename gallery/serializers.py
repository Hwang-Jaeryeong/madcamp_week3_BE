# gallery/serializers.py

from rest_framework import serializers
from .models import Gallery

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'receiver', 'picture', 'content']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.picture and hasattr(instance.picture, 'url'):
            request = self.context.get('request')
            if request is not None:
                representation['picture'] = request.build_absolute_uri(instance.picture.url)
        return representation
