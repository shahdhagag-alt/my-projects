import os
import streamlit as st

st.set_page_config(page_title="Shahd | Portfolio", page_icon="👩‍💻", layout="centered")

NAME = "Shahd Hagag"
TITLE = "Data Science Student | Alexandria University"
BIO = (
    "Fourth-year Data Science student at the Faculty of Computers and Data Science, "
    "Alexandria University."
)
PHOTO = "photo.jpeg"  
SKILLS = ["Python", "Pandas", "Scikit-learn", "SQL", "Power BI", "Streamlit"]
LINKS = {
    "GitHub": "https://github.com/shahdhagag-alt",
    "LinkedIn": "https://www.linkedin.com/in/shahd-hagag-92a3a1328/",
}
PROJECTS = [
    {
        "title": "Customer Personality Analytics & Campaign Response Prediction",
        "desc": "Data Analytics and Machine Learning project that solves a real marketing targeting problem.",
        "tech": ["Python", "Scikit-learn", "Pandas", "Matplotlib", "Seaborn", "Power BI"],
        "link": "https://github.com/shahdhagag-alt/customer-personality-analytics-and-prediction",
    },
    {
        "title": "Credit Card Default Prediction",
        "desc": "ML model to predict credit card default on a 30,000-client dataset.",
        "tech": ["Python", "Scikit-learn", "Pandas"],
    },
    {
        "title": "Car & Motorcycle Preferences Survey",
        "desc": "Team project analyzing survey data about car and motorcycle preferences.",
        "tech": ["Python", "Pandas", "Matplotlib"],
    },
]
# ==================================

# Header
col1, col2 = st.columns([1, 2], vertical_alignment="center")
with col1:
    if os.path.exists(PHOTO):
        st.image(PHOTO, use_container_width=True)
    else:
        st.info("photo.jpg")
with col2:
    st.title(NAME)
    st.subheader(TITLE)
    st.write(BIO)

st.divider()

# Skills
st.header("Skills")
st.write(" • ".join(SKILLS))

st.divider()

# Projects
st.header("Projects")
for p in PROJECTS:
    with st.container(border=True):
        st.subheader(p["title"])
        st.write(p["desc"])
        st.caption("Tech: " + ", ".join(p["tech"]))
        if p.get("link"):
            st.link_button("View project", p["link"])

st.divider()

# Contact
st.header("Contact")
cols = st.columns(len(LINKS))
for c, (label, url) in zip(cols, LINKS.items()):
    c.link_button(label, url)
