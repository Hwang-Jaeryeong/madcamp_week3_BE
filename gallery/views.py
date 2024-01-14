# gallery/views.py

from rest_framework import generics, permissions
from .models import Gallery
from .serializers import GallerySerializer

class GalleryCreateView(generics.CreateAPIView):
    serializer_class = GallerySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GalleryListViewByReceiver(generics.ListAPIView):
    serializer_class = GallerySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        receiver_name = self.request.data.get('receiver', '')
        return Gallery.objects.filter(receiver=receiver_name, user=self.request.user)

