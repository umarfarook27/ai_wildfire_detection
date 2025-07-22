import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import requests
from geopy.distance import geodesic
from twilio.rest import Client

# Set Streamlit page title
st.set_page_config(page_title="Wildfire Risk & Water Resources", layout="wide")

st.title("🔥 AI-Based Wildfire Risk Dashboard with Water Resources 💧")

# Twilio Credentials (Replace with your actual credentials)
TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_PHONE_NUMBER = "YOUR_TWILIO_PHONE_NUMBER"

# Function to fetch water resources from OpenStreetMap (OSM)
def get_water_resources(lat, lon, radius=5000):
    overpass_url = "https://overpass.kumi.systems/api/interpreter"  # Alternative Overpass API
    query = f"""
    [out:json];
    node
      ["natural"="water"](around:{radius},{lat},{lon});
    out body;
    """
    response = requests.get(overpass_url, params={'data': query})
    
    water_resources = []
    if response.status_code == 200:
        data = response.json()
        for element in data.get("elements", []):
            water_resources.append({
                "latitude": element["lat"],
                "longitude": element["lon"],
                "type": "Water Resource"
            })
    return water_resources

# Function to send SMS alert using Twilio
def send_sms_alert(fire_risk, location, phone_number):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message_body = f"🚨 Wildfire Alert! High fire risk detected in {location}. Risk Level: {fire_risk}. Stay Safe!"
    
    message = client.messages.create(
        body=message_body,
        from_=TWILIO_PHONE_NUMBER,
        to=phone_number
    )
    
    return message.sid

# Sample Fire Risk Data
fire_data = pd.DataFrame({
    "latitude": [34.0522, 36.7783, 40.7128, 37.7749, 39.7392],
    "longitude": [-118.2437, -119.4179, -74.0060, -122.4194, -104.9903],
    "fire_risk": ["High", "High", "Low", "High", "Medium"]
})

# User input for location & phone number (optional for SMS alerts)
st.sidebar.header("🚀 Interactive Controls")
user_lat = st.sidebar.number_input("Enter Latitude", value=34.0522)
user_lon = st.sidebar.number_input("Enter Longitude", value=-118.2437)
phone_number = st.sidebar.text_input("Enter Phone Number (for SMS Alert)", "")

if st.sidebar.button("📢 Send Alert"):
    if phone_number and fire_data[fire_data['fire_risk'] == "High"].shape[0] > 0:
        send_sms_alert("High", "User-Specified Location", phone_number)
        st.sidebar.success("✅ Alert Sent Successfully!")

# Create Map
m = folium.Map(location=[user_lat, user_lon], zoom_start=6)

# Add Fire Risk Markers
for _, row in fire_data.iterrows():
    color = "red" if row["fire_risk"] == "High" else "green"
    folium.Marker(
        [row["latitude"], row["longitude"]],
        popup=f"🔥 Fire Risk: {row['fire_risk']}",
        icon=folium.Icon(color=color),
    ).add_to(m)

    # Fetch and Add Nearby Water Resources
    water_resources = get_water_resources(row["latitude"], row["longitude"])
    for water in water_resources:
        folium.Marker(
            [water["latitude"], water["longitude"]],
            popup="💧 Water Resource",
            icon=folium.Icon(color="blue"),
        ).add_to(m)

# Display Map
st.write("🔥 **Live Fire Risk & Water Resource Map**")
st_folium(m, width=900, height=600)
