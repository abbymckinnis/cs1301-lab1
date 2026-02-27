import streamlit as st
import pandas as pd
import info

st.set_page_config(page_title="Portfolio", page_icon="📌", layout="wide")


# ---------- Sidebar Links ----------
def links_section():
    st.sidebar.header("Links")

    linkedin_link = f'<a href="{info.my_linkedin_url}" target="_blank"><img src="{info.linkedin_image_url}" width="70"></a>'
    github_link = f'<a href="{info.my_github_url}" target="_blank"><img src="{info.github_image_url}" width="60"></a>'
    email_link = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" width="70"></a>'

    st.sidebar.markdown("LinkedIn", unsafe_allow_html=True)
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)

    st.sidebar.markdown("GitHub", unsafe_allow_html=True)
    st.sidebar.markdown(github_link, unsafe_allow_html=True)

    st.sidebar.markdown("Email", unsafe_allow_html=True)
    st.sidebar.markdown(email_link, unsafe_allow_html=True)


# ---------- About Me ----------
def about_me_section():
    st.title("Portfolio")
    st.header("About Me")
    st.image(info.profile_picture, width=220)
    st.write(info.about_me)
    st.divider()


# ---------- Education ----------
def education_section(education_data, course_data):
    st.header("Education")
    st.subheader(education_data["Institution"])
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Location:** {education_data['Location']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")

    st.subheader("Relevant Coursework")
    df = pd.DataFrame(course_data)
    st.dataframe(df, hide_index=True, use_container_width=True)
    st.divider()


# ---------- Experience ----------
def experience_section(experience_data):
    st.header("Experience")
    for title, (bullets, img_path) in experience_data.items():
        st.subheader(title)
        st.image(img_path, use_container_width=True)
        for b in bullets:
            st.write(b)
        st.write("")
    st.divider()


# ---------- Projects ----------
def projects_section(projects_data):
    st.header("Projects")
    for title, desc in projects_data.items():
        st.subheader(title)
        st.write(desc)
    st.divider()


# ---------- Programming Skills ----------
def programming_section(programming_data):
    st.header("Programming Skills")
    for lang, level in programming_data.items():
        st.write(f"**{lang}**")
        st.progress(int(level))
    st.divider()


# ---------- Leadership ----------
def leadership_section(leadership_data):
    st.header("Leadership")
    for title, (bullets, img_path) in leadership_data.items():
        st.subheader(title)
        st.image(img_path, use_container_width=True)
        for b in bullets:
            st.write(b)
        st.write("")
    st.divider()


# ---------- Activities ----------
def activities_section(activity_data):
    st.header("Activities")
    for title, bullets in activity_data.items():
        st.subheader(title)
        for b in bullets:
            st.write(b)


# Run page
links_section()
about_me_section()
education_section(info.education_data, info.course_data)
experience_section(info.experience_data)
projects_section(info.projects_data)
programming_section(info.programming_data)
leadership_section(info.leadership_data)
activities_section(info.activity_data)
