import streamlit as st

st.title("Interactive Personality Quiz 🧠")

st.image("../images/gt.png", use_container_width=True)

q1 = st.radio("Pick a vibe:", ["Locked in", "Chill", "Chaos"], index=None)
q2 = st.multiselect("Pick two:", ["Music", "Sports", "Sleep", "Travel"])
q3 = st.slider("How social are you?", 0, 10, 5)

calm = competitive = chaotic = 0

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

if q3 >= 7:
    chaotic += 1

if st.button("Get result"):
    result = max(
        {"Calm": calm, "Competitive": competitive, "Chaotic": chaotic},
        key=lambda x: {"Calm": calm, "Competitive": competitive, "Chaotic": chaotic}[x]
    )
    st.success(f"You are **{result}**!")
