# info.py
# This file contains the information displayed in your Streamlit portfolio.

# -------------------------
# ABOUT ME
# -------------------------
# Make sure this file exists inside: Images/
# (Example: Lab1_WebDev_MCKINNIS/Images/profile.jpeg)
profile_picture = "Images/profile.jpeg"

about_me = (
    "I'm Abby McKinnis. I’m a CS major at Georgia Tech, "
    "and I also play for the women’s softball team."
)

# -------------------------
# SOCIALS (optional)
# -------------------------
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

my_linkedin_url = "https://www.linkedin.com/in/abigail-mckinnis-3603063ab/"
my_github_url = "https://github.com/abbymckinnis"
my_email_address = "amckinnis6@gatech.edu"

# -------------------------
# EDUCATION + COURSES
# -------------------------
# DataFrame-friendly format (lists)
education_data = {
    "Field": ["Degree", "Institution", "Location", "Graduation Date", "GPA"],
    "Value": [
        "Bachelor of Science in Computer Science",
        "Georgia Institute of Technology",
        "Atlanta, GA",
        "May 2029",
        "4.0",
    ],
    "Logo": ["Images/gt.png"] * 5,
}

course_data = {
    "code": ["CS 1301", "CS 1300", "MATH 1551"],
    "names": ["Intro to CS", "People Skills", "Calc 1"],
    "semester_taken": ["2nd", "2nd", "1st"],
    "skills": [
        "Python is not my favorite snake anymore",
        "Connection between people and computers",
        "Number systems and values",
    ],
}

# -------------------------
# EXPERIENCE / LEADERSHIP
# Each entry: title -> (bullet_list, image_path)
# -------------------------
experience_data = {
    "Coach at GAC": (
        [
            "Coached instead of playing and poured into others",
            "Increased support from fans",
            "Left a positive mark on the school",
        ],
        "Images/gac.png",
    ),
    "Board Member for BSAA Committee": (
        [
            "Promoted and supported Black softball athletes",
            "Helped improve inclusion and community",
        ],
        "Images/bsa.png",
    ),
    "Head Member of HS Committee": (
        [
            "Managed Honors Society activities (tutoring and education support)",
        ],
        "Images/gt.png",
    ),
}

leadership_data = {
    "Coached at MSP All American Games": (
        [
            "Selected as one of the top coaches and earned my first win",
        ],
        "Images/msp.png",
    ),
}

activity_data = {
    "Minority Softball Prospects – All American Games": [
        "Helped the foundation by being the face of the program",
        "Attracted more viewers and participants",
    ]
}

# -------------------------
# PROJECTS
# -------------------------
projects_data = {
    "RecruitHer App": (
        "Helped develop a recruiting website to support girls in sports "
        "by improving visibility and connections."
    ),
    "Interactive Streamlit Quiz": (
        "Built an interactive 5-question quiz using Streamlit with multiple "
        "question types, images, and dynamic results."
    ),
}

# -------------------------
# SKILLS
# -------------------------
programming_data = {
    "Python": 90,
    "Java": 70,
    "C": 40,
}

programming_icons = {
    "Python": "🐍",
    "Java": "☕",
    "C": "🔍",
}

spoken_data = {
    "English": "Fluent",
    "French": "Fluent (except for some words)",
}

spoken_icons = {
    "English": "🇬🇧",
    "French": "🇫🇷",
    "Spanish": "🇪🇸",
}                                                           "- improved racial tensions and black beleif"],"bsa.png"),
    "Head member of HS committee":(["- Managed and handled most Honors Society activities within the school in regards to tutoring and edu."],"gt.png")

}

projects_data = {
    "RecruitHer App": "Helped develop a recruiting website to support girls in sports by improving visibility and connections.",
    "Interactive Streamlit Quiz": "Built an interactive 5-question quiz using Streamlit with multiple question types, images, and dynamic results to match the user with a result type."
}

programming_data = {
    "Python": 90,
    "Java": 70,
    "C": 40,
}

#CHANGE BELOW (OPTIONAL)
programming_icons = {
    "Python": "🐍",
    "Java": "☕",
    "C": "🔍",
}
spoken_icons = {"French": "🇫🇷",
    "English": "🇬🇧",
    "Spanish":"🇪🇸"
}

#CHANGE BELOW
spoken_data = {
    "English": "Fluent",
    "French": "Fluent except for some words",
}
leadership_data = {
    "Coached at MSP All American Games": (["- Elected as one of the top coaches and earned my first win"],"msp.png"),

}
activity_data={
    "Minority Softball Prospects- All American Games": ["- Helped the foundation earn money by being the face of the program", 
            "- Attracted so many viewers and participants."]
}
