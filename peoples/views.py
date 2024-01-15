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
        # POST 요청으로 name과 이미지를 전달받아 해당하는 Person 객체 정보를 반환합니다.
        name = self.request.data.get('name', None)
        image = self.request.data.get('file', None)  # 'file' 키로부터 이미지를 가져옴

        if name and image:
            person = Person.objects.filter(name=name, user=request.user).first()
            if person:
                # 이미지 업로드 및 크기 조절 처리
                person.picture_url = image
                person.save()

                serializer = self.get_serializer(person)
                return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'error': 'Person not found or image not provided.'}, status=status.HTTP_404_NOT_FOUND)

