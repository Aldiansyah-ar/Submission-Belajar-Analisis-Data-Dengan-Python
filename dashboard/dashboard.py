import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

sns.set(style='dark')

#Load cleaned data
data_df = pd.read_csv("../data/aotizhongxin.csv")

data_df.reset_index(inplace=True)
data_df["date"] = pd.to_datetime(data_df["date"])

#Membuat filter rentang waktu
min_date = data_df["date"].min()
max_date = data_df["date"].max()

with st.sidebar:
    #Mengambil start date dan end_date
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date, max_value=max_date, value=[min_date, max_date] 
    )

#Menyiapkan aotizhongxin_df dalam rentang waktu
filtered_df = data_df[(data_df["date"] >= str(start_date)) & (data_df["date"] <= str(end_date))]
aotizhongxin_df = filtered_df

#Dashboard kadar PM2.5 di kota Aotizhongxin
st.header('Kadar Gas di Kota Aotizhongxin')
st.subheader('Kadar PM2.5')

col1, col2, col3 = st.columns(3)

with col1:
    PM25_max = aotizhongxin_df['PM2.5'].max().round(2)
    st.metric("Maximum PM2.5", value=PM25_max)

with col2:
    PM25_mean = aotizhongxin_df['PM2.5'].mean().round(2)
    st.metric("Average PM2.5", value=PM25_mean)

with col3:
    PM25_min = aotizhongxin_df['PM2.5'].min().round(2)
    st.metric("Minimum PM2.5", value=PM25_min)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    aotizhongxin_df["date"],
    aotizhongxin_df["PM2.5"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)

ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)

#Dashboard kadar PM10 di kota Aotizhongxin
st.subheader('Kadar PM10')

col1, col2, col3 = st.columns(3)

with col1:
    PM25_max = aotizhongxin_df['PM10'].max().round(2)
    st.metric("Maximum PM10", value=PM25_max)

with col2:
    PM25_mean = aotizhongxin_df['PM10'].mean().round(2)
    st.metric("Average PM10", value=PM25_mean)

with col3:
    PM25_min = aotizhongxin_df['PM10'].min().round(2)
    st.metric("Minimum PM10", value=PM25_min)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    aotizhongxin_df["date"],
    aotizhongxin_df["PM10"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)

ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)

#Dashboard kadar SO2 di kota Aotizhongxin
st.subheader('Kadar SO2')

col1, col2, col3 = st.columns(3)

with col1:
    PM25_max = aotizhongxin_df['SO2'].max().round(2)
    st.metric("Maximum SO2", value=PM25_max)

with col2:
    PM25_mean = aotizhongxin_df['SO2'].mean().round(2)
    st.metric("Average SO2", value=PM25_mean)

with col3:
    PM25_min = aotizhongxin_df['SO2'].min().round(2)
    st.metric("Minimum SO2", value=PM25_min)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    aotizhongxin_df["date"],
    aotizhongxin_df["SO2"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)

ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)

#Dashboard kadar NO2 di kota Aotizhongxin
st.subheader('Kadar NO2')

col1, col2, col3 = st.columns(3)

with col1:
    PM25_max = aotizhongxin_df['NO2'].max().round(2)
    st.metric("Maximum NO2", value=PM25_max)

with col2:
    PM25_mean = aotizhongxin_df['NO2'].mean().round(2)
    st.metric("Average NO2", value=PM25_mean)

with col3:
    PM25_min = aotizhongxin_df['NO2'].min().round(2)
    st.metric("Minimum NO2", value=PM25_min)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    aotizhongxin_df["date"],
    aotizhongxin_df["NO2"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)

ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)

#Dashboard kadar CO di kota Aotizhongxin
st.subheader('Kadar CO')

col1, col2, col3 = st.columns(3)

with col1:
    PM25_max = aotizhongxin_df['CO'].max().round(2)
    st.metric("Maximum CO", value=PM25_max)

with col2:
    PM25_mean = aotizhongxin_df['CO'].mean().round(2)
    st.metric("Average CO", value=PM25_mean)

with col3:
    PM25_min = aotizhongxin_df['CO'].min().round(2)
    st.metric("Minimum CO", value=PM25_min)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    aotizhongxin_df["date"],
    aotizhongxin_df["CO"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)

ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)

#Dashboard kadar SO2 di kota Aotizhongxin
st.subheader('Kadar O3')

col1, col2, col3 = st.columns(3)

with col1:
    PM25_max = aotizhongxin_df['O3'].max().round(2)
    st.metric("Maximum O3", value=PM25_max)

with col2:
    PM25_mean = aotizhongxin_df['O3'].mean().round(2)
    st.metric("Average O3", value=PM25_mean)

with col3:
    PM25_min = aotizhongxin_df['O3'].min().round(2)
    st.metric("Minimum O3", value=PM25_min)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    aotizhongxin_df["date"],
    aotizhongxin_df["O3"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)

ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)

st.caption('Copyright © Aldiansyah Anugrah Ramadhan')