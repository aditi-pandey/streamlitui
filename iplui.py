import streamlit as st

# Title of the app
st.title("IPL Prediction")

# Create two columns
col1, col2, col3 = st.columns(3)

# Dropdown menu in the first column
with col1:
    options1 = ["Choose an option", "Kolkata Knight Riders", "Chennai Super Kings", "Rajasthan Royals",
                "Mumbai Indians", "Deccan Chargers", "Kings XI Punjab", "Royal Challengers Bangalore",
                "Delhi Daredevils", "Kochi Tuskers Kerala", "Pune Warriors", "Rising Pune Supergiants",
                "Delhi Capitals", "Delhi Daredevils"]
    selected_option1 = st.selectbox("Batting Team:", options1, key="batting")

# Dropdown menu in the second column
with col2:
    options2 = ["Choose an option", "Kolkata Knight Riders", "Chennai Super Kings", "Rajasthan Royals",
                "Mumbai Indians", "Deccan Chargers", "Kings XI Punjab", "Royal Challengers Bangalore",
                "Delhi Daredevils", "Kochi Tuskers Kerala", "Pune Warriors", "Rising Pune Supergiants",
                "Delhi Capitals", "Delhi Daredevils"]
    selected_option2 = st.selectbox("Bowling Team:", options2, key="bowling")

with col3:
    option3 = ["Choose an option", "Bangalore", "Chandigarh","Delhi","Mumbai","Kolkata","Jaipur","Hyderabad","Chennai","Abu Dhabi","Cape Town","Port Elizabeth","Durban","Centurion","East London","Johannesburg","Kimberley","Bloemfontein","Ahmedabad","Cuttack","Nagpur","Dharamsala","Kochi","Indore","Visakhapatnam","Pune","Raipur","Ranchi","Abu Dhabi","Rajkot","Bengaluru","Dubai","Sharjah","Navi Mumbai","Lucknow","Guwahati","Mohali"]
    selected_option3 = st.selectbox("city:",option3,key="city")


target = st.text_input("Target", key="target")
current_score = st.text_input("Current Score", key="current_score")
balls_left = st.text_input("Balls Left", key="balls_left")
wickets_out_1 = st.text_input("Wickets Out (Team 1)", key="wickets_out_1")
wickets_out_2 = st.text_input("Wickets Out (Team 2)", key="wickets_out_2")

