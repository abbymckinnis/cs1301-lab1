import streamlit as st

st.set_page_config(page_title="Quiz", page_icon="🧠", layout="centered")

st.title("Interactive Personality Quiz 🧠")
st.write("Answer the questions below to get your result!")

tabs = st.tabs(["📝 Quiz", "ℹ️ How It Works", "⭐ Extra"])

with tabs[1]:
    st.write("You’ll answer 5 questions. Your choices add points to different personality types.")
    st.write("At the end, the type with the most points is your result!")

with tabs[2]:
    st.write("Extra features:")
    st.write("- Tabs")
    st.write("- Progress bar")
    st.write("- Balloons on submit")

with tabs[0]:
    st.image("images/gt.png", use_container_width=True)

    # --- Questions (5 total, 3+ types) ---
    q1 = st.radio("1) Pick a vibe:", ["Locked in", "Chill", "Chaos"], index=None)  # NEW
    q2 = st.multiselect("2) Pick 2 things you love:", ["Music", "Sports", "Food", "Sleep", "Travel"])  # NEW

    st.image("images/msp.png", use_container_width=True)

    q3 = st.slider("3) How social are you? (0-10)", 0, 10, 5)  # NEW
    q4 = st.number_input("4) Choose a number (1-100):", min_value=1, max_value=100, value=7)  # NEW

    st.image("images/gac.png", use_container_width=True)

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

    total_answered = 0
    if q1 is not None:
        total_answered += 1
    if len(q2) > 0:
        total_answered += 1
    if q3 is not None:
        total_answered += 1
    if q4 is not None:
        total_answered += 1
    if q5 is not None:
        total_answered += 1

    st.progress(total_answered / 5)

    if st.button("Get my result!"):
        scores = {"Calm": calm, "Competitive": competitive, "Chaotic": chaotic}
        result = max(scores, key=scores.get)

        st.success(f"Your result is: **{result}** 🎉")
        st.balloons()

        if result == "Calm":
            st.image("images/bsa.png", use_container_width=True)
            st.write("You’re steady, grounded, and you keep people level.")
        elif result == "Competitive":
            st.image("images/all american.png", use_container_width=True)
            st.write("You’re focused, driven, and love chasing big goals.")
        else:
            st.image("images/gac.png", use_container_width=True)
            st.write("You’re spontaneous, high-energy, and always down for something new.")
