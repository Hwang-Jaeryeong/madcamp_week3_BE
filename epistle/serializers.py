# letter/serializers.py

from rest_framework import serializers
from .models import Letter

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = ['id', 'content', 'author', 'timestamp', 'receiver']
