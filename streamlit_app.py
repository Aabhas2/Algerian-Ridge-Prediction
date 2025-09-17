import numpy as np
import pandas as pd
import pickle as pkl
import streamlit as st

# Import pickle files: Ridge regressor and standard scaler
ridge_model = pkl.load(open("models/ridge.pkl", "rb"))
standard_scaler = pkl.load(open("models/scaler.pkl", "rb"))

def main():
    st.title("Forest Fire Weather Index (FWI) Prediction")
    
    # Create input fields
    temperature = st.number_input("Temperature", value=0.0)
    rh = st.number_input("RH (Relative Humidity)", value=0.0)
    ws = st.number_input("Ws (Wind Speed)", value=0.0)
    rain = st.number_input("Rain", value=0.0)
    ffmc = st.number_input("FFMC (Fine Fuel Moisture Code)", value=0.0)
    dmc = st.number_input("DMC (Duff Moisture Code)", value=0.0)
    isi = st.number_input("ISI (Initial Spread Index)", value=0.0)
    classes = st.number_input("Classes", value=0.0)
    region = st.number_input("Region", value=0.0)
    
    # Create a prediction button
    if st.button("Predict FWI"):
        # Make prediction
        new_data_scaled = standard_scaler.transform([[temperature, rh, ws, rain, ffmc, dmc, isi, classes, region]])
        result = ridge_model.predict(new_data_scaled)
        
        # Display the result
        st.success(f"The predicted FWI is: {result[0]*100:.2f}%")
        
        # Add some context about the prediction
        st.info("Note: FWI (Fire Weather Index) is an indicator of fire intensity. Higher values indicate more severe fire weather conditions.")

if __name__ == "__main__":
    main()