import ollama

def ask_resume_rag(resume, question):

    prompt = f"""
You are a career assistant.

Use the following resume information to answer the question.

Resume:
{resume}

Question:
{question}
"""

    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']