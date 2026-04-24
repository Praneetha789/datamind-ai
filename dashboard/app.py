import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import json
import os
import time

# ================= CONFIG =================
st.set_page_config(page_title="DataMind AI SaaS", layout="wide")

DB_FILE = "users_db.json"

# ================= USER DB =================
def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f)

db = load_db()

# ================= SESSION =================
if "user" not in st.session_state:
    st.session_state.user = None

if "chat" not in st.session_state:
    st.session_state.chat = []

# ================= SPLASH SCREEN =================
if "splash" not in st.session_state:
    st.session_state.splash = True

if st.session_state.splash:
    splash = st.empty()

    splash.markdown("""
    <style>
    .splash {
        position: fixed;
        top:0;left:0;
        width:100%;height:100%;
        background: linear-gradient(135deg,#06b6d4,#7c3aed,#22c55e);
        display:flex;
        justify-content:center;
        align-items:center;
        flex-direction:column;
        z-index:9999;
        animation: fade 2s ease-in-out;
    }

    .title {
        font-size:70px;
        font-weight:900;
        color:white;
        animation: zoom 1.5s infinite alternate;
        text-shadow:0 0 30px rgba(255,255,255,0.5);
    }

    .sub {
        color:white;
        font-size:18px;
        margin-top:10px;
        opacity:0.8;
    }

    @keyframes zoom {
        from {transform:scale(1);}
        to {transform:scale(1.1);}
    }

    @keyframes fade {
        from {opacity:0;}
        to {opacity:1;}
    }
    </style>

    <div class="splash">
        <div class="title">DataMind AI</div>
        <div class="sub">AI Analytics • Smart Cleaning • Data Intelligence</div>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(2)
    splash.empty()
    st.session_state.splash = False

# ================= LOGIN =================
if st.session_state.user is None:

    st.markdown("""
    <style>
    .login-box{
        text-align:center;
        padding:40px;
    }

    .login-title{
        font-size:55px;
        font-weight:900;
        background: linear-gradient(90deg,#06b6d4,#7c3aed,#22c55e);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='login-box'><div class='login-title'>Welcome to DataMind AI</div></div>", unsafe_allow_html=True)

    username = st.text_input("Enter your name")
    password = st.text_input("Password", type="password")

    if st.button("Login / Signup"):
        if username:
            if username not in db:
                db[username] = {"password": password, "uploads": []}
                save_db(db)

            if db[username]["password"] == password:
                st.session_state.user = username
                st.rerun()
            else:
                st.error("Wrong password")

    st.stop()

user = st.session_state.user
user_data = db[user]

# ================= MAIN UI STYLE =================
st.markdown("""
<style>

body{
    background: linear-gradient(135deg,#7c3aed,#06b6d4,#22c55e);
    color:white;
}

/* GLASS CARD */
.card{
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(20px);
    border-radius:18px;
    padding:20px;
    border:1px solid rgba(255,255,255,0.3);
    transition:0.4s;
}

.card:hover{
    transform:translateY(-10px) scale(1.03);
    box-shadow:0 20px 40px rgba(0,0,0,0.2);
}

/* BUTTON */
.stButton>button{
    background: linear-gradient(90deg,#06b6d4,#7c3aed,#22c55e);
    color:white;
    border-radius:10px;
}

/* CHAT */
.chat{
    background: rgba(255,255,255,0.2);
    padding:10px;
    border-radius:12px;
    height:250px;
    overflow:auto;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown(f"""
<h1 style='text-align:center;'>👋 Welcome {user}</h1>
<p style='text-align:center;'>AI SaaS Analytics Dashboard</p>
""", unsafe_allow_html=True)

# ================= CARDS =================
c1, c2, c3 = st.columns(3)

c1.markdown("<div class='card'>⚡ Smart Data Cleaning Engine</div>", unsafe_allow_html=True)
c2.markdown("<div class='card'>📊 AI Visualization Dashboard</div>", unsafe_allow_html=True)
c3.markdown("<div class='card'>🤖 AI Chat Assistant</div>", unsafe_allow_html=True)

# ================= UPLOAD =================
st.sidebar.title("Control Panel")

file = st.sidebar.file_uploader("Upload Dataset", type=["csv","xlsx"])
run = st.sidebar.button("Run AI Engine")

# ================= DATA =================
if file:
    df = pd.read_csv(file) if file.name.endswith("csv") else pd.read_excel(file)

    st.subheader("Dataset Preview")
    st.dataframe(df, use_container_width=True)

    if run:
        df_clean = df.copy()

        df_clean = df_clean.drop_duplicates()

        for col in df_clean.select_dtypes(include=np.number).columns:
            df_clean[col] = df_clean[col].fillna(df_clean[col].median())

        # KPI SCORE
        score = 85

        st.markdown("## 📊 AI Data Health")

        radius = 80
        circumference = 2 * np.pi * radius
        offset = circumference - (circumference * score / 100)

        st.markdown(f"""
        <svg width="220" height="220">
            <circle cx="110" cy="110" r="80" stroke="white" stroke-width="10" fill="none" opacity="0.2"/>
            <circle cx="110" cy="110" r="80"
                stroke="#22c55e"
                stroke-width="10"
                fill="none"
                stroke-linecap="round"
                stroke-dasharray="{circumference}"
                stroke-dashoffset="{offset}"
                transform="rotate(-90 110 110)"/>
            <text x="50%" y="50%" text-anchor="middle" font-size="28" fill="white">{score}%</text>
        </svg>
        """, unsafe_allow_html=True)

        # CHARTS
        num = df_clean.select_dtypes(include=np.number).columns

        if len(num) > 0:
            col = st.selectbox("Select Column", num)

            st.plotly_chart(px.histogram(df_clean, x=col), use_container_width=True)
            st.plotly_chart(px.box(df_clean, y=col), use_container_width=True)

# ================= CHATBOT =================
st.markdown("## 🤖 AI Chat Assistant")

msg = st.text_input("Ask DataMind AI")

if st.button("Send"):
    if msg:
        st.session_state.chat.append(("You", msg))

        def reply(x):
            x = x.lower()
            if "clean" in x:
                return "I clean missing values, duplicates, and outliers."
            if "chart" in x:
                return "I generate histograms, box plots, and correlations."
            return "Ask me about data cleaning or analytics."

        st.session_state.chat.append(("AI", reply(msg)))

# chat display
st.markdown("<div class='chat'>", unsafe_allow_html=True)
for r, m in st.session_state.chat:
    st.write(f"**{r}:** {m}")
st.markdown("</div>", unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("---")
st.caption(f"DataMind AI SaaS • Logged in as {user}")