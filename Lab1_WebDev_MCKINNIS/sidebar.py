import streamlit as st

def show_sidebar():
    with st.sidebar:
        st.header("Navigation")
        st.page_link("Home_Page.py", label="Home")
        st.page_link("pages/1_Portfolio.py", label="Portfolio")
        # add more links as needed
