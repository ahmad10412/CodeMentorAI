import streamlit as st
from utils.feedback_engine import get_code_feedback

# Apply custom styles
def apply_custom_styles():
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                color: white;
                font-family: 'Segoe UI', sans-serif;
            }

            h1 {
                color: #FFDE59 !important;
                font-size: 2.8rem;
                font-weight: 700;
            }

            .stSubheader {
                color: #F8F8F8 !important;
            }

            textarea {
                background-color: #f7f7f7 !important;
                color: #000 !important;
                border-radius: 8px;
                padding: 12px;
                font-size: 1rem;
            }

            div.stButton > button {
                background-color: #FF6F61;
                color: white;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                transition: 0.3s;
            }

            div.stButton > button:hover {
                background-color: #E85D54;
            }

            .st-expanderHeader {
                font-weight: 600;
                color: #FFD700;
            }

            .stMarkdown {
                font-size: 1.1rem;
            }

            .stTextInput input {
                background-color: #ffffff;
                color: #000000;
            }

            .stSelectbox div[role="button"] {
                background-color: #ffffff !important;
                color: #000 !important;
                border-radius: 5px;
            }
        </style>
    """, unsafe_allow_html=True)

# Apply the styles
apply_custom_styles()

# App header
st.markdown("<h1 style='text-align: center;'>🧠 CodeMentorAI</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color:#dfe6e9;'>AI-Powered Feedback for Future Coders</h4>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<p style='text-align: center; color:#f1c40f; font-size: 1.2rem;'>Every great coder once started with <code>Hello, World!</code></p>", unsafe_allow_html=True)

# UI Elements
language = st.selectbox("Choose Language", ["Python", "JavaScript", "Java"])
code_input = st.text_area("Paste your code here", height=300)

# Secret passphrase input
with st.expander("🔐 Unlock Feedback"):
    user_secret = st.text_input("Enter your access phrase", type="password")

# Feedback button
if st.button("Get Feedback"):
    if user_secret.strip() != "Wingardium Leviosa":
        st.error("🚫 Invalid passphrase. Access denied.")
    elif code_input.strip() == "":
        st.warning("Please enter some code first.")
    else:
        with st.spinner("Analyzing your code..."):
            feedback = get_code_feedback(code_input, language)
            st.markdown(feedback)
