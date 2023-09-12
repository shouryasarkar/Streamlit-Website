import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title= "My Webpage", page_icon="😃", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        # This line is to remove the streamlit text from below the webpage 
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/9c7d8841-1027-44f9-8cec-185fd6189444/uvYPsETmGZ.json")
# img_contact_form = Image.open("C:\Users\Shourya Sarkar\OneDrive\Desktop 1\Sreamlit Projects\images\Pharmacy.png")

#---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Shourya 👋")
    st.title("A passionate coder from India.")

# What I do 

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")

        st.write("##")
        st.write("Welcome to my website! My name is Shourya Sarkar and I am excited to share my story with you. I am a sophmore at Heritage Institute of Technology, and have a passion for building robots and machine learning. Throughout my life, I have faced many challenges and opportunities that have helped me grow and develop into the person I am today. I believe in the power of hard work, determination, and perseverance to achieve one's goals and dreams.On this website, you will find information about my background, experiences, and achievements. I hope that my story will inspire and motivate you to pursue your own passions and goals. Thank you for visiting my website and I look forward to sharing more with you.")
        st.write("[Youtube Channel >](https://www.youtube.com/channel/UCUOfLqwwfoaX5ZE_4nCjoWw)")


    with right_column:
        st_lottie(lottie_coding, height=300, key = "coding")


# ----- PROJECTS ------
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))

    # with image_column:
    #     #insert image
    #     st.image(img_contact_form)

    with text_column:
        st.subheader("Alexa")
        st.write("##")
        st.write("It's a simple Alexa without AI properties which can do do a lot of of things.It is capable of voice interaction, music playback,setting alarms and providing weather, traffic, sports, and other real-time information, such as news. Working on it to modify some features.")
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=dIhAF6g5Izg)")



# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/shouryapr123@gmail.com" method="POST">
    <input type = "hidden" name = "_captcha" value = "false">
        <input type="text" name="name" placeholder = "Your Name" required>
        <input type="email" name="email" placeholder = "Your Email" required>
        <textarea name = "message" placeholder = "Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()