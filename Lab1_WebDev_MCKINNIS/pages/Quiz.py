import streamlit as st
from pathlib import Path

# Safe image path setup
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR.parent / "images"

st.set_page_config(page_title="Quiz", page_icon="🧠", layout="centered")

st.title("Interactive Personality Quiz 🧠")
st.write("Answer the questions below to get your result!")

# --- Small image strip at the top (INCLUDING merch.png) ---
top_images = [
    ("gt.png", "Georgia Tech"),
    ("msp.png", "MSP"),
    ("gac.png", "GAC"),
    ("bsa.png", "BSAA"),
    ("all american.png", "All American"),
    ("me.png", "Me"),
    ("merch.png", "Merch"),
]

st.markdown("#### 📸 Quick Highlights")
cols = st.columns(4)  # 4 across; wraps automatically in rows
for i, (fname, cap) in enumerate(top_images):
    with cols[i % 4]:
        st.image(str(IMAGE_DIR / fname), width=150)
        st.caption(cap)

st.divider()

tabs = st.tabs(["📝 Quiz", "ℹ️ How It Works", "⭐ Extra"])

with tabs[1]:
    st.write(
        "You’ll answer 5 questions. Each choice adds points to a personality type. "
        "The type with the most points becomes your result!"
    )

with tabs[2]:
    st.write("Extra features used:")
    st.write("- Tabs")
    st.write("- Progress bar")
    st.write("- Image gallery at top")
    st.write("- Balloons")

with tabs[0]:
    # --- Questions ---
    q1 = st.radio("1) Pick a vibe:", ["Locked in", "Chill", "Chaos"], index=None)  # NEW
    q2 = st.multiselect("2) Pick 2 things you love:", ["Music", "Sports", "Food", "Sleep", "Travel"])  # NEW
    q3 = st.slider("3) How social are you? (0-10)", 0, 10, 5)  # NEW
    q4 = st.number_input("4) Choose a number (1-100):", min_value=1, max_value=100, value=7)  # NEW
    q5 = st.selectbox("5) Pick a snack:", ["Chips", "Fruit", "Candy", "Protein bar"])  # NEW

    # --- Scoring ---
    calm = 0
    competitive = 0
    chaotic = 0

    if q1 == "Locked in":
        competitive += 2
    elif q1 == "Chill":
        calm += 2
    elif q1 == "Chaos":
        chaotic += 2

    if "Sports" in q2:
        competitive += 1
    if "Sleep" in q2:
        calm += 1
    if "Travel" in q2:
        chaotic += 1

    if q3 >= 7:
        chaotic += 1
    elif q3 <= 3:
        calm += 1
    else:
        competitive += 1

    if q4 % 2 == 0:
        calm += 1
    else:
        chaotic += 1

    if q5 == "Protein bar":
        competitive += 1
    elif q5 == "Fruit":
        calm += 1
    else:
        chaotic += 1

    answered = sum([
        q1 is not None,
        len(q2) > 0,
        q3 is not None,
        q4 is not None,
        q5 is not None
    ])
    st.progress(answered / 5)

    if st.button("Get my result!"):
        scores = {"Calm": calm, "Competitive": competitive, "Chaotic": chaotic}
        result = max(scores, key=scores.get)

        st.success(f"Your result is: **{result}** 🎉")
        st.balloons()

        if result == "Calm":
            st.write("You’re steady, grounded, and the calm in every room.")
        elif result == "Competitive":
            st.write("You’re driven, focused, and always chasing the next goal.")
        else:
            st.write("You’re high-energy, spontaneous, and always down for something fun.")
