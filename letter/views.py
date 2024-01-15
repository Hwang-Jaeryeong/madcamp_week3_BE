# letters/views.py
from rest_framework import generics, permissions
from .models import Letter
from .serializers import LetterSerializer
from peoples.models import Person
from rest_framework.generics import ListAPIView


class LetterListCreateView(generics.ListCreateAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        receiver_name = self.request.data.get('receiver', '')

        if receiver_name:
            receivers = Person.objects.filter(name=receiver_name)
            return Letter.objects.filter(author=user, receiver__in=receivers)
        else:
            return Letter.objects.filter(author=user)

    def perform_create(self, serializer):
        author = self.request.data.get('author', '')
        receiver_name = self.request.data.get('receiver', '')
        receivers = Person.objects.filter(name=receiver_name)

        if receivers.exists():
            receiver = receivers.first()  # You can choose how to handle multiple receivers
            serializer.save(author=author, receiver=receiver)
        else:
            # Handle the case where the receiver doesn't exist
            pass

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
        receiver_name = self.request.data.get('receiver', '')
        letters = Letter.objects.filter(receiver=receiver_name)
        return letters
