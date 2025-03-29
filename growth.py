# import streamlit as st

# st.set_page_config(page_title= "growth mindset project", page_icon="⭐")
# st.title("🧠 Growth Mindset Challenge: Web App With Streamlit")

# st.header("🚀 Welcome to your Own Growth Journey!")
# st.write("Embrace challenges, learn from mistakes, and unlock yuor full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! 🌟")

# # Quote section:
# st.header("💡 Today's Growth Mindset Quote")
# st.write("Success is not final, failure is not fatal: it is the courage to continue that counts.-Winston Churchill")

# st.header("🔧 What's Your Challenge Today?")
# user_input = st.text_input("Describe a Challenge you're facing:")



# # Condition:
# if user_input:
#     st.success(f"💪🏻You're facing: {user_input}. keep pushing forward towards your goal!🚀")
# else:
#     st.warning("Tell us about your challenge to get started!")


# # reflexing:
# st.header("🧠reflect on Your Learning")
# reflection = st.text_area("Write your reflection here:")

# if reflection:
#     st.success(f"✨Great Insight! Your reflection: {reflection}")
# else:
#     st.info("Reflecting on past exprience help you grow! Share your difficulties")


# # acheivements:
# st.header("🏆 Celebrate Your Wins")
# acheivements = st.text_input("Share something yoy've recently accomplished:")

# if acheivements:
#     st.success(f"🎉 Amazing! You achieved: Amazing! You achieved: {acheivements}")
# else:
#     st.info("Big or Small , every acheivement counts! Share one now 😊")
    
    
    
# result = st.button("🔥 Need More Motivation?")

# if result:
#     st.write("You're doing amazing! Every step counts. Keep growing and shining!✨")
    


# # footer:
# st.write("- - -")
# st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
# st.write("**⛔ Created by Efza Laraib**")



























import streamlit as st

# Set page configuration
st.set_page_config(page_title="Growth Mindset Project", page_icon="⭐")
st.title("🧠 Growth Mindset Challenge: Web App With Streamlit")

# Inject custom CSS for styling
st.markdown("""
    <style>
        /* General page styling */
        body {
            background-color: #FFB6C1;  /* Add your preferred background color here */
            font-family: 'Arial', sans-serif;
            color: #333;
        }

        /* Title Styling */
        .title {
            font-size: 2.5rem;
            color: #4CAF50;
            text-align: center;
        }

        /* Header Styling */
        h1, h2, h3 {
            color: #4CAF50;
            text-align: center;
        }

        /* Section Header */
        .section-header {
            font-size: 1.8rem;
            color: #ff6347;
            text-align: center;
            margin-top: 30px;
        }

        /* Write section Styling */
        .section-write {
            text-align: center;
            font-size: 1.1rem;
            margin-top: 20px;
            color: #555;
        }

        /* Button Styling */
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            font-size: 1rem;
            width: 200px;
            margin: auto;
            padding: 12px;
            border: none;
        }

        .stButton button:hover {
            background-color: #45a049;
        }

        /* Success, Warning, Info, and Error message Styling */
        .stSuccess, .stWarning, .stInfo {
            font-size: 1.1rem;
            border-radius: 5px;
            padding: 10px;
            text-align: center;
            color: #fff;
        }

        .stSuccess {
            background-color: #4CAF50;
        }

        .stWarning {
            background-color: #ff9800;
        }

        .stInfo {
            background-color: #2196F3;
        }

        /* Footer Styling */
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 1rem;
            color: #999;
        }
    </style>
""", unsafe_allow_html=True)

# Title section
st.markdown('<div class="title">🧠 Growth Mindset Challenge: Web App</div>', unsafe_allow_html=True)

# Welcome message
st.header("🚀 Welcome to your Own Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! 🌟")

# Quote section
st.markdown('<div class="section-header">💡 Today\'s Growth Mindset Quote</div>', unsafe_allow_html=True)
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill")

# What's your challenge section
st.markdown('<div class="section-header">🔧 What\'s Your Challenge Today?</div>', unsafe_allow_html=True)
user_input = st.text_input("Describe a Challenge you're facing:")

if user_input:
    st.success(f"💪🏻 You're facing: {user_input}. Keep pushing forward towards your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflect on Your Learning section
st.markdown('<div class="section-header">🧠 Reflect on Your Learning</div>', unsafe_allow_html=True)
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"✨ Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your difficulties.")

# Celebrate Your Wins section
st.markdown('<div class="section-header">🏆 Celebrate Your Wins</div>', unsafe_allow_html=True)
achievements = st.text_input("Share something you've recently accomplished:")

if achievements:
    st.success(f"🎉 Amazing! You achieved: {achievements}")
else:
    st.info("Big or small, every achievement counts! Share one now 😊")

# Motivation button
result = st.button("🔥 Need More Motivation?")

if result:
    st.write("You're doing amazing! Every step counts. Keep growing and shining!✨")

# Footer
st.markdown('<div class="footer">🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟</div>', unsafe_allow_html=True)
st.markdown("**⛔ Created by Efza Laraib**", unsafe_allow_html=True)

