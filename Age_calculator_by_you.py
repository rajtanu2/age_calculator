import streamlit as st
from datetime import date

# Set page config
st.set_page_config(page_title="Age Calculator", page_icon="🎂", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Age Calculator 🎂</h1>", unsafe_allow_html=True)
st.markdown("### Enter your Birth Date to Calculate Age")

# Limit date range (1900 to today)
birth_date = st.date_input(
    "Select your Birth Date",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

# Calculate age
if st.button("Calculate Age"):
    today = date.today()
    if birth_date > today:
        st.error("❌ Birth date cannot be in the future!")
    else:
        age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        age_days = (today - birth_date).days
        st.success(f"🎉 You are {age_years} years old!")
        st.info(f"📅 Total Days Lived: {age_days} days")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ by Mayur Bhamare</p>", unsafe_allow_html=True)
