import streamlit as st
from utils.openai_client import get_openai_client, try_parse_json
from utils.helpers import render_accuracy_bar, setup_page_config, add_navigation

# Page configuration
setup_page_config("Test Report-Based Prediction")

# Page content
st.header("📊 Test Report-Based Disease Prediction")
st.write("Upload your test reports or enter test values to get AI-powered disease predictions.")

# Test report input
col1, col2 = st.columns(2)

with col1:
    blood_sugar = st.slider("Blood Sugar (mg/dL)", 0.0, 500.0, 100.0, 0.1)
    blood_pressure = st.slider("Blood Pressure (mm Hg)", 0.0, 200.0, 90.0, 0.1)

with col2:
    cholesterol = st.slider("Cholesterol (mg/dL)", 0.0, 400.0, 180.0, 0.1)
    hemoglobin = st.slider("Hemoglobin (g/dL)", 0.0, 20.0, 12.0, 0.1)

# Disease selection
disease_options = ["Diabetes", "Hypertension", "Cholesterol Issues", "Heart Disease", "Anemia"]
selected_disease = st.selectbox("Select Disease for Prediction", disease_options)

if st.button("📈 Analyze Report", type="primary"):
    client = get_openai_client()
    if not client:
        st.error("OpenAI API key missing or invalid. Cannot perform AI prediction.")
    else:
        prompt = (
            "You are a helpful healthcare assistant.\n"
            f"Given these test values:\n"
            f"Blood Sugar: {blood_sugar} mg/dL\n"
            f"Blood Pressure: {blood_pressure} mm Hg\n"
            f"Cholesterol: {cholesterol} mg/dL\n"
            f"Hemoglobin: {hemoglobin} g/dL\n"
            f"Predict if the patient has {selected_disease} and provide:\n"
            "  confidence (0-100), treatment_plan, lifestyle_changes, follow_up_tests\n"
            "Respond ONLY with JSON."
        )
        
        messages = [
            {"role": "system", "content": "You are a helpful healthcare assistant."},
            {"role": "user", "content": prompt},
        ]
        
        with st.spinner("Analyzing test report with AI..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=messages,
                )
                answer = response.choices[0].message.content
                data = try_parse_json(answer)
                
                if data:
                    confidence = data.get("confidence", 0)
                    treatment = data.get("treatment_plan", "N/A")
                    lifestyle = data.get("lifestyle_changes", "N/A")
                    follow_up = data.get("follow_up_tests", "N/A")
                    
                    st.subheader(f"📊 Analysis Results for {selected_disease}")
                    render_accuracy_bar(confidence)
                    
                    st.markdown("**Treatment Plan:**")
                    st.write(treatment)
                    
                    st.markdown("**Lifestyle Changes:**")
                    st.write(lifestyle)
                    
                    st.markdown("**Follow-up Tests:**")
                    st.write(follow_up)
                    
                else:
                    st.error("Failed to parse AI response.")
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")

st.info("💡 **Tip:** These values are typical ranges for healthy adults. Consult your doctor for personalized ranges.")

add_navigation()
