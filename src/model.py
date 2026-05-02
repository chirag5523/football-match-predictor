import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Sample training data (you can expand this later)
def create_and_train_model():
    # Sample historical match data
    data = {
        'home_xg': [2.1, 1.8, 2.5, 1.4, 2.8, 1.9],
        'away_xg': [1.2, 1.5, 0.9, 2.1, 1.3, 1.7],
        'home_form': [8, 6, 9, 5, 7, 8],      # last 5 games points
        'away_form': [7, 8, 4, 6, 5, 7],
        'home_advantage': [1, 1, 1, 0, 1, 1],
        'xg_diff': [0.9, 0.3, 1.6, -0.7, 1.5, 0.2],
        'result': [1, 0, 1, 2, 1, 1]           # 1=Home Win, 0=Draw, 2=Away Win
    }
    
    df = pd.DataFrame(data)
    
    X = df.drop('result', axis=1)
    y = df['result']
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    # Save model
    joblib.dump(model, 'models/football_predictor.pkl')
    print("✅ ML Model trained and saved!")
    return model

# Load or train model
def get_model():
    model_path = 'models/football_predictor.pkl'
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        return create_and_train_model()

def predict_match(home_team, away_team):
    model = get_model()
    
    # Dummy features (in real project, fetch from Firestore)
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
    result = outcomes[prediction]
    
    return {
        'result': result,
        'home_win_prob': round(probabilities[1]*100, 1),
        'draw_prob': round(probabilities[0]*100, 1),
        'away_win_prob': round(probabilities[2]*100, 1),
        'predicted_score': "3 - 1" if home_team == "Arsenal" else "1 - 2"
    }