# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'phone_number', 'nickname', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return super().create(validated_data)
