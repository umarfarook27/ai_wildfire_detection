# 🔥 AI-Based Wildfire Detection & Prevention System

An intelligent solution to detect and prevent wildfires using AI, IoT, and geospatial data visualization. This project uses machine learning to predict high fire risk zones based on environmental data and displays the results on an interactive dashboard, including nearby water resources and residential areas.

---

## 📌 Description

Wildfires are becoming more frequent and destructive due to climate change and human activity. Delayed response and lack of real-time data contribute to the scale of damage.  
This project uses an **AI-powered model** to predict wildfire risk and visualize it along with **nearby water sources** and **homes around fire zones** on a live interactive map.

---

## ✅ Features

- 🔍 Predicts wildfire risk based on real-world environmental features  
- 📊 Displays **high**, **low**, and **medium** fire risk zones  
- 💧 Shows **water resources** using OpenStreetMap Overpass API  
- 🏡 Marks **houses near fire-prone areas** for early response  
- 🗺️ Fully interactive map with zoom and details  
- ⚡ Built with **Streamlit** for rapid and intuitive web dashboard

---

## 🧠 Technologies Used

- **Python**
- **Pandas** – data processing  
- **Scikit-learn** – machine learning model  
- **Streamlit** – interactive web dashboard  
- **Folium** – map generation and markers  
- **Geopy** – distance calculation  
- **Overpass API** – fetch water body data  
- *(Twilio alerting skipped due to deployment limitations)*

---

## 🧪 AI Model Summary

- Algorithm: `RandomForestClassifier`  
- Features: `temperature`, `humidity`, `wind_speed`, `vegetation_dryness`  
- Target: `fire_risk` (0 = Low, 1 = High)  
- Dataset: `sample_wildfire_data.csv`  

---
