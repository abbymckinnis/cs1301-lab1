import streamlit as st

st.set_page_config(page_title="Interactive Quiz", page_icon="🧠")

st.title("Interactive Personality Quiz 🧠")
st.write("Answer the questions below to get your result!")

# EXTRA CREDIT
st.toast("Quiz loaded! 🎉")

# EXTRA CREDIT
tabs = st.tabs(["📝 Quiz", "ℹ️ How It Works", "⭐ Extra"])

with tabs[1]:
    st.write(
        "This quiz assigns points to three categories based on your answers. "
        "At the end, the category with the most points becomes your result."
    )
    with st.expander("Simple explanation"):
        st.write("More points in a category = your final result.")

with tabs[2]:
    st.write("Extra customization added for demo points:")
    st.write("- Tabs")
    st.write("- Toast notification")
    st.write("- Downloadable results")
    st.write("- Expanders")

# ---------------- QUIZ TAB ----------------
with tabs[0]:

    # Show images (requirement)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("Images/gt.png", use_container_width=True)
    with col2:
        st.image("Images/msp.png", use_container_width=True)
    with col3:
        st.image("Images/gac.png", use_container_width=True)

    st.divider()

    # Initialize scores
    points = {"Competitor": 0, "Creative": 0, "Chill": 0}

    # Question 1 — radio
    st.subheader("Question 1")
    q1 = st.radio(
        "Your ideal Friday night:",
        ["Training / grinding", "Watching a movie", "Hanging with friends"]
    )
    if q1 == "Training / grinding":
        points["Competitor"] += 2
    elif q1 == "Watching a movie":
        points["Chill"] += 2
    else:
        points["Creative"] += 2

    # Question 2 — multiselect
    st.subheader("Question 2")
    q2 = st.multiselect(
        "Choose activities you enjoy:",
        ["Sports", "Music", "Art", "Gaming", "Travel", "Cooking"]
    )
    for item in q2:
        if item in ["Sports", "Travel"]:
            points["Competitor"] += 1
        elif item in ["Art", "Music"]:
            points["Creative"] += 1
        else:
            points["Chill"] += 1

    # Question 3 — slider
    st.subheader("Question 3")
    q3 = st.slider("How competitive are you?", 0, 10, 5)
    if q3 >= 7:
        points["Competitor"] += 2
    elif q3 <= 3:
        points["Chill"] += 2
    else:
        points["Creative"] += 2

    # Question 4 — number input
    st.subheader("Question 4")
    q4 = st.number_input(
        "How many hours of sleep did you get last night?",
        min_value=0.0,
        max_value=14.0,
        value=7.0,
        step=0.5
    )
    if q4 < 6:
        points["Competitor"] += 1
        points["Creative"] += 1
    elif q4 > 8:
        points["Chill"] += 2
    else:
        points["Chill"] += 1

    # Question 5 — selectbox
    st.subheader("Question 5")
    q5 = st.selectbox(
        "Pick a snack:",
        ["Protein bar", "Fruit", "Chips", "Donuts", "Popcorn"]
    )
    if q5 == "Protein bar":
        points["Competitor"] += 2
    elif q5 == "Fruit":
        points["Creative"] += 2
    else:
        points["Chill"] += 2

    st.divider()

    # Progress bar
    st.progress(1.0)

    # Metrics (nice for demo)
    c1, c2, c3 = st.columns(3)
    c1.metric("Competitor", points["Competitor"])
    c2.metric("Creative", points["Creative"])
    c3.metric("Chill", points["Chill"])

    st.divider()

    # Result button
    if st.button("Get My Result 🎉"):
        result = max(points, key=points.get)

        st.header(f"Your Result: {result}")

        if result == "Competitor":
            st.write(
                "You are driven, disciplined, and goal-oriented. "
                "You thrive under pressure and enjoy pushing yourself."
            )
            st.image("Images/all american.png", use_container_width=True)

        elif result == "Creative":
            st.write(
                "You are thoughtful, expressive, and imaginative. "
                "You enjoy learning people and creating meaning."
            )
            st.image("Images/bsa.png", use_container_width=True)

        else:
            st.write(
                "You bring calm energy. You value balance, peace, and enjoyment."
            )
            st.image("Images/gac.png", use_container_width=True)

        # EXTRA CREDIT
        summary = f"Quiz Result: {result}\n\nPoints Breakdown:\n{points}"
        st.download_button(
            "Download my result 📄",
            data=summary,
            file_name="quiz_result.txt",
        )

        st.balloons()
