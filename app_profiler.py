import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Profile Page")

# Collect basic information
name = "Koketso Monyethabene"
field = "Mathematical Sciences"
institution = "Sefako Makgatho Health Sciences University"

# Display basic profile information
st.header("Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="CV | Koketso Monyethabene",
    layout="centered"
)

# -----------------------------
# CUSTOM CSS (PINK + BUTTERFLIES)
# -----------------------------
st.markdown(
    """
    <style>
    body {
        background-color: #ffd1dc;
    }

    .stApp {
        background-color: #ffd1dc;
    }

    .butterfly {
        position: fixed;
        font-size: 30px;
        animation: float 12s infinite linear;
        opacity: 0.7;
    }

    .b1 { left: 10%; animation-delay: 0s; }
    .b2 { left: 30%; animation-delay: 3s; }
    .b3 { left: 55%; animation-delay: 6s; }
    .b4 { left: 75%; animation-delay: 9s; }

    @keyframes float {
        0%   { top: 110%; }
        100% { top: -10%; }
    }
    </style>

    <div class="butterfly b1">🦋</div>
    <div class="butterfly b2">🦋</div>
    <div class="butterfly b3">🦋</div>
    <div class="butterfly b4">🦋</div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# CV DATA
# -----------------------------
cv = {
    "name": "Koketso Monyethabene",
    "contact": "koketso.monyethabene@gmail.com",

    "profile": (
        "Analytical and detail-oriented Mathematics Honours graduate with a strong "
        "foundation in quantitative analysis, statistical modelling, and data-driven "
        "problem-solving. Experienced in applying regression, probability, and analytical "
        "techniques to interpret datasets and support evidence-based conclusions. "
        "Highly motivated to apply mathematical and analytical skills within a Group "
        "Finance environment."
    ),

    "education": [
        "BSc Honours in Mathematics – Sefako Makgatho Health Sciences University (2025)",
        "Maths Problem-Solving Course – Limina Education Services (2025)",
        "BSc in Physical Sciences – Sefako Makgatho Health Sciences University (2021–2024)"
    ],

    "skills": [
        "Teamwork",
        "Regression Analysis",
        "Probability Theory",
        "Critical Thinking",
        "Communication"
    ],

    "experience": [
        "Statistical Modelling Practice – Applied regression and probability models to datasets",
        "Student Assistant / Demonstrator – Academic support and quantitative tutorials"
    ]
}

# -----------------------------
# DISPLAY CV
# -----------------------------
st.markdown(f"## {cv['name']}")
st.markdown(f"**{cv['contact']}**")

st.divider()

st.markdown("### 👤 Profile")
st.write(cv["profile"])

st.markdown("### 🎓 Education")
for edu in cv["education"]:
    st.markdown(f"- {edu}")

st.markdown("### 🧠 Skills")
for skill in cv["skills"]:
    st.markdown(f"- {skill}")

st.markdown("### 💼 Experience")
for exp in cv["experience"]:
    st.markdown(f"- {exp}")

     


# Add a contact section
st.header("Contact Information")
email = "koketso.monyethabene@gmail.com"
st.write(f"You can reach {name} at {email}.")