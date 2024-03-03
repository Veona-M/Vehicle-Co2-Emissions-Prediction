import pandas as pd
import streamlit as st
import pickle
import numpy as np

file_path = 'knn_model.pickle'
with open(file_path, 'rb') as file:
    knn_model = pickle.load(file)

le_file_path = 'le_encoder.pickle'
with open(le_file_path, 'rb') as file:
    le_encoder = pickle.load(file)

st.set_page_config(page_title='Vehicle CO2 Emissions Prediction App',
                   page_icon='🚗',
                   layout='wide',
                   initial_sidebar_state='expanded')

st.header("CO2 Emissions Prediction")
st.write("This app uses the data you enter to calculate the amount of carbon dioxide that the specified vehicle "
         "produces.")


def predict_emission(transmission, fuel_type, engine_size_l, cylinders, fuel_consumption_comb):
    input_data = np.array([[transmission, fuel_type, engine_size_l, cylinders, fuel_consumption_comb]]).astype(
        np.float64)
    prediction = knn_model.predict(input_data)
    return prediction


with st.form(key='User Input'):
    st.subheader('User Input')
    transmission = st.selectbox("Please select vehicle Type of transmission : 0 for Automated Manual/ 1 for Automatic/ "
                                "2 for Automatic with Select Shift / 3 for Continuously Variable/ 4 for Manual",
                                [0, 1, 2, 3, 4])
    fuel_type = st.selectbox("Please select the fuel type : 0 for Diesel / 1 for Ethanol / 2 for Natural gas/"
                             " 3 for Premium Gasoline/ 4 for Regular Gasoline", [0, 1, 2, 3, 4])
    engine_size_l = st.number_input("Enter the vehicle's engine size in Litres", min_value=1.0, step=0.1)
    cylinders = st.number_input("Enter the number of cylinders in the engine?", min_value=1, step=1)
    fuel_consumption_comb = st.number_input("Enter the fuel consumption in L/100km", min_value=0.01)

    submitted = st.form_submit_button("Predict")
    if submitted:
        user_data = pd.DataFrame({
            'transmission': [transmission],
            'fuel_type': [fuel_type],
            'engine_size_l': [engine_size_l],
            'cylinders': [cylinders],
            'fuel_consumption_comb': [fuel_consumption_comb],

        })

        prediction_result = predict_emission(transmission, fuel_type, engine_size_l, cylinders, fuel_consumption_comb)
        st.write("Prediction Result (grams/km) :", prediction_result)





