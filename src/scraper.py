import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_premier_league_table():
    """Improved scraper with better parsing"""
    print("🚀 Starting Real Web Scraper...\n")
    
    # Try Sky Sports first
    url = "https://www.skysports.com/premier-league-table"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the table
        table = soup.find('table', {'class': 'sdc-site-table'})
        
        if table:
            df = pd.read_html(str(table))[0]
            print(f"✅ Successfully scraped {len(df)} teams from Sky Sports!")
            
            # Clean column names
            df = df.rename(columns={
                'Team': 'Team',
                'P': 'Played',
                'W': 'Won',
                'D': 'Drawn',
                'L': 'Lost',
                'F': 'Goals_For',
                'A': 'Goals_Against',
                'GD': 'Goal_Difference',
                'Pts': 'Points'
            })
            return df[['Team', 'Played', 'Won', 'Drawn', 'Lost', 'Points', 'Goal_Difference']]
            
    except Exception as e:
        print(f"Sky Sports failed: {e}")
    
    print("❌ Using sample data as fallback.")
    return get_sample_data()

def get_sample_data():
    data = {
        'Team': ['Arsenal', 'Liverpool', 'Manchester City', 'Chelsea', 'Tottenham', 'Newcastle'],
        'Played': [35, 35, 35, 35, 35, 35],
        'Won': [25, 23, 22, 19, 18, 17],
        'Drawn': [6, 7, 6, 8, 7, 8],
        'Lost': [4, 5, 7, 8, 10, 10],
        'Points': [81, 76, 72, 65, 61, 59],
        'Goal_Difference': [42, 35, 28, 20, 15, 12]
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = scrape_premier_league_table()
    print("\nExtracted Table:")
    print(df)
    df.to_csv('data/premier_league_table.csv', index=False)
    print("\n💾 Saved to data/premier_league_table.csv")