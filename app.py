# -*- coding: utf-8 -*-
import streamlit as st
import datetime
import random
import re

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Smart AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ================= SESSION =================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# ================= CSS =================
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
    background:linear-gradient(135deg,#020617,#020617,#0f172a);
}
.login-box{
    max-width:420px;
    margin:120px auto;
    padding:40px;
    background:#020617;
    border-radius:20px;
    border:1px solid #1e293b;
    box-shadow:0 0 40px rgba(59,130,246,0.35);
}
button{
    background:linear-gradient(135deg,#2563eb,#3b82f6) !important;
    color:white !important;
    border:none !important;
    border-radius:14px !important;
    padding:8px 20px !important;
}
button:hover{
    background:linear-gradient(135deg,#1d4ed8,#2563eb) !important;
}
.user{
    float:right;
    background:#2563eb;
    color:white;
    padding:12px 16px;
    border-radius:18px;
    margin:6px 0;
    max-width:65%;
    clear:both;
}
.bot{
    float:left;
    background:#020617;
    color:#facc15;
    padding:12px 16px;
    border-radius:18px;
    margin:6px 0;
    max-width:65%;
    clear:both;
    border:1px solid #1e293b;
}
input{
    border-radius:16px !important;
    border:2px solid #1e293b !important;
}
input:focus{
    outline:none !important;
    border-color:#3b82f6 !important;
    box-shadow:none !important;
}
.logout-btn{
    position:fixed;
    top:20px;
    right:30px;
}
</style>
""", unsafe_allow_html=True)

# ================= LOGIN PAGE =================
if not st.session_state.logged_in:
    st.markdown("""
    <div class="login-box">
        <h2 style="text-align:center;color:white;">🔐 Login</h2>
    </div>
    """, unsafe_allow_html=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if email and password:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.warning("Please enter email and password")

    st.stop()

# ================= LOGOUT =================
with st.container():
    st.markdown("<div class='logout-btn'>", unsafe_allow_html=True)
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.messages = []
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ================= KNOWLEDGE BASE (40+ QUESTIONS) =================
qa = {
    "hello": ["Hello 👋", "Hi there 😊"],
    "hi": ["Hi 👋", "Hey 😊"],
    "how are you": ["I'm doing great 😄", "All good here!"],
    "good morning": ["Good morning ☀️"],
    "good night": ["Good night 🌙 Sweet dreams"],
    "your name": ["I'm Smart AI Chatbot 🤖"],
    "what do you do": ["I chat, answer questions and help you learn 💬"],
    "who made you": ["I was created by Akanksha Khurana 💙"],
    "date": [datetime.date.today().strftime("%d %B %Y")],
    "time": [datetime.datetime.now().strftime("%I:%M %p")],
    "day": [datetime.datetime.now().strftime("%A")],
    "bye": ["Goodbye 👋", "See you soon 😊"],
    "thank you": ["You're welcome 💙", "Anytime 😄"],
    "help": ["I can chat, answer basics and guide you 🤖"],
    "joke": ["Why do programmers love dark mode? Less bugs 😂"],
    "weather": ["I can't access live weather yet 🌦️"],
    "age": ["I’m timeless 😎"],
    "love": ["I love helping you 💙"],
    "ai": ["AI means Artificial Intelligence 🤖"],
    "python": ["Python is powerful and beginner-friendly 🐍"],
    "study": ["Consistency beats talent 💪"],
    "motivate": ["You’re doing amazing 🌟 Keep going!"],
    "life": ["Life is all about learning and growth 🌱"],
    "coding": ["Practice daily and build projects 💻"],
    "chatbot": ["A chatbot talks with users automatically 🤖"],
    "future": ["Your future is bright ✨"],
    "food": ["I like pizza 🍕"],
    "movie": ["I love sci-fi movies 🤖"],
    "cricket": ["Cricket is amazing 🏏"],
    "india": ["India is awesome "],
    "location": ["I live in the cloud ☁️"],
    "hobby": ["Chatting with you 😊"],
    "weather": ["I can't check live weather yet 🌦️"],
    "exam": ["You will do great 💪"],
   
}

def get_reply(text):
    replies = []
    for key, values in qa.items():
        if key in text:
            replies.append(random.choice(values))
    return replies if replies else ["Tell me more 🤔"]

# ================= CHAT UI =================
st.markdown("<h1 style='text-align:center;color:white;'>🤖 Smart AI Chatbot</h1>", unsafe_allow_html=True)

for role, msg in st.session_state.messages:
    st.markdown(f"<div class='{role}'>{msg}</div>", unsafe_allow_html=True)

# ================= INPUT HANDLER =================
def handle_input():
    text = st.session_state.user_input.strip()
    if not text:
        return

    st.session_state.messages.append(("user", text))

    # SPLIT MULTIPLE QUESTIONS
    parts = re.split(r"[?.!]", text.lower())
    for part in parts:
        part = part.strip()
        if part:
            replies = get_reply(part)
            for r in replies:
                st.session_state.messages.append(("bot", r))

    st.session_state.user_input = ""

st.text_input(
    "",
    placeholder="Type your message and press Enter...",
    key="user_input",
    on_change=handle_input
)
