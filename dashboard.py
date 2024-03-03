import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
import streamlit as st
import os

st.set_page_config(
    page_title='Co2 Emissions Prediction ',
    layout='centered',
    initial_sidebar_state='expanded',
)


@st.cache_data
def load_data(your_data):
    dataframe = pd.read_csv(your_data)
    return dataframe


file_path = os.path.dirname(__file__)
file_path = os.path.join(file_path, './CO2 Emissions_Canada.csv')

# Sidebar
st.sidebar.header('CO2 Data')
data = st.sidebar.file_uploader('Upload your Dataset', type=['csv', 'txt', 'xls'])
if data is not None:
    df = load_data(data)
else:
    df = load_data(file_path)

menu = ['Transmission', 'Fuel Type', 'Engine Size', 'Cylinders', 'Fuel Consumption']
selection = st.sidebar.selectbox('Features', menu)

# Renaming columns for better reference
df = df.rename(
    columns={'Make': 'make', 'Model': 'model', 'Vehicle Class': 'vehicle_class', 'Engine Size(L)': 'engine_size_l',
             'Cylinders': 'cylinders', 'Transmission': 'transmission', 'Fuel Type': 'fuel_type',
             'Fuel Consumption City (L/100 km)': 'fuel_consumption_city(L/100km)',
             'Fuel Consumption Hwy (L/100 km)': 'fuel_consumption_hwy(L/100km)',
             'Fuel Consumption Comb (L/100 km)': 'fuel_consumption_comb',
             'Fuel Consumption Comb (mpg)': 'fuel_consumption_comb(mpg)', 'CO2 Emissions(g/km)': 'co2_emissions(g/km)'})

# Mapping similar labels

df['transmission'] = np.where(df['transmission'].isin(['AS5', 'AS6', 'AS8', 'AS9', 'AS4', 'AS10', 'AS7']),
                              'Automatic With Select Shift', df['transmission'])
df['transmission'] = np.where(df['transmission'].isin(['M6', 'M7', 'M5']), 'Manual',
                              df['transmission'])
df['transmission'] = np.where(df['transmission'].isin(['AV7', 'AV8', 'AV', 'AV6', 'AV10']),
                              'Continuously Variable', df['transmission'])
df['transmission'] = np.where(df['transmission'].isin(['A6', 'A7', 'A8', 'A4', 'A5', 'A9', 'A10']),
                              'Automatic', df['transmission'])
df['transmission'] = np.where(df['transmission'].isin(['AM7', 'AM5', 'AM8', 'AM9', 'AM6']),
                              'Automated Manual', df['transmission'])

df['fuel_type'] = np.where(df['fuel_type'] == 'Z', 'Premium Gasoline', df['fuel_type'])
df['fuel_type'] = np.where(df['fuel_type'] == 'D', 'Diesel', df['fuel_type'])
df['fuel_type'] = np.where(df['fuel_type'] == 'X', 'Regular Gasoline', df['fuel_type'])
df['fuel_type'] = np.where(df['fuel_type'] == 'E', 'Ethanol(E85)', df['fuel_type'])
df['fuel_type'] = np.where(df['fuel_type'] == 'N', 'Natural Gas', df['fuel_type'])

# First page
if selection == 'Transmission':
    st.header('Co2 Emissions Dashboard')
    st.write('Analyzes how different vehicle features contribute to Co2 Emissions.')
    st.dataframe(df.head(10))
    # plot1
    st.subheader('Frequency distribution of the Type of Vehicle Transmission')
    fig = px.histogram(df, x='transmission', color='transmission')
    fig.update_layout(
        xaxis_title='Type of Transmission',
        xaxis={'categoryorder': 'total descending'},
        width=1000
    )
    st.plotly_chart(fig, use_container_width=True)

    # plot 2
    st.subheader('Average Co2 Emissions per Type of Transmission')
    co2_vs_transmission = df.groupby('transmission')['co2_emissions(g/km)'].mean().reset_index()
    fig = px.bar(co2_vs_transmission, x='transmission', y='co2_emissions(g/km)', color='transmission')
    fig.update_layout(
        xaxis_title='Type of Transmission',
        yaxis_title='Co2 Emissions(g/km)',
        xaxis={'categoryorder': 'total descending'}
    )
    st.plotly_chart(fig, use_container_width=True)


if selection == 'Fuel Type':
    st.header('Co2 Emissions Dashboard')
    st.write('Analyzes how different vehicle features contribute to Co2 Emissions.')
    st.dataframe(df.head(10))

    # plot1
    st.subheader('Frequency distribution of the Fuel Type')
    fig = px.histogram(df, x='fuel_type', color='fuel_type')
    fig.update_layout(
        xaxis_title='Fuel Type',
        xaxis={'categoryorder': 'total descending'},
        width=1000
    )
    st.plotly_chart(fig, use_container_width=True)

    # plot2
    st.subheader('Average Co2 Emissions per Fuel Type')
    co2_vs_fuel = df.groupby('fuel_type')['co2_emissions(g/km)'].mean().reset_index()
    fig = px.bar(co2_vs_fuel, x='fuel_type', y='co2_emissions(g/km)', color='fuel_type')
    fig.update_layout(
        xaxis_title='Fuel Type',
        yaxis_title='Co2 Emissions(g/km)',
        xaxis={'categoryorder': 'total descending'}
    )
    st.plotly_chart(fig, use_container_width=True)


if selection == 'Engine Size':
    st.header('Co2 Emissions Dashboard')
    st.write('Analyzes how different vehicle features contribute to Co2 Emissions.')
    st.dataframe(df.head(10))

    # plot1
    st.subheader('Distribution of Vehicle Engine Size in Litres')
    fig = px.histogram(df, x='engine_size_l')
    fig.update_layout(
        xaxis_title='Engine Size (L)'
    )
    st.plotly_chart(fig, use_container_width=True)

    # plot2
    st.subheader('Relationship between Engine Size and CO2 Emissions')
    fig = sns.lmplot(
        data=df,
        x='engine_size_l',
        y='co2_emissions(g/km)',
        markers='.'
    )
    plt.xlabel('Engine Size (L)')
    plt.ylabel('CO2 Emissions(g/km)')
    plt.figure(figsize=(1, 2))
    sns.set_style('darkgrid')
    st.pyplot(fig)


if selection == 'Cylinders':
    st.header('Co2 Emissions Dashboard')
    st.write('Analyzes how different vehicle features contribute to Co2 Emissions.')
    st.dataframe(df.head(10))

    # plot1
    st.subheader('Distribution of Number of cylinders in a vehicle engine')
    fig = px.histogram(df, x='cylinders')
    fig.update_layout(
        xaxis_title='No. of Cylinders'
    )
    st.plotly_chart(fig, use_container_width=True)

    # plot2
    st.subheader('Relationship between No. of Cylinders and CO2 Emissions')
    fig = sns.lmplot(
        data=df,
        x='cylinders',
        y='co2_emissions(g/km)',
        markers='.'
    )
    plt.xlabel('No. of Cylinders')
    plt.ylabel('CO2 Emissions(g/km)')
    sns.set_style('darkgrid')
    st.pyplot(fig)

if selection == 'Fuel Consumption':
    st.header('Co2 Emissions Dashboard')
    st.write('Analyzes how different vehicle features contribute to Co2 Emissions.')
    st.dataframe(df.head(10))

    # plot1
    st.subheader('Distribution of Vehicle Fuel consumption')
    fig = px.histogram(df, x='fuel_consumption_comb')
    fig.update_layout(
        xaxis_title='Fuel Consumption (L/100km)'
    )
    st.plotly_chart(fig)

    # plot2
    st.subheader('Relationship between Fuel consumption and CO2 Emissions')
    fig = sns.lmplot(
        data=df,
        x='fuel_consumption_comb',
        y='co2_emissions(g/km)'
    )
    plt.xlabel('Fuel consumption comb(L/100km)')
    plt.ylabel('CO2 Emissions(g/km)')
    sns.set_style('darkgrid')
    st.pyplot(fig)
