import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def get_code_feedback(code_input, language="Python"):
    prompt = (
        f"You are a coding teacher. The student wrote this {language} code:\n\n"
        f"{code_input}\n\n"
        "Please explain any errors, suggest improvements, and explain your suggestions in a beginner-friendly way."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You provide friendly and accurate coding feedback."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
