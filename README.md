# ⚽ Football Match Predictor

A complete **Premier League Match Predictor** with web scraping, Firestore database, Machine Learning, and Streamlit dashboard.

## Features
- Automated data scraping from FBref
- Cloud Firestore as Data Warehouse
- Machine Learning predictions (Win/Draw/Loss probabilities)
- Interactive Streamlit Dashboard
- Optional Arsenal-friendly theme & banter mode

## Tech Stack
- **Python** • Pandas • Scikit-learn
- **Firebase Firestore**
- **Streamlit** (Dashboard)
- **BeautifulSoup + requests** (Scraping)

## Project Structure
football-match-predictor/
├── data/               # Raw & processed data
├── notebooks/          # Jupyter notebooks for analysis
├── src/
│   ├── scraper.py
│   ├── firestore_utils.py
│   ├── features.py
│   ├── model.py
│   └── dashboard.py
├── models/             # Saved ML models
├── config/
├── requirements.txt
├── README.md
└── run_scraper.py


## Setup Instructions
1. Clone or download this repo
2. `pip install -r requirements.txt`
3. Setup Firebase Firestore (see below)
4. Run `streamlit run src/dashboard.py`

## Future Plans
- Add Arsenal special highlights
- Player impact metrics
- Shot maps