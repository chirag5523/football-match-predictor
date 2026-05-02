import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()

def initialize_firestore():
    """Initialize Firestore with error handling for deployment"""
    try:
        cred_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "firebase-key.json")
        
        if not os.path.exists(cred_path):
            st.warning("⚠️ Running in demo mode (no Firestore connection)")
            return None
        
        if not firebase_admin._apps:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
        
        db = firestore.client()
        print("✅ Firestore connected")
        return db
    except Exception as e:
        print(f"Firestore not available: {e}")
        return None