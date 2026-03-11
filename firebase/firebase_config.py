import firebase_admin
from firebase_admin import credentials, firestore

# Load your Firebase service account key
cred = credentials.Certificate("firebase/serviceAccountKey.json")

# Initialize Firebase only once
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Firestore database client
db = firestore.client()
