import pandas as pd

def get_current_table():
    """Return current Premier League table (sample for now)"""
    print("📊 Loading Premier League Table (Demo Mode)")
    
    data = {
        'Team': ['Arsenal', 'Liverpool', 'Manchester City', 'Chelsea', 'Tottenham', 'Newcastle', 'Aston Villa'],
        'Played': [35, 35, 35, 35, 35, 35, 35],
        'Won': [25, 23, 22, 19, 18, 17, 16],
        'Drawn': [6, 7, 6, 8, 7, 8, 7],
        'Lost': [4, 5, 7, 8, 10, 10, 12],
        'Points': [81, 76, 72, 65, 61, 59, 55],
        'Goal_Difference': [42, 35, 28, 20, 15, 12, 8]
    }
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = get_current_table()
    print(df)
    df.to_csv('data/premier_league_table.csv', index=False)