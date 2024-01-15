# peoples/serializers.py
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'date', 'exis', 'motto', 'introduction', 'picture_url')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.picture_url and hasattr(instance.picture_url, 'url'):
            request = self.context.get('request')
            if request is not None:
                representation['picture_url'] = request.build_absolute_uri(instance.picture_url.url)
        return representation


