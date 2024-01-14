# letters/urls.py

from django.urls import path
from .views import LetterListCreateView, LetterDetailView, LetterListViewByReceiver

urlpatterns = [
    path('', LetterListCreateView.as_view(), name='letter-list-create'),
    path('letters/', LetterDetailView.as_view(), name='letter-detail'),
    path('list/', LetterListViewByReceiver.as_view(), name='letter-list-by-receiver'),

]
