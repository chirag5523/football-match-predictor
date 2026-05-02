from scraper import get_sample_data
from firestore_utils import initialize_firestore
import datetime

def save_to_firestore():
    db = initialize_firestore()
    if not db:
        return
    
    # Get data
    df = get_sample_data()
    
    # Save Teams collection
    teams_ref = db.collection('teams')
    
    for _, row in df.iterrows():
        team_data = {
            'team_name': row['Team'],
            'position': int(row['Position']),
            'points': int(row['Points']),
            'played': int(row['Played']),
            'won': int(row['Won']),
            'drawn': int(row['Drawn']),
            'lost': int(row['Lost']),
            'goal_difference': int(row['Goal_Difference']),
            'last_updated': datetime.datetime.now()
        }
        # Add or update
        teams_ref.document(row['Team']).set(team_data)
    
    print("✅ Data successfully saved to Firestore!")
    print(f"   Saved {len(df)} teams")

# Run pipeline
if __name__ == "__main__":
    print("🚀 Running Data Pipeline...\n")
    save_to_firestore()