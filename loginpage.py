import streamlit as st

# Read the HTML file
with open("myapp.html", "r") as f:
    html_content = f.read()

# Render in Streamlit
st.components.v1.html(html_content, height=400)
