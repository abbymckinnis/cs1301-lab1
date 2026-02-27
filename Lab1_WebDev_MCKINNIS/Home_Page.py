import streamlit as st
from pathlib import Path

# Build an absolute path to /images no matter where Streamlit runs from
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"

st.set_page_config(page_title="Lab 1 Home", page_icon="🏠", layout="centered")

st.title("Web Development Lab 1")
st.subheader("CS 1301")
st.write("**Abby McKinnis**")

st.write("""
Welcome to my Lab 1 Streamlit app! Use the sidebar to navigate between pages.

1. **Portfolio**: Learn about me, my experience, skills, and projects.
2. **Quiz**: Take my interactive personality quiz and get a result!
""")

st.image(str(IMAGE_DIR / "gt.png"), use_container_width=True)
