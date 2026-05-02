import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()

def initialize_firestore():
    try:
        cred_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "firebase-key.json")
        
        if not firebase_admin._apps:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
        
        db = firestore.client()
        print("✅ Firestore initialized successfully!")
        return db
    except Exception as e:
        print(f"❌ Firestore Error: {e}")
        return None