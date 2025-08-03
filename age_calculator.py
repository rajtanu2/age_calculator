import streamlit as st
from datetime import date

st.set_page_config(page_title="Age Calculator", page_icon="🎂", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Age Calculator 🎂</h1>", unsafe_allow_html=True)
st.markdown("### Enter your Birth Date to Calculate Age")

birth_date = st.date_input("Select your Birth Date")

if st.button("Calculate Age"):
    today = date.today()
    age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    age_days = (today - birth_date).days
    st.success(f"🎉 You are {age_years} years old!")
    st.info(f"📅 Total Days Lived: {age_days} days")

st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ by Mayur Bhamare</p>", unsafe_allow_html=True)
