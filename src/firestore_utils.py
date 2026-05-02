import os
import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st

def initialize_firestore():
    """Initialize Firestore using Streamlit Secrets or local key"""
    try:
        # For Streamlit Cloud (using Secrets)
        if "firebase" in st.secrets:
            firebase_config = st.secrets["firebase"]
            
            # Create credential from secrets
            cred_dict = {
                "type": firebase_config["type"],
                "project_id": firebase_config["project_id"],
                "private_key_id": firebase_config["private_key_id"],
                "private_key": firebase_config["private_key"],
                "client_email": firebase_config["client_email"],
                "client_id": firebase_config["client_id"],
                "auth_uri": firebase_config["auth_uri"],
                "token_uri": firebase_config["token_uri"]
            }
            
            cred = credentials.Certificate(cred_dict)
            
        else:
            # For local development
            cred_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "firebase-key.json")
            if not os.path.exists(cred_path):
                st.warning("⚠️ Firestore not connected - Running in Demo Mode")
                return None
            cred = credentials.Certificate(cred_path)
        
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        
        db = firestore.client()
        # st.success("✅ Firestore connected")
        return db
        
    except Exception as e:
        st.warning("⚠️ Firestore not available (Demo Mode)")
        return None