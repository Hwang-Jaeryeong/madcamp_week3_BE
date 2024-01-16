# letters/urls.py
from django.urls import path
from .views import LetterListCreateView, LetterDetailView, LetterListViewByReceiver

urlpatterns = [
    path('list/<int:receiver_id>/', LetterListViewByReceiver.as_view(), name='letter-list-by-receiver'),
    path('<int:receiver_id>/', LetterListCreateView.as_view(), name='letter-list-create'),
]

