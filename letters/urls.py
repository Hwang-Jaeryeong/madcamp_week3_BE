# letters/urls.py
from django.urls import path
from .views import LetterListCreateView, LetterDetailView

urlpatterns = [
    path('letters/', LetterListCreateView.as_view(), name='letter-list-create'),
    path('letters/<int:pk>/', LetterDetailView.as_view(), name='letter-detail'),
]
