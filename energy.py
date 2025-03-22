import streamlit as st
import google.generativeai as genai
import os
import json

# Configure API key for Google Gemini
genai.configure(api_key=os.getenv("AIzaSyC_IdYlWLiCXtVvn2qlLZIFgD6Rm9Smg5U"))

# Load user credentials from Streamlit Secrets
USER_CREDENTIALS = json.loads(st.secrets["USER_CREDENTIALS"])

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def login():
    """Login Page"""
    st.title("🔐 Login to Energy Tracker")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.authenticated = True
            st.success("Login successful! Redirecting...")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password!")

def logout():
    """Logout Function"""
    st.session_state.authenticated = False
    st.experimental_rerun()

def main_app():
    """Main Energy Tracker App"""
    st.title("🔋 Energy Consumption Tracker with AI Insights")

    # Logout Button
    if st.button("Logout"):
        logout()

    # Input fields
    device_name = st.text_input("Enter Device Name:")
    power = st.number_input("Power (W)", min_value=0.0, format="%.2f")
    hours = st.number_input("Hours Used per Day", min_value=0.0, format="%.2f")

    if st.button("Calculate Energy Consumption"):
        if device_name and power > 0 and hours > 0:
            daily_consumption = (power * hours) / 1000  # kWh
            monthly_consumption = daily_consumption * 30
            yearly_consumption = daily_consumption * 365

            st.write(f"### {device_name} Energy Consumption:")
            st.write(f"- *{daily_consumption:.2f} kWh/day*")
            st.write(f"- *{monthly_consumption:.2f} kWh/month*")
            st.write(f"- *{yearly_consumption:.2f} kWh/year*")

            # *Manual Energy-Saving Tips*
            st.subheader("💡 Manual Energy-Saving Tips")
            st.write("- Turn off devices when not in use.")
            st.write("- Use energy-efficient appliances like LED bulbs.")
            st.write("- Unplug chargers and electronics when not needed.")
            st.write("- Reduce screen brightness and use power-saving modes.")

            # *AI-Generated Energy-Saving Tips*
            st.subheader("🤖 AI-Generated Energy-Saving Tips")
            prompt = f"Suggest energy-saving tips for a {device_name} consuming {power}W for {hours} hours daily."

            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt)
                st.write(response.text)
            except Exception as e:
                st.error("Error generating AI response. Please check your API key.")
        else:
            st.error("⚠ Please enter valid values.")

# Show login page if user is not authenticated
if not st.session_state.authenticated:
    login()
else:
    main_app()
