from django.urls import path
from .views import TestFirestore

urlpatterns = [
    path("test-firestore/", TestFirestore.as_view()),
]
