import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from resume_parser import extract_text
from ai_engine import analyze_resume, resume_chat
from job_matcher import match_resume_job
from rag_engine import ask_resume_rag

st.set_page_config(
    page_title="AI Career Coach",
    page_icon="🤖",
    layout="wide"
)

# ---------- SIDEBAR ----------

st.sidebar.title("🤖 AI Career Coach")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Resume Analyzer",
        "Interview Trainer",
        "Resume Chatbot",
        "Resume Knowledge AI"
    ]
)

st.sidebar.success("AI Powered Career Assistant")

# ---------- HEADER ----------

st.markdown("""
<h1 style='text-align:center;
font-size:55px;
background: linear-gradient(90deg,#00c6ff,#0072ff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;'>
🤖 AI Career Coach
</h1>
""", unsafe_allow_html=True)

st.markdown(
"<p style='text-align:center;color:gray;'>AI Resume Analyzer • Interview Trainer • Job Advisor</p>",
unsafe_allow_html=True
)

st.divider()

# =====================================
# RESUME ANALYZER
# =====================================

if menu == "Resume Analyzer":

    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    if uploaded_file:

        resume_text = extract_text(uploaded_file)
        resume_text = resume_text[:1000]

        st.success("Resume uploaded successfully")

        col1, col2, col3 = st.columns(3)

        col1.metric("ATS Score", "78%", "+10%")
        col2.metric("Skill Match", "72%", "+6%")
        col3.metric("Job Fit", "High")

        st.divider()

        # ---------- SKILL BAR CHART ----------

        skills = {
            "Python": 85,
            "Machine Learning": 70,
            "SQL": 65,
            "Communication": 75,
            "Data Structures": 60
        }

        df = pd.DataFrame({
            "Skill": skills.keys(),
            "Score": skills.values()
        })

        fig = px.bar(df, x="Skill", y="Score", color="Score")

        st.subheader("📊 Skill Strength")

        st.plotly_chart(fig, use_container_width=True)

        # ---------- RADAR CHART ----------

        radar = go.Figure()

        radar.add_trace(go.Scatterpolar(
            r=list(skills.values()),
            theta=list(skills.keys()),
            fill='toself'
        ))

        radar.update_layout(
            polar=dict(radialaxis=dict(visible=True))
        )

        st.subheader("📡 Skill Radar")

        st.plotly_chart(radar)

        st.divider()

        # ---------- AI ANALYSIS ----------

        if st.button("🚀 Analyze Resume"):

            with st.spinner("Analyzing resume..."):

                result = analyze_resume(resume_text)

            st.subheader("📄 Resume Analysis")

            st.write(result)

        st.divider()

        # ---------- JOB MATCH ----------

        st.subheader("📄 Resume vs Job Description")

        job_description = st.text_area("Paste Job Description")

        if job_description:

            score, matched = match_resume_job(resume_text, job_description)

            st.metric("Job Match Score", f"{score}%")

            st.write("### Matched Keywords")

            st.write(list(matched))

# =====================================
# INTERVIEW TRAINER
# =====================================

if menu == "Interview Trainer":

    st.subheader("🎤 AI Interview Trainer")

    question = st.text_input("Ask interview question")

    if question:

        with st.spinner("Generating answer..."):

            answer = analyze_resume(question)

        st.write(answer)

# =====================================
# SIMPLE RESUME CHATBOT
# =====================================

if menu == "Resume Chatbot":

    st.subheader("🤖 Resume Chatbot")

    question = st.text_input("Ask anything about your resume")

    if question:

        with st.spinner("Thinking..."):

            reply = resume_chat("", question)

        st.write(reply)

# =====================================
# RAG RESUME KNOWLEDGE AI
# =====================================

if menu == "Resume Knowledge AI":

    st.subheader("🧠 Resume Knowledge Assistant")

    uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

    if uploaded_file:

        resume_text = extract_text(uploaded_file)

        question = st.text_input("Ask questions about the resume")

        if question:

            answer = ask_resume_rag(resume_text, question)

            st.write(answer)