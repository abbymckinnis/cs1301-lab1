import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR.parent / "images"

st.set_page_config(page_title="Quiz", page_icon="🧠", layout="centered")

RESULT_IMAGES = {
    "Calm": "https://em-content.zobj.net/source/apple/391/relieved-face_1f60c.png",
    "Competitive": "https://em-content.zobj.net/source/apple/391/fire_1f525.png",
    "Chaotic": "https://em-content.zobj.net/source/apple/391/zany-face_1f92a.png",
    "Creative": "https://em-content.zobj.net/source/apple/391/artist-palette_1f3a8.png",
}

st.title("Interactive Personality Quiz 🧠")
st.write("Answer the questions below to get your result!")

# Top images (no captions)
col1, col2 = st.columns(2)
with col1:
    st.image(str(IMAGE_DIR / "me.png"), width=160)
with col2:
    st.image(str(IMAGE_DIR / "merch.png"), width=160)

st.divider()

tabs = st.tabs(["📝 Quiz", "ℹ️ How It Works", "⭐ Extra"])

with tabs[1]:
    st.write(
        "Each answer adds points to different personality types. "
        "Your final result is the type with the most points."
    )

with tabs[2]:
    st.write("Extra features used:")
    st.write("- Tabs")
    st.write("- Progress bar")
    st.write("- Emoji result image")
    st.write("- Balloons")

with tabs[0]:
    # --- Questions ---
    q1 = st.radio(
        "1) Pick a vibe:",
        ["Locked in", "Chill", "Chaos", "Creative energy"],
        index=None
    )  # NEW

    q2 = st.multiselect(
        "2) Pick 2 things you love:",
        ["Music", "Sports", "Art", "Sleep", "Travel"]
    )  # NEW

    q3 = st.slider(
        "3) Your energy level today (0–10):",
        0, 10, 5
    )  # NEW

    q4 = st.number_input(
        "4) Choose a number (1–100):",
        min_value=1,
        max_value=100,
        value=7
    )  # NEW

    q5 = st.selectbox(
        "5) Pick a snack:",
        ["Chips", "Fruit", "Candy", "Protein bar"]
    )  # NEW

    # --- Scores (balanced) ---
    calm = 0
    competitive = 0
    chaotic = 0
    creative = 0

    # Q1 gives 2 points (NOT overpowering)
    if q1 == "Locked in":
        competitive += 2
    elif q1 == "Chill":
        calm += 2
    elif q1 == "Chaos":
        chaotic += 2
    elif q1 == "Creative energy":
        creative += 2

    # Q2: each selection gives 1 point (max 2 picks = max 2 points)
    for item in q2:
        if item == "Sports":
            competitive += 1
        elif item == "Sleep":
            calm += 1
        elif item == "Travel":
            chaotic += 1
        elif item in ("Music", "Art"):
            creative += 1

    # Q3: energy level gives 2 points to ONE category
    if q3 <= 3:
        calm += 2
    elif q3 <= 6:
        creative += 2
    else:
        chaotic += 2

    # Q4: number pattern gives 2 points to ONE category
    if q4 % 10 == 0:
        competitive += 2
    elif q4 % 2 == 0:
        calm += 2
    else:
        creative += 2

    # Q5: snack gives 2 points to ONE category
    if q5 == "Protein bar":
        competitive += 2
    elif q5 == "Fruit":
        calm += 2
    elif q5 == "Candy":
        creative += 2
    else:  # Chips
        chaotic += 2

    # Progress bar
    answered = sum([
        q1 is not None,
        len(q2) > 0,
        q3 is not None,
        q4 is not None,
        q5 is not None
    ])
    st.progress(answered / 5)

    if st.button("Get my result!"):
        scores = {
            "Calm": calm,
            "Competitive": competitive,
            "Chaotic": chaotic,
            "Creative": creative
        }

        result = max(scores, key=scores.get)

        st.success(f"Your result is: **{result}** 🎉")
        st.image(RESULT_IMAGES[result], width=120)
        st.balloons()

        if result == "Calm":
            st.write("You’re grounded, steady, and bring peace into any space.")
        elif result == "Competitive":
            st.write("You’re driven, focused, and thrive on goals and challenges.")
        elif result == "Creative":
            st.write("You’re imaginative, expressive, and see the world differently.")
        else:
            st.write("You’re spontaneous, energetic, and always down for something new.")
