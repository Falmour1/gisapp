import streamlit as st
from ui import render_sidebar, render_map
from gee_utils import initialize_gee

# Initialize Google Earth Engine
initialize_gee()

# Set up Streamlit page
st.set_page_config(page_title="GIS APP by Falm", layout="wide")

# Sidebar & UI
render_sidebar()
render_map()
