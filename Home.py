import streamlit as st
from utils.helpers import setup_page_config

# Page configuration
setup_page_config("Home")

# Initialize session state for navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# # Hide sidebar navigation
st.markdown("""
    <style>
        [data-testid="stSidebar"] { display: none; }
        
        .stButton > button {
            width: 100%;
            height: 150px;
            border-radius: 15px;
            border: 1px solid #ddd;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-size: 16px;
            font-weight: bold;
            white-space: pre-line;
            line-height: 1.4;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        }
    </style>
""", unsafe_allow_html=True)



# Main page content
st.markdown("""
<div style='text-align: center; padding-top: 30px;'>
    <h1 style='color: #4B8BBE;'>🏥 Disease Analysis Using AI & ML</h1>
    <p style='font-size: 20px; color: #666; margin-bottom: 30px;'>
        Advanced AI-powered disease prediction and health analysis
    </p>
</div>
""", unsafe_allow_html=True)

# Create clickable feature cards
col1, col2 = st.columns(2)

with col1:
    if st.button("🔍\n Symptom-Based Prediction"):
        st.switch_page("pages/1_🔍_Symptom_Based_Prediction.py")
    
    if st.button("🧠\nAI Health Chatbot\n"):
        st.switch_page("pages/3_🧠_AI_Health_Chatbot.py")

with col2:
    if st.button("📊\nTest Report Analysis\n"):
        st.switch_page("pages/2_📊_Test_Report_Based_Prediction.py")
    
    if st.button("🌍\nDisease Hotspots\n"):
        st.switch_page("pages/4_🌍_Disease_Hotspots.py")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 14px;'>
    <p>⚠️ This tool provides health information and is not a substitute for professional medical advice</p>
</div>
""" , unsafe_allow_html=True)
