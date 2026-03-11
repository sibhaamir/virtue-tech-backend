import firebase_admin
from firebase_admin import auth as firebase_auth, credentials
from rest_framework import authentication, exceptions
from .models import User
import os
import json

# Safe Firebase initialization
if not firebase_admin._apps:
    firebase_key = os.environ.get("FIREBASE_KEY")

    if firebase_key:
        try:
            cred_dict = json.loads(firebase_key)
            cred = credentials.Certificate(cred_dict)
            firebase_admin.initialize_app(cred)
        except Exception as e:
            print("Firebase initialization failed:", e)
    else:
        print("WARNING: FIREBASE_KEY environment variable not set")