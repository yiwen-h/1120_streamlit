import streamlit as st
import pandas as pd
import datetime
import requests
import plotly.express as px
'''
# TaxiFareModel front

This front queries the Le Wagon [taxi fare model API](https://taxifare.lewagon.ai/predict?pickup_datetime=2012-10-06%2012:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2)
'''

# store mapbox token in your secrets!
# Example secrets file in .streamlit folder
token = st.secrets["mapbox"]["token"]
px.set_mapbox_access_token(token)

with st.form(key='params_for_api'):

    pickup_date = st.date_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
    pickup_time = st.time_input('pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
    pickup_datetime = f'{pickup_date} {pickup_time}'
    pickup_longitude = st.number_input('pickup longitude', value=-73.9798156)
    pickup_latitude = st.number_input('pickup latitude', value=40.7614327)
    dropoff_longitude = st.number_input('dropoff longitude', value=-73.7803331)
    dropoff_latitude = st.number_input('dropoff latitude', value=40.6413111)
    passenger_count = st.number_input('passenger_count', min_value=1, max_value=8, step=1, value=1)

    submitted = st.form_submit_button('Make prediction')
    if submitted:

        params = dict(
            pickup_datetime=pickup_datetime,
            pickup_longitude=pickup_longitude,
            pickup_latitude=pickup_latitude,
            dropoff_longitude=dropoff_longitude,
            dropoff_latitude=dropoff_latitude,
            passenger_count=passenger_count)

        wagon_cab_api_url = 'https://taxifare.lewagon.ai/predict'
        response = requests.get(wagon_cab_api_url, params=params)

        prediction = response.json()

        pred = prediction['fare']
        st.header(f'Fare amount: ${round(pred, 2)}')

        map_df = pd.DataFrame({'lat': [pickup_latitude, dropoff_latitude],
                               'lon': [pickup_longitude, dropoff_longitude]})
        # st.map(map_df)


        fig = px.scatter_mapbox(map_df, lat="lat", lon="lon",zoom=10)
        fig.update_traces(marker=dict(color="RoyalBlue", size=10))
        fig.update_layout(mapbox_style='basic')
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig)
