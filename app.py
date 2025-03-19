import streamlit as st
import geocoder
import time
import os
from PIL import Image
import pydeck as pdk
import pandas as pd

# Function to get the location based on IP
def get_location():
    g = geocoder.ip('me')  # Get approximate location from IP
    if g.latlng:
        return g.latlng[0], g.latlng[1]
    else:
        return None, None

# Main function to structure the app
def main():
    st.set_page_config(page_title="Water Leakage Reporting System", page_icon="💧", layout="wide")
    
    # Custom styling for aesthetics
    st.markdown("""
    <style>
        .report-card {
            background-color: #f0f8ff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #1e90ff;
            text-align: center;
        }
        .sub-title {
            font-size: 18px;
            color: #4682b4;
            text-align: center;
        }
        .header {
            font-size: 28px;
            color: #1e90ff;
        }
        .error {
            color: red;
        }
        .success {
            color: green;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("Water Leakage Reporting System", anchor="top")
    st.markdown('<p class="sub-title">Automatically captures location and reports water leakage incidents with an image.</p>', unsafe_allow_html=True)
    
    # Session state for report tracking
    if "report_count" not in st.session_state:
        st.session_state.report_count = 0
    
    # Max reports constraint
    if st.session_state.report_count < 3:
        # Use columns to organize layout better
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown('<p class="header">Take a Picture of the Leakage</p>', unsafe_allow_html=True)
            captured_image = st.camera_input("Take a picture of the leakage")
        
        with col2:
            st.markdown('<p class="header">Location</p>', unsafe_allow_html=True)
            # Display location info and capture button
            if st.button("Report Leakage"):
                if captured_image is None:
                    st.error("Please take a picture before reporting.")
                else:
                    with st.spinner("Getting your location..."):
                        lat, lon = get_location()
                        time.sleep(2)  # Simulate processing delay
                
                    if lat and lon:
                        st.session_state.report_count += 1
                        st.success(f"Leakage reported at Latitude: {lat}, Longitude: {lon}", icon="✅")
                        
                        # Display map using pydeck
                        map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
                        deck = pdk.Deck(
                            initial_view_state=pdk.ViewState(
                                latitude=lat,
                                longitude=lon,
                                zoom=15,
                            ),
                            layers=[pdk.Layer(
                                "ScatterplotLayer",
                                data=map_data,
                                get_position=["lon", "lat"],
                                get_color=[255, 0, 0, 160],
                                get_radius=100,
                            )]
                        )
                        st.pydeck_chart(deck)

                        # Show the captured image with some description
                        st.image(captured_image, caption="Reported Leakage", use_container_width=True)
                    else:
                        st.error("Failed to retrieve location. Please check your internet connection.", icon="⚠️")
    else:
        st.warning("Maximum of 3 reports reached. Further reports are ignored.", icon="🚫")

if __name__ == "__main__":
    main()
