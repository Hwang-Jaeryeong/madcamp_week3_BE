# gallery/urls.py

from django.urls import path
from .views import GalleryCreateView, GalleryListViewByReceiver

urlpatterns = [
    path('<int:receiver_id>/', GalleryCreateView.as_view(), name='gallery-create'),
    path('list/<int:receiver_id>/', GalleryListViewByReceiver.as_view(), name='gallery-list-by-receiver'),
]
