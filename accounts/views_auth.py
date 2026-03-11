from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firebase.firebase_config import db
from rest_framework_simplejwt.tokens import RefreshToken
import uuid

class Signup(APIView):
    def post(self, request):
        data = request.data
        uid = str(uuid.uuid4())

        user_data = {
            "uid": uid,
            "name": data.get("name"),
            "email": data.get("email"),
            "role": data.get("role"),  # student / tutor
            "created_at": firestore.SERVER_TIMESTAMP
        }

        db.collection("users").document(uid).set(user_data)

        return Response({"message": "User registered successfully", "uid": uid}, status=201)


class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        role = request.data.get("role")

        # Query user by email + role
        users = db.collection("users").where("email", "==", email).where("role", "==", role).stream()

        user = None
        for u in users:
            user = u.to_dict()

        if not user:
            return Response({"error": "Invalid credentials"}, status=400)

        refresh = RefreshToken.for_user(type("obj", (object,), {"id": user['uid']}))

        return Response({
            "message": "Login successful",
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": user
        })
