import streamlit as st

st.set_page_config(page_title= "growth mindset project", page_icon="⭐")
st.title("🧠 Growth Mindset Challenge: Web App With Streamlit")

st.header("🚀 Welcome to your Own Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock yuor full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! 🌟")

# Quote section:
st.header("💡 Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts.-Winston Churchill")

st.header("🔧 What's Your Challenge Today?")
user_input = st.text_input("Describe a Challenge you're facing:")



# Condition:
if user_input:
    st.success(f"💪🏻You're facing: {user_input}. keep pushing forward towards your goal!🚀")
else:
    st.warning("Tell us about your challenge to get started!")


# reflexing:
st.header("🧠reflect on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"✨Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past exprience help you grow! Share your difficulties")


# acheivements:
st.header("🏆 Celebrate Your Wins")
acheivements = st.text_input("Share something yoy've recently accomplished:")

if acheivements:
    st.success(f"🎉 Amazing! You achieved: Amazing! You achieved: {acheivements}")
else:
    st.info("Big or Small , every acheivement counts! Share one now 😊")
    
    
    
result = st.button("🔥 Need More Motivation?")

if result:
    st.write("You're doing amazing! Every step counts. Keep growing and shining!✨")
    


# footer:
st.write("- - -")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
st.write("**⛔ Created by Efza Laraib**")


