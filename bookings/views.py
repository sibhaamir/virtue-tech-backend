from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from firebase.firebase_config import db

class TestFirestore(APIView):
    def get(self, request):
        db.collection("test_collection").add({"message": "Hello from Django & Firestore!"})
        return Response({"status": "Firestore connected!"})
