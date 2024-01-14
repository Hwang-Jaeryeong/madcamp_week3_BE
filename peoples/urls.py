# peoples/urls.py

from django.urls import path
from .views import PersonListCreateView, PersonDetailView

urlpatterns = [
    path('people/', PersonListCreateView.as_view(), name='person-list-create'),
    path('people/get/', PersonDetailView.as_view(), name='person-detail'),
]
