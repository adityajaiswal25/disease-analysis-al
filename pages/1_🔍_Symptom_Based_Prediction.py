import streamlit as st
from utils.openai_client import get_openai_client, try_parse_json
from utils.helpers import render_accuracy_bar, setup_page_config

# Page configuration
setup_page_config("Symptom-Based Prediction")

from utils.helpers import add_navigation

# Page content
st.header("🔍 Symptom-Based Disease Prediction")
st.write("Enter your symptoms and get AI-powered disease predictions with treatment recommendations.")

# Symptom input
symptoms = st.text_area(
    "Describe your symptoms",
    placeholder="e.g., fever, headache, cough, fatigue, chest pain...",
    height=100
)

if st.button("🔮 Predict Disease", type="primary"):
    if symptoms.strip() == "":
        st.error("Please enter some symptoms to predict.")
    else:
        client = get_openai_client()
        if not client:
            st.error("OpenAI API key missing or invalid. Cannot perform AI prediction.")
        else:
            prompt = (
                "You are a helpful healthcare assistant.\n"
                f"Given these symptoms: {symptoms}\n"
                "Respond ONLY with a JSON object containing:\n"
                "  disease (string), accuracy (number, 0-100),\n"
                "  doctor_consultation (string), hospital_info (string), "
                "  preventive_measures (string), severity (string).\n"
                "No additional text."
            )
            
            messages = [
                {"role": "system", "content": "You are a helpful healthcare assistant."},
                {"role": "user", "content": prompt},
            ]
            
            with st.spinner("Analyzing symptoms with AI..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=messages,
                    )
                    answer = response.choices[0].message.content
                    data = try_parse_json(answer)
                    
                    if data:
                        col1, col2 = st.columns([2, 1])
                        
                        with col1:
                            st.subheader(f"🩺 Predicted Disease: {data.get('disease', 'N/A')}")
                            st.write(f"**Severity:** {data.get('severity', 'N/A')}")
                            st.write(f"**Recommended Doctor:** {data.get('doctor_consultation', 'N/A')}")
                            st.write(f"**Hospital Information:** {data.get('hospital_info', 'N/A')}")
                            st.write(f"**Preventive Measures:** {data.get('preventive_measures', 'N/A')}")
                        
                        with col2:
                            accuracy = data.get('accuracy', 0)
                            render_accuracy_bar(accuracy)
                    
                except Exception as e:
                    st.error("Error fetching AI response.")
                    st.error(str(e))

st.info("💡 **Tip:** Be as specific as possible with your symptoms for better predictions")
st.warning("⚠️ **Disclaimer:** This prediction is for informational purposes only and should not replace professional medical advice.")

add_navigation()
