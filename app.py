import streamlit as st
from utils.feedback_engine import get_code_feedback

st.set_page_config(page_title='CodeMentorAI', layout='centered')

st.title("🧠 CodeMentorAI")
st.subheader("Your AI-Powered Coding Feedback Assistant")

language = st.selectbox("Choose Language", ["Python", "JavaScript", "Java"])
code_input = st.text_area("Paste your code here", height=300)

# Secret passphrase input
with st.expander("🔐 Unlock Feedback"):
    user_secret = st.text_input("Enter your access phrase", type="password")

if st.button("Get Feedback"):
    if user_secret != "Wingardium Leviosa":
        st.error("🚫 Invalid passphrase. Access denied.")
    elif code_input.strip() == "":
        st.warning("Please enter some code first.")
    else:
        with st.spinner("Analyzing your code..."):
            feedback = get_code_feedback(code_input, language)
            st.markdown(feedback)
