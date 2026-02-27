from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"

# About Me
profile_picture = IMAGE_DIR / "gt.png"

about_me = (
    "Hi! I'm Abby McKinnis. I'm a student at Georgia Tech and a student-athlete. "
    "I’m interested in tech, leadership, and building cool projects!"
)

# Links
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

my_linkedin_url = "https://www.linkedin.com/"
my_github_url = "https://github.com/"
my_email_address = "example@email.com"

# Education
education_data = {
    "Degree": "Bachelor of Science (Computer Science)",
    "Institution": "Georgia Institute of Technology",
    "Location": "Atlanta, GA",
    "Graduation Date": "2029",
    "GPA": "4.0"
}

course_data = {
    "code": ["CS 1301", "MATH 1552", "CS 1331"],
    "names": ["Intro to Computing", "Calculus II", "Intro to OOP"],
    "semester_taken": ["Spring 2026", "Spring 2026", "Future"],
    "skills": ["Python fundamentals", "Integration + series", "Java + OOP basics"]
}

# Experience
experience_data = {
    "Coach at GAC": (
        [
            "- Coached and supported athletes",
            "- Led practices and helped improve performance",
            "- Built strong team culture"
        ],
        IMAGE_DIR / "gac.png"
    ),
    "Board Member (BSAA Committee)": (
        [
            "- Supported Black softball athletes",
            "- Promoted unity and inclusion",
            "- Helped plan events/initiatives"
        ],
        IMAGE_DIR / "bsa.png"
    ),
}

# Projects (make sure you mention your quiz here for the lab requirement)
projects_data = {
    "Streamlit Portfolio": "Built a multi-page Streamlit portfolio website.",
    "Interactive Personality Quiz": "Created a 5-question quiz with multiple input types, images, and 3 result types."
}

# Programming Skills
programming_data = {
    "Python": 85,
    "Java": 60,
    "C": 40
}

# Leadership
leadership_data = {
    "MSP All American Games": (
        ["- Selected to participate and represent the program"],
        IMAGE_DIR / "msp.png"
    )
}

# Activities
activity_data = {
    "All American Games": [
        "- Competed with and supported elite athletes",
        "- Gained experience in high-level environments"
    ]
}
