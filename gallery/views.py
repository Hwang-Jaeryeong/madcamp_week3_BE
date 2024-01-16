# gallery/views.py
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Gallery
from .serializers import GallerySerializer
from peoples.models import Person
from rest_framework.permissions import IsAuthenticated

class GalleryCreateView(generics.CreateAPIView):
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        receiver_id = self.kwargs.get('receiver_id')
        receiver = get_object_or_404(Person, id=receiver_id)
        serializer.save(user=user, receiver=receiver)


        # serializer.data에서 이미지의 상대 경로를 가져옵니다.
        image_relative_path = serializer.data.get('picture', '')

        # request.build_absolute_uri 메서드를 사용하여 절대 경로로 변환합니다.
        absolute_image_url = self.request.build_absolute_uri(image_relative_path)

        # serializer.data에 변환된 절대 경로를 다시 저장합니다.
        serializer.data['picture'] = absolute_image_url

class GalleryListViewByReceiver(generics.ListAPIView):
    serializer_class = GallerySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        receiver_id = self.kwargs.get('receiver_id', None)
        return Gallery.objects.filter(receiver_id=receiver_id)