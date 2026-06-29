import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Healthcare Dashboard", layout="wide")

st.title("🏥 Healthcare Analytics Dashboard")

df = pd.read_csv("data/patient_data.csv")

# Sidebar filters
st.sidebar.header("🔍 Filters")
diagnosis_filter = st.sidebar.multiselect(
    "Select Diagnosis",
    options=df["Diagnosis"].unique(),
    default=df["Diagnosis"].unique()
)
gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

filtered_df = df[
    (df["Diagnosis"].isin(diagnosis_filter)) &
    (df["Gender"].isin(gender_filter))
]

# KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Patients", len(filtered_df))
col2.metric("Readmitted", len(filtered_df[filtered_df["Readmitted"]=="Yes"]))
col3.metric("Avg Stay (Days)", f"{filtered_df['HospitalStayDays'].mean():.1f}")
col4.metric("Avg Cost (₹)", f"{filtered_df['TreatmentCost'].mean():,.0f}")

st.markdown("---")

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Patient Count by Diagnosis")
    fig, ax = plt.subplots()
    filtered_df["Diagnosis"].value_counts().plot(kind="bar", ax=ax, color="steelblue")
    st.pyplot(fig)

with col2:
    st.subheader("Readmission Rate")
    fig, ax = plt.subplots()
    filtered_df["Readmitted"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
    st.pyplot(fig)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Avg Stay by Diagnosis")
    fig, ax = plt.subplots()
    filtered_df.groupby("Diagnosis")["HospitalStayDays"].mean().sort_values().plot(kind="barh", color="coral", ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Cost by Outcome")
    fig, ax = plt.subplots()
    sns.boxplot(x="Outcome", y="TreatmentCost", data=filtered_df, ax=ax)
    st.pyplot(fig)

st.markdown("---")
st.subheader("📋 Patient Data")
st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)