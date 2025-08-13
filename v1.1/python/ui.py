import streamlit as st
from map_utils import create_map

def render_sidebar():
    st.sidebar.header("Controls")
    st.sidebar.date_input("Start Date")
    st.sidebar.date_input("End Date")

def render_map():
    m = create_map()
    st.components.v1.html(m.to_html(), height=600)
