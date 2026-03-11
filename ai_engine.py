import ollama

MODEL = "phi3"

def ask_ai(prompt):

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )

    return response['message']['content']


def analyze_resume(resume):

    resume = resume[:1000]

    prompt = f"""
You are an expert recruiter.

Analyze this resume.

Return:

ATS Score
Strengths
Weaknesses
Missing Skills
Best Job Roles
Interview Questions

Resume:
{resume}
"""

    return ask_ai(prompt)


def resume_chat(resume, question):

    resume = resume[:1000]

    prompt = f"""
Use this resume to answer.

Resume:
{resume}

Question:
{question}
"""

    return ask_ai(prompt)