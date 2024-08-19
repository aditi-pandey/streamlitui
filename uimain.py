import streamlit as st
import numpy as np
import joblib
import time  # For dummy data update

# Try loading the models, or define dummy models if they are not available
try:
    ball_to_ball_model = joblib.load('"C:/Users/HP/Downloads/catboost_model.pkl"')

except:
    ball_to_ball_model = None  # Use None as a placeholder

try:
    win_prediction_model = joblib.load("C:/Users/HP/Downloads/scaling_encoding_02.pkl")
except:
    win_prediction_model = None  # Use None as a placeholder


# Define a dummy model class that simulates predictions
class DummyModel:
    def predict(self, X):
        # Randomly predict 0 or 1 to simulate model output
        return np.random.choice([0, 1], size=(X.shape[0],))


# Use dummy models if real models are not loaded
if ball_to_ball_model is None:
    ball_to_ball_model = DummyModel()

if win_prediction_model is None:
    win_prediction_model = DummyModel()


# Dummy scorecard data
def get_dummy_scorecard():
    return {
        "team1": "Team A",
        "team2": "Team B",
        "score1": "120/5",
        "score2": "80/3",
        "over1": "15.2",
        "over2": "12.4",
        "wickets1": 5,
        "wickets2": 3,
        "partnership1": "30 (for 6th wicket)",
        "partnership2": "25 (for 4th wicket)",
        "fall_of_wicket1": "Player X b Bowler Y, 110",
        "fall_of_wicket2": "Player Z b Bowler W, 75",
        "striker1": "Player X",
        "striker2": "Player Y",
        "bowler1": "Bowler A",
        "bowler2": "Bowler B",
        "powerplay1": "0-6",
        "powerplay2": "0-6"
    }


# Dummy fetch data function to simulate team and city data
def fetch_data():
    teams = ["Kolkata Knight Riders", "Chennai Super Kings", "Rajasthan Royals",
                "Mumbai Indians", "Deccan Chargers", "Kings XI Punjab", "Royal Challengers Bangalore",
                "Delhi Daredevils", "Kochi Tuskers Kerala", "Pune Warriors", "Rising Pune Supergiants",
                "Delhi Capitals", "Delhi Daredevils"]
    cities = ["Bangalore", "Chandigarh","Delhi","Mumbai","Kolkata","Jaipur","Hyderabad","Chennai","Abu Dhabi","Cape Town","Port Elizabeth","Durban","Centurion","East London","Johannesburg","Kimberley","Bloemfontein","Ahmedabad","Cuttack","Nagpur","Dharamsala","Kochi","Indore","Visakhapatnam","Pune","Raipur","Ranchi","Abu Dhabi","Rajkot","Bengaluru","Dubai","Sharjah","Navi Mumbai","Lucknow","Guwahati","Mohali"]
    return teams, cities


# Title of the app
st.markdown(
    "<h1 style='text-align: center;'>IPL Win Prediction and Ball-to-Ball Forecasting</h1>",
    unsafe_allow_html=True
)

# Sidebar menu for navigation
menu = st.sidebar.selectbox("Navigate",
                            ["Welcome", "Live Scorecard", "Ball-to-Ball Forecasting", "Match Win Prediction"])

# Welcome Page
if menu == "Welcome":
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Welcome to the IPL Forcasting Prediction App!</h2>
            <p>Navigate through the menu on the left to explore different features.</p>
        </div>
        """, unsafe_allow_html=True
    )

# Live Scorecard Page
elif menu == "Live Scorecard":
    st.title("Live Scorecard")
    scorecard_data = get_dummy_scorecard()  # Initial dummy data

    col1, col2 = st.columns(2)

    with col1:
        st.write(
            f"{scorecard_data['team1']}  {scorecard_data['score1']} ({scorecard_data['over1']}) - {scorecard_data['wickets1']}")
        st.write(f"Partnership: {scorecard_data['partnership1']}")
        st.write(f"Last Wicket: {scorecard_data['fall_of_wicket1']}")
        st.write(f"Striker: {scorecard_data['striker1']}")
        st.write(f"Bowler: {scorecard_data['bowler1']}")

    with col2:
        st.write(
            f"{scorecard_data['team2']}  {scorecard_data['score2']} ({scorecard_data['over2']}) - {scorecard_data['wickets2']}")
        st.write(f"Partnership: {scorecard_data['partnership2']}")
        st.write(f"Last Wicket: {scorecard_data['fall_of_wicket2']}")
        st.write(f"Striker: {scorecard_data['striker2']}")
        st.write(f"Bowler: {scorecard_data['bowler2']}")

# Ball-to-Ball Forecasting Page
elif menu == "Ball-to-Ball Forecasting":
    st.markdown("<h2 style='text-align: center;'>Ball-to-Ball Forecasting</h2>", unsafe_allow_html=True)
    teams, cities = fetch_data()

    # Dropdown menus for team and city selection
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_batting_team_b2b = st.selectbox("Batting Team:", ["Choose an option", "Kolkata Knight Riders", "Chennai Super Kings", "Rajasthan Royals",
                "Mumbai Indians", "Deccan Chargers", "Kings XI Punjab", "Royal Challengers Bangalore",
                "Delhi Daredevils", "Kochi Tuskers Kerala", "Pune Warriors", "Rising Pune Supergiants",
                "Delhi Capitals", "Delhi Daredevils"] + teams, key="batting_team_b2b")

    with col2:
        selected_bowling_team_b2b = st.selectbox("Bowling Team:", ["Choose an option","Kolkata Knight Riders", "Chennai Super Kings", "Rajasthan Royals",
                "Mumbai Indians", "Deccan Chargers", "Kings XI Punjab", "Royal Challengers Bangalore",
                "Delhi Daredevils", "Kochi Tuskers Kerala", "Pune Warriors", "Rising Pune Supergiants",
                "Delhi Capitals", "Delhi Daredevils"] + teams, key="bowling_team_b2b")

    with col3:
        selected_city_b2b = st.selectbox("City:", ["Choose an option", "Bangalore", "Chandigarh","Delhi","Mumbai","Kolkata","Jaipur","Hyderabad","Chennai","Abu Dhabi","Cape Town","Port Elizabeth","Durban","Centurion","East London","Johannesburg","Kimberley","Bloemfontein","Ahmedabad","Cuttack","Nagpur","Dharamsala","Kochi","Indore","Visakhapatnam","Pune","Raipur","Ranchi","Abu Dhabi","Rajkot","Bengaluru","Dubai","Sharjah","Navi Mumbai","Lucknow","Guwahati","Mohali"] + cities, key="city_option_b2b")

    # Input fields for ball-to-ball forecasting
    current_score_b2b = st.text_input("Current Score", key="current_score_b2b")
    balls_left_b2b = st.text_input("Balls Left", key="balls_left_b2b")
    wickets_out_b2b = st.text_input("Wickets Out", key="wickets_out_b2b")

    # Button to make ball-to-ball prediction
    if st.button("Predict Next Ball Outcome", key="predict_ball"):
        # Ensure all inputs are selected/filled
        if (selected_batting_team_b2b != "Choose an option" and
                selected_bowling_team_b2b != "Choose an option" and
                selected_city_b2b != "Choose an option" and
                current_score_b2b and balls_left_b2b and wickets_out_b2b):

            # Convert inputs to appropriate data types
            input_data_b2b = np.array([[
                int(current_score_b2b), int(balls_left_b2b), int(wickets_out_b2b)
            ]])

            # Make the ball-to-ball prediction
            ball_prediction = ball_to_ball_model.predict(input_data_b2b)[0]

            # Display the prediction
            st.subheader(f"Prediction: {'Likely a Boundary' if ball_prediction == 1 else 'Likely a Dot Ball'}")

        else:
            st.error("Please fill all the fields correctly")

# Match Win Prediction Page
elif menu == "Match Win Prediction":
    st.markdown("<h2 style='text-align: center;'>Match Win Prediction</h2>", unsafe_allow_html=True)
    teams, cities = fetch_data()

    # Dropdown menus for team and city selection
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_batting_team_win = st.selectbox("Batting Team:", ["Choose an option"],"Kolkata Knight Riders", "Chennai Super Kings", "Rajasthan Royals",
                "Mumbai Indians", "Deccan Chargers", "Kings XI Punjab", "Royal Challengers Bangalore",
                "Delhi Daredevils", "Kochi Tuskers Kerala", "Pune Warriors", "Rising Pune Supergiants",
                "Delhi Capitals", "Delhi Daredevils" , key="batting_team_win")

    with col2:
        selected_bowling_team_win = st.selectbox("Bowling Team:", ["Choose an option"],"Kolkata Knight Riders", "Chennai Super Kings", "Rajasthan Royals",
                "Mumbai Indians", "Deccan Chargers", "Kings XI Punjab", "Royal Challengers Bangalore",
                "Delhi Daredevils", "Kochi Tuskers Kerala", "Pune Warriors", "Rising Pune Supergiants",
                "Delhi Capitals", "Delhi Daredevils" , key="bowling_team_win")

    with col3:
        selected_city_win = st.selectbox("City:", ["Choose an option"], "Bangalore", "Chandigarh","Delhi","Mumbai","Kolkata","Jaipur","Hyderabad","Chennai","Abu Dhabi","Cape Town","Port Elizabeth","Durban","Centurion","East London","Johannesburg","Kimberley","Bloemfontein","Ahmedabad","Cuttack","Nagpur","Dharamsala","Kochi","Indore","Visakhapatnam","Pune","Raipur","Ranchi","Abu Dhabi","Rajkot","Bengaluru","Dubai","Sharjah","Navi Mumbai","Lucknow","Guwahati","Mohali" + cities, key="city_option_win")

    # Input fields for win prediction
    target_win = st.text_input("Target", key="target_win")
    current_score_win = st.text_input("Current Score", key="current_score_win")
    balls_left_win = st.text_input("Balls Left", key="balls_left_win")
    wickets_out_1_win = st.text_input("Wickets Out (Team 1)", key="wickets_out_1_win")
    wickets_out_2_win = st.text_input("Wickets Out (Team 2)", key="wickets_out_2_win")

    # Button to make win prediction
    if st.button("Predict Match Result", key="predict_match"):
        # Ensure all inputs are selected/filled
        if (selected_batting_team_win != "Choose an option" and
                selected_bowling_team_win != "Choose an option" and
                selected_city_win != "Choose an option" and
                target_win and current_score_win and balls_left_win and
                wickets_out_1_win and wickets_out_2_win):
            # Convert inputs to appropriate data types
            input_data_win = np.array([[
                int(target_win), int(current_score_win), int(balls_left_win),
                int(wickets_out_1_win), int(wickets_out_2_win)
            ]])

            # Make the win prediction
            win_prediction = win_prediction_model.predict(input_data_win)[0]

            # Simulate win probabilities for both teams
            team1_prob = win_prediction * 100  # Assume model output is a probability (1 for team1 win, 0 for team2 win)
            team2_prob = 100 - team1_prob

            # Display the win prediction comparison bar
            st.subheader(f"Prediction: {selected_batting_team_win} vs {selected_bowling_team_win}")

            # Show the comparison bar
            st.progress(team1_prob / 100)
            st.write(f"{selected_batting_team_win}: {team1_prob:.2f}%")
            st.write(f"{selected_bowling_team_win}: {team2_prob:.2f}%")

        else:
            st.error("Please fill all the fields correctly.")