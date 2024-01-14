# gallery/urls.py

from django.urls import path
from .views import GalleryCreateView, GalleryListViewByReceiver

urlpatterns = [
    path('', GalleryCreateView.as_view(), name='gallery-create'),
    path('list/', GalleryListViewByReceiver.as_view(), name='gallery-list-by-receiver'),
]
