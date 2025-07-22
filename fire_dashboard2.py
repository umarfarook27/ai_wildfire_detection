import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import requests

# Set page title
st.title("🔥 AI-Based Wildfire Risk Dashboard with Water Resources & Nearby Houses 💧")

# Sample Fire Risk Data (Simulated)
fire_data = pd.DataFrame({
    "latitude": [34.0522, 36.7783, 40.7128, 37.7749, 39.7392],
    "longitude": [-118.2437, -119.4179, -74.0060, -122.4194, -104.9903],
    "fire_risk": ["High", "High", "Low", "High", "Medium"]
})

# Function to fetch water resources from OpenStreetMap (OSM)
def get_water_resources(lat, lon, radius=5000):
    overpass_url = "http://overpass-api.de/api/interpreter"
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
                "longitude": element["lon"]
            })
    return water_resources

# Function to fetch nearby houses from OpenStreetMap (OSM)
def get_nearby_houses(lat, lon, radius=5000):
    overpass_url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    node
      ["building"="house"](around:{radius},{lat},{lon});
    out body;
    """
    response = requests.get(overpass_url, params={'data': query})

    houses = []
    if response.status_code == 200:
        data = response.json()
        for element in data.get("elements", []):
            houses.append({
                "latitude": element["lat"],
                "longitude": element["lon"]
            })
    return houses

# Create Map Centered on the US
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

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

    # Fetch and Add Nearby Houses
    houses = get_nearby_houses(row["latitude"], row["longitude"])
    for house in houses:
        folium.Marker(
            [house["latitude"], house["longitude"]],
            popup="🏠 House Nearby",
            icon=folium.Icon(color="gray"),
        ).add_to(m)

# Display Map
st.write("🔥 **Live Fire Risk, Houses & Water Resources Map**")
folium_static(m)
