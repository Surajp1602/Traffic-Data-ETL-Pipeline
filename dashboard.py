import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

st.title("Traffic Analytics Dashboard")

engine = create_engine("sqlite:///traffic.db")

df = pd.read_sql("SELECT * FROM traffic_data", engine)

st.subheader("Traffic Dataset")
st.dataframe(df)

st.subheader("Vehicle Count by Location")

location_summary = (
    df.groupby("location")["vehicle_count"]
    .mean()
    .reset_index()
)

st.bar_chart(
    location_summary.set_index("location")
)

st.subheader("Average Speed by Location")

speed_summary = (
    df.groupby("location")["avg_speed"]
    .mean()
    .reset_index()
)

st.bar_chart(
    speed_summary.set_index("location")
)

st.subheader("Traffic Level Distribution")

traffic_counts = (
    df["traffic_level"]
    .value_counts()
)

st.bar_chart(traffic_counts)

st.subheader("Hourly Traffic Trend")

hourly = (
    df.groupby("hour")["vehicle_count"]
    .mean()
)

st.line_chart(hourly)