import firebase_admin
from firebase_admin import auth as firebase_auth, credentials
from rest_framework import authentication, exceptions
from .models import User
import os
import json

if not firebase_admin._apps:
    firebase_key = os.getenv("FIREBASE_KEY")

    if firebase_key:
        cred_dict = json.loads(firebase_key)
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)
    else:
        print("WARNING: FIREBASE_KEY not set")