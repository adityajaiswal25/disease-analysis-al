import streamlit as st
from utils.openai_client import get_openai_client
from utils.helpers import setup_page_config, add_navigation

# Page configuration
setup_page_config("AI Health Chatbot")

# Page content
st.header("🧠 AI Health Chatbot")
st.write("Chat with our AI assistant for health advice, symptom analysis, and medical information.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat interface
st.markdown("### 💬 Chat with AI Health Assistant")

# Display chat history
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(f"**🧑 You:** {message['content']}")
    else:
        st.markdown(f"**🤖 Assistant:** {message['content']}")

# User input
user_input = st.text_area(
    "Type your message here...",
    placeholder="Ask about symptoms, treatments, medications, or general health advice...",
    height=100,
    key="user_input"
)

col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    if st.button("📤 Send", type="primary"):
        if user_input.strip():
            client = get_openai_client()
            if not client:
                st.error("OpenAI API key missing or invalid. Cannot perform AI chat.")
            else:
                # Add user message to history
                st.session_state.chat_history.append({"role": "user", "content": user_input})
                
                # Prepare messages for API
                messages = [
                    {"role": "system", "content": "You are a helpful healthcare assistant. Provide clear, accurate, and helpful health advice. Always remind users to consult with healthcare professionals for serious concerns."}
                ]
                messages.extend(st.session_state.chat_history)
                
                with st.spinner("AI is thinking..."):
                    try:
                        response = client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=messages,
                        )
                        answer = response.choices[0].message.content
                        
                        # Add AI response to history
                        st.session_state.chat_history.append({"role": "assistant", "content": answer})
                        
                        # Rerun to update display
                        st.rerun()
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

with col2:
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

with col3:
    if st.button("💾 Save Chat"):
        chat_text = "\n\n".join([f"{msg['role'].upper()}: {msg['content']}" for msg in st.session_state.chat_history])
        st.download_button(
            label="📥 Download",
            data=chat_text,
            file_name="health_chat.txt",
            mime="text/plain"
        )

st.info("💡 **Tips for better responses:**")
st.markdown("""
- Be specific about your symptoms
- Include duration and severity
- Mention any medications you're taking
- Ask one question at a time
""")

st.warning("⚠️ **Important:** This chatbot provides general health information and is not a substitute for professional medical advice.")
add_navigation()

