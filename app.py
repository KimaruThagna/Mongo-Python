import streamlit as st
from db_config import salary_collection
from pymongo import DESCENDING,ASCENDING

st.header('Data analytics using Mongodb and Python')
st.subheader('Analyzing salary Data for professors and Associate professors')
display_data = st.checkbox('Display raw dataset')