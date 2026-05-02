import streamlit as st
import pandas as pd
import plotly.express as px
from model import predict_match

# Try to import Firestore (will fail gracefully on deployment)
try:
    from firestore_utils import initialize_firestore
    db = initialize_firestore()
except:
    db = None

st.set_page_config(
    page_title="Arsenal FC Predictor",
    page_icon="🔴",
    layout="wide"
)

# Arsenal Theme
st.markdown("""
<style>
    .main {background-color: #f8f8f8;}
    h1, h2, h3 {color: #EF0000 !important;}
    .stButton>button {background-color: #EF0000; color: white;}
    .stButton>button:hover {background-color: #cc0000;}
</style>
""", unsafe_allow_html=True)

st.image("https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg", width=180)
st.title("Arsenal FC Match Predictor")
st.markdown("**Come On You Gunners!** 💪🔴")

st.sidebar.header("🔴 Arsenal Navigation")
page = st.sidebar.radio("Go to", ["League Table", "Player Stats", "Match Predictor", "Arsenal Focus"])

if page == "League Table":
    st.header("Current Premier League Table")
    
    if db:
        teams_ref = db.collection('teams')
        teams = [doc.to_dict() for doc in teams_ref.stream()]
        if teams:
            df = pd.DataFrame(teams).sort_values('position')
        else:
            df = get_sample_table()
    else:
        df = get_sample_table()
    
    # Points Chart
    fig = px.bar(df, x='Team', y='Points', title="Premier League Points", 
                 color='Points', color_continuous_scale='Reds')
    st.plotly_chart(fig, use_container_width=True)
    
    # Table
    def highlight_arsenal(row):
        return ['background-color: #EF0000; color: white' if row['Team'] == 'Arsenal' else ''] * len(row)
    
    styled_df = df.style.apply(highlight_arsenal, axis=1)
    st.dataframe(styled_df, use_container_width=True, hide_index=True)

elif page == "Player Stats":
    st.header("🔴 Key Arsenal Player Stats")
    players = {
        "Player": ["Bukayo Saka", "Martin Ødegaard", "Gabriel Jesus", "Declan Rice", "William Saliba"],
        "Goals": [15, 8, 12, 3, 2],
        "Assists": [10, 12, 5, 4, 1],
        "Rating": [8.5, 8.7, 8.2, 8.0, 8.4]
    }
    df_players = pd.DataFrame(players)
    
    col1, col2 = st.columns(2)
    with col1: st.dataframe(df_players, use_container_width=True)
    with col2:
        fig = px.bar(df_players, x="Player", y=["Goals", "Assists"], barmode='group')
        st.plotly_chart(fig, use_container_width=True)

elif page == "Match Predictor":
    st.header("🔮 Realistic ML Match Predictor")
    
    col1, col2 = st.columns(2)
    with col1:
        home_team = st.selectbox("Home Team", ["Arsenal", "Liverpool", "Manchester City"], index=0)
    with col2:
        away_team = st.selectbox("Away Team", ["Tottenham", "Manchester United", "Newcastle"])
    
    if st.button("🔴 Predict Match", type="primary"):
        with st.spinner("Analyzing match..."):
            result = predict_match(home_team, away_team)
        
        st.balloons()
        st.success(f"**{home_team} vs {away_team}** → **{result['result']}**")
        
        colA, colB, colC = st.columns(3)
        with colA: st.metric("Home Win", f"{result['home_win_prob']}%")
        with colB: st.metric("Draw", f"{result['draw_prob']}%")
        with colC: st.metric("Away Win", f"{result['away_win_prob']}%")
        
        st.info(f"**Predicted Score:** {result['predicted_score']}")

elif page == "Arsenal Focus":
    st.header("🔴 Arsenal Season Insights")
    st.success("**1st Place** | Form: W W D W W")
    fig = px.line(x=[1,2,3,4,5,6], y=[2.1,2.8,1.9,3.2,2.5,2.7], 
                  title="Arsenal xG Trend", markers=True)
    fig.update_traces(line_color='#EF0000')
    st.plotly_chart(fig, use_container_width=True)

# Helper Function
def get_sample_table():
    data = {
        'Team': ['Arsenal', 'Liverpool', 'Manchester City', 'Chelsea', 'Tottenham'],
        'Played': [35,35,35,35,35],
        'Won': [25,23,22,19,18],
        'Drawn': [6,7,6,8,7],
        'Lost': [4,5,7,8,10],
        'Points': [81,76,72,65,61],
        'Goal_Difference': [42,35,28,20,15]
    }
    return pd.DataFrame(data)

# Footer
st.markdown("---")
st.markdown("""
    <p style="color: #1f1f1f; font-size: 15px; text-align: center;">
        🔴 Arsenal FC Match Predictor | Built with ❤️ for The Gunners
    </p>
""", unsafe_allow_html=True)