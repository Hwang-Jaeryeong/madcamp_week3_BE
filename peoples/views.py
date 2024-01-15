# peoples/views.py

from rest_framework import generics, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Person
from .serializers import PersonSerializer

class PersonListCreateView(generics.ListCreateAPIView):
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Person.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class PersonDetailView(CreateAPIView):
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        name = request.data.get('name', None)
        image_file = request.FILES.get('picture_url', None)  # 'file' 키로부터 이미지 파일을 가져옴

        if not name or not image_file:
            return Response({'error': 'Name and image file are required.'}, status=status.HTTP_400_BAD_REQUEST)

        person, created = Person.objects.get_or_create(name=name, user=request.user)

        if image_file:
            # 이미지 파일을 저장하고 URL 생성
            file_name = default_storage.save(image_file.name, ContentFile(image_file.read()))
            image_url = request.build_absolute_uri(default_storage.url(file_name))

            person.picture_url = image_url
            person.save()

        serializer = self.get_serializer(person)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

