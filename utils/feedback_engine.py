import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def get_code_feedback(code_input, language="Python"):
    prompt = (
    f"You are a Python coding tutor reviewing this student input:\n\n"
    f"{code_input}\n\n"
    "Your response should be in the following markdown format:\n"
    "### ❌ Input Issue:\n"
    "- State if the code is invalid or has logical problems.\n\n"
    "### 🔍 What Went Wrong:\n"
    "- Explain the error briefly.\n\n"
    "### ✅ Try This Instead:\n"
    "```python\n<corrected code>\n```\n\n"
    "### 💡 Why This Works:\n"
    "- Give a beginner-friendly explanation.\n"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",  # use exact model version
            messages=[
                {"role": "system", "content": "You provide friendly and accurate coding feedback."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
