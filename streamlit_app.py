import streamlit as st
import pandas as pd
import joblib
st.set_page_config(page_title="California Housing Prediction")
st.title("California Housing Value Prediction")
st.caption("Educational estimates of 1990 California district median home values, not current individual property valuations.")
@st.cache_resource
def load_model(): return joblib.load("housing_model.joblib")
model=load_model()
with st.form("housing"):
    longitude=st.number_input("Longitude",value=-122.23)
    latitude=st.number_input("Latitude",value=37.88)
    age=st.number_input("Housing median age (years)",min_value=0.0,value=41.0)
    rooms=st.number_input("Total rooms",min_value=0.0,value=880.0)
    bedrooms=st.number_input("Total bedrooms",min_value=0.0,value=129.0)
    population=st.number_input("Population",min_value=0.0,value=322.0)
    households=st.number_input("Households",min_value=0.0,value=126.0)
    income=st.number_input("Median income (in $10,000 units)",min_value=0.0,value=8.3252)
    ocean=st.selectbox("Ocean proximity",["NEAR BAY","<1H OCEAN","INLAND","NEAR OCEAN","ISLAND"])
    submitted=st.form_submit_button("Predict")
if submitted:
    data=pd.DataFrame([dict(longitude=longitude,latitude=latitude,housing_median_age=age,total_rooms=rooms,total_bedrooms=bedrooms,population=population,households=households,median_income=income,ocean_proximity=ocean)])
    value=float(model.predict(data)[0])
    st.metric("Predicted median district house value",f"${max(0,value):,.0f}")
    st.info("Predictions reflect historical 1990 district-level census data. Not suitable for financial decisions.")
