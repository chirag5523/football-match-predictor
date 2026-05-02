import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier

def create_and_train_model():
    """Train a simple model"""
    print("Training new ML model...")
    
    # Sample training data
    data = {
        'home_xg': [2.1, 1.8, 2.5, 1.4, 2.8, 1.9, 2.3],
        'away_xg': [1.2, 1.5, 0.9, 2.1, 1.3, 1.7, 1.1],
        'home_form': [8, 6, 9, 5, 7, 8, 7],
        'away_form': [7, 8, 4, 6, 5, 7, 6],
        'home_advantage': [1, 1, 1, 0, 1, 1, 1],
        'xg_diff': [0.9, 0.3, 1.6, -0.7, 1.5, 0.2, 1.2],
        'result': [1, 0, 1, 2, 1, 1, 1]
    }
    
    df = pd.DataFrame(data)
    X = df.drop('result', axis=1)
    y = df['result']
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    # Ensure models folder exists
    os.makedirs('models', exist_ok=True)
    
    joblib.dump(model, 'models/football_predictor.pkl')
    print("✅ Model trained and saved!")
    return model

def get_model():
    """Load or create model"""
    model_path = 'models/football_predictor.pkl'
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        return create_and_train_model()

def predict_match(home_team, away_team):
    model = get_model()
    
    features = {
        'home_xg': 2.4 if home_team == "Arsenal" else 1.8,
        'away_xg': 1.3 if away_team == "Arsenal" else 1.6,
        'home_form': 8 if home_team == "Arsenal" else 6,
        'away_form': 6 if away_team == "Arsenal" else 7,
        'home_advantage': 1,
        'xg_diff': 1.1 if home_team == "Arsenal" else -0.5
    }
    
    input_df = pd.DataFrame([features])
    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]
    
    outcomes = {0: "Draw", 1: "Home Win", 2: "Away Win"}
    
    return {
        'result': outcomes[prediction],
        'home_win_prob': round(probabilities[1]*100, 1),
        'draw_prob': round(probabilities[0]*100, 1),
        'away_win_prob': round(probabilities[2]*100, 1),
        'predicted_score': "3 - 1" if home_team == "Arsenal" else "1 - 2"
    }