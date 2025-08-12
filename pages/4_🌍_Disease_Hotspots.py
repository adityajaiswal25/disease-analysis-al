import streamlit as st
import pandas as pd
import plotly.express as px
from utils.openai_client import get_openai_client, try_parse_json
from utils.helpers import setup_page_config, add_navigation

# Page configuration
setup_page_config("Disease Hotspots")

# Page content
st.header("🌍 Disease Hotspots & Statistics")
st.write("Get insights into disease trends and hotspots in your area with AI-powered analysis.")

# City input
city = st.text_input(
    "Enter your city name",
    placeholder="e.g., Mumbai, Delhi, Bangalore, Chennai...",
    help="Enter your city to get localized disease trend data"
)

if st.button("🗺️ Show Hotspot Data", type="primary"):
    if city.strip() == "":
        st.error("Please enter a city name.")
    else:
        client = get_openai_client()
        if not client:
            st.error("OpenAI API key missing or invalid. Cannot fetch AI data.")
        else:
            prompt = (
               
    f"You are a disease hotspot assistant. When given a city name, provide the following information as plain text (no tables, no JSON): "
    f"1. Common diseases currently reported or historically known in {city} "
    f"2. Short description of each disease "
    f"3. Recommended prevention measures for each disease "
    f"4. Names and contacts of major hospitals in the area "
    f"5. Seasonal or weather-related health risks. "
    f"Rules: - If active case numbers are not available, skip that part and still give the other details. "
    f"- Use only verified or generally accepted health knowledge — do not invent new diseases. "
    f"- Always give the most relevant and useful information for the city. "
    f"- Format neatly with headings and bullet points for readability."
)



            
            
            messages = [
                {"role": "system", "content": "You are a knowledgeable healthcare assistant."},
                {"role": "user", "content": prompt},
            ]
            
            with st.spinner(f"Fetching disease data for {city}..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=messages,
                    )
                    answer = response.choices[0].message.content
                    st.markdown(answer)
                    
                    # if data and isinstance(data, list):
                    #     # Create DataFrame
                    #     df = pd.DataFrame(data)
                        
                    #     # Ensure required columns exist
                    #     required_cols = ['disease', 'cases', 'description', 'prevention', 'severity']
                    #     missing_cols = [col for col in required_cols if col not in df.columns]
                        
                    #     if missing_cols:
                    #         st.error(f"Missing required data: {missing_cols}")
                    #         st.text("Raw response:")
                    #         st.text(answer)
                    #     else:
                    #         # Display results
                    #         st.subheader(f"📊 Disease Trends in {city}")
                            
                    #         # Create bar chart
                    #         fig = px.bar(
                    #             df, 
                    #             x='disease', 
                    #             y='cases', 
                    #             title=f'Disease Cases in {city}',
                    #             color='severity',
                    #             labels={'cases': 'Number of Cases', 'disease': 'Disease'},
                    #             color_discrete_map={'Low': 'green', 'Medium': 'orange', 'High': 'red'}
                    #         )
                    #         st.plotly_chart(fig, use_container_width=True)
                            
                    #         # Display table
                    #         st.subheader("📋 Detailed Disease Information")
                            
                    #         # Create styled table
                    #         for _, row in df.iterrows():
                    #             st.markdown(f"""
                    #             <div style='padding: 15px; margin: 10px 0; border-left: 4px solid {"#ff6b6b" if row["severity"] == "High" else "#ffa726" if row["severity"] == "Medium" else "#4caf50"}; background-color: #f8f9fa;'>
                    #                 <h4>{row['disease']} ({row['cases']} cases)</h4>
                    #                 <p><strong>Severity:</strong> {row['severity']}</p>
                    #                 <p><strong>Description:</strong> {row['description']}</p>
                    #                 <p><strong>Prevention:</strong> {row['prevention']}</p>
                    #             </div>
                    #             """, unsafe_allow_html=True)
                            
                    #         # Summary statistics
                    #         total_cases = df['cases'].sum()
                    #         st.subheader("📈 Summary Statistics")
                    #         col1, col2, col3 = st.columns(3)
                    #         with col1:
                    #             st.metric("Total Cases", total_cases)
                    #         with col2:
                    #             st.metric("Diseases Tracked", len(df))
                    #         with col3:
                    #             high_severity = len(df[df['severity'] == 'High'])
                    #             st.metric("High Severity", high_severity)
                                
                    # else:
                    #     st.error("Failed to parse AI response. Please try again.")
                    #     st.text("Raw response:")
                    #     st.text(answer)
                        
                except Exception as e:
                    st.error(f"Error fetching data: {str(e)}")

# Additional features
st.markdown("---")
st.markdown("### 📍 Additional Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='padding: 15px; text-align: center;'>
        <h4>🌡️ Temperature Check</h4>
        <p>Monitor weather-related disease patterns</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='padding: 15px; text-align: center;'>
        <h4>🦠 Seasonal Trends</h4>
        <p>Track seasonal disease outbreaks</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='padding: 15px; text-align: center;'>
        <h4>🏥 Healthcare Access</h4>
        <p>Find nearby hospitals and clinics</p>
    </div>
    """, unsafe_allow_html=True)
add_navigation()

