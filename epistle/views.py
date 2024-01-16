# letters/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics, permissions
from .models import Letter
from .serializers import LetterSerializer
from peoples.models import Person
from rest_framework.permissions import IsAuthenticated

class LetterListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, receiver_id):
        # Extracting data from the request body
        content = request.data.get('content', '')
        author = request.data.get('author', '')

        # Retrieving the receiver from the database
        try:
            receiver = Person.objects.get(id=receiver_id)
        except Person.DoesNotExist:
            return Response({"detail": "Receiver not found"}, status=status.HTTP_404_NOT_FOUND)

        # Creating the letter
        letter = Letter.objects.create(content=content, author=author, receiver=receiver)

        # Serializing the response
        serializer = LetterSerializer(letter)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LetterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Letter.objects.filter(author=user)

class LetterListViewByReceiver(generics.ListAPIView):
    serializer_class = LetterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        receiver_id = self.kwargs.get('receiver_id', None)
        return Letter.objects.filter(receiver_id=receiver_id)

