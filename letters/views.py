# letters/views.py
from rest_framework import generics, permissions
from .models import Letter
from .serializers import LetterSerializer

class LetterListCreateView(generics.ListCreateAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Letter.objects.filter(author=user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class LetterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Letter.objects.filter(author=user)
