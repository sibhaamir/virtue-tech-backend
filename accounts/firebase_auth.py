import firebase_admin
from firebase_admin import auth as firebase_auth, credentials
from rest_framework import authentication, exceptions
from .models import User
import os
import json

# Initialize Firebase Admin using ENV variable
if not firebase_admin._apps:
    firebase_key = os.environ.get("FIREBASE_KEY")

    if not firebase_key:
        raise Exception("FIREBASE_KEY environment variable not set")

    cred_dict = json.loads(firebase_key)
    cred = credentials.Certificate(cred_dict)

    firebase_admin.initialize_app(cred)


class FirebaseAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_header = authentication.get_authorization_header(request).split()

        if not auth_header or auth_header[0].lower() != b"bearer":
            return None

        token = auth_header[1].decode("utf-8")

        try:
            decoded_token = firebase_auth.verify_id_token(token)
        except Exception:
            raise exceptions.AuthenticationFailed("Invalid Firebase ID token")

        uid = decoded_token["uid"]
        email = decoded_token.get("email")
        name = decoded_token.get("name", "")

        user, created = User.objects.get_or_create(
            firebase_uid=uid,
            defaults={
                "username": email.split("@")[0] if email else uid,
                "email": email,
                "first_name": name.split(" ")[0] if name else "",
                "last_name": " ".join(name.split(" ")[1:]) if name else "",
            },
        )

        return (user, None)