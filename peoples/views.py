# peoples/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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

class PersonDetailView(generics.CreateAPIView):
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        name = request.data.get('name', None)
        image = request.data.get('file', None)  # 이미지 파일을 'file' 필드에서 가져옴

        if not name:
            return Response({'error': 'Name is required.'}, status=status.HTTP_400_BAD_REQUEST)

        person, created = Person.objects.get_or_create(name=name, user=request.user)

        if image:
            person.picture_url = image
            person.save()
        else:
            return Response({'error': 'Image file is required.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(person)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)


