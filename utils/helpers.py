import streamlit as st

def render_accuracy_bar(accuracy_percent):
    """Render a vertical accuracy bar"""
    bar_html = f"""
    <div style='text-align: center;'>
        <div style='width: 50px; height: 200px; background: #e0e0e0; border-radius: 10px; margin: 0 auto; position: relative; overflow: hidden;'>
            <div style='width: 100%; background: linear-gradient(180deg, #4B8BBE, #74b9ff); transition: height 1.5s ease; border-radius: 10px 10px 0 0; position: absolute; bottom: 0; height: {accuracy_percent}%;'></div>
        </div>
        <div style='margin-top: 8px; font-weight: bold;'>{accuracy_percent}% Accuracy</div>
    </div>
    """
    st.markdown(bar_html, unsafe_allow_html=True)

def setup_page_config(title):
    """Set up page configuration"""
    st.set_page_config(
        page_title=f"{title} - Disease Analysis",
        page_icon="🏥",
        layout="centered"
    )
    
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            [data-testid="stSidebar"] {display: none;}
        </style>
    """, unsafe_allow_html=True)

def add_navigation():
    """Add navigation back to home"""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("🏠 Back to Home"):
            st.switch_page("Home.py")
    st.markdown("---")
