from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpRequest
from rest_framework import generics, permissions, status, request
from rest_framework.response import Response
from .models import Gallery
from .serializers import GallerySerializer

class GalleryCreateView(generics.CreateAPIView):
    serializer_class = GallerySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # request 객체에서 user 정보를 가져옵니다.
        user = self.request.user

        # serializer.save()를 호출하기 전에 user 정보를 저장합니다.
        serializer.save(user=user)

        # serializer.data에서 이미지의 상대 경로를 가져옵니다.
        image_relative_path = serializer.data.get('picture', '')

        # HttpRequest.build_absolute_uri 메서드를 사용하여 절대 경로로 변환합니다.
        absolute_image_url = HttpRequest.build_absolute_uri(self.request, image_relative_path)

        # serializer.data에 변환된 절대 경로를 다시 저장합니다.
        serializer.data['picture'] = absolute_image_url

class GalleryListViewByReceiver(generics.ListAPIView):
    serializer_class = GallerySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        receiver_name = self.request.data.get('receiver', '')
        return Gallery.objects.filter(receiver=receiver_name, user=self.request.user)


