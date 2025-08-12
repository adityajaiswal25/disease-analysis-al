# Disease Analysis Using AI & ML - Multi-Page Application

A comprehensive AI-powered disease analysis application with separate pages for different health analysis features.

> **👨‍💻 Developed & Designed by [Aditya Jaiswal](https://www.linkedin.com/in/adityajaiswal25)**  
> *Final Year B.Tech (CSAI) | Python Developer | Cloud Computing Enthusiast | Noida, India*



## 🚀 Features

- **🔍 Symptom-Based Prediction** - Get disease predictions based on symptoms
- **📊 Test Report Analysis** - Analyze medical test reports for disease predictions  
- **🧠 AI Health Chatbot** - Chat with AI for health advice and information
- **🌍 Disease Hotspots** - View disease trends and statistics for your area

## 📁 Project Structure

```
disease-analysis-app/
├── Home.py                 # Main landing page
├── pages/
│   ├── 1_🔍_Symptom_Based_Prediction.py
│   ├── 2_📊_Test_Report_Based_Prediction.py
│   ├── 3_🧠_AI_Health_Chatbot.py
│   ├── 4_🌍_Disease_Hotspots.py
│   └── 5_ℹ️_About.py
├── utils/
│   ├── __init__.py
│   ├── openai_client.py    # OpenAI client utilities
│   └── helpers.py          # Shared helper functions
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🛠️ Installation & Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the application:**
```bash
streamlit run Home.py
```

3. **Access the application:**
- Open your browser to `http://localhost:8501`
- Use the sidebar navigation to access different features

## 🎯 Usage Guide

### Symptom-Based Prediction
- Enter symptoms separated by commas
- Get disease predictions with accuracy percentages
- Receive doctor recommendations and preventive measures

### Test Report Analysis  
- Input test values (blood sugar, pressure, cholesterol, etc.)
- Select the disease to analyze for
- Get confidence scores and treatment recommendations

### AI Health Chatbot
- Ask any health-related questions
- Get instant AI responses
- Save chat history for reference

### Disease Hotspots
- Enter your city name
- View disease trends and statistics
- See interactive charts and maps

## ⚠️ Important Disclaimers

- This tool provides **health information only** and is **not a substitute** for professional medical advice
- Always **consult healthcare professionals** for serious medical concerns
- **Emergency situations** should be handled by calling emergency services
- **Medication advice** should be verified with licensed physicians

## 🔧 Technical Details

- **Framework:** Streamlit
- **AI Provider:** OpenAI GPT-4o-mini
- **Data Visualization:** Plotly, Pandas
- **Styling:** Custom CSS with responsive design

## 🚀 Quick Start

1. Ensure Python 3.7+ is installed
2. Install requirements: `pip install -r requirements.txt`
3. Run: `streamlit run Home.py`
4. Navigate using the sidebar menu

## 📞 Support

For issues or questions:
- Check the console for error messages
- Ensure all dependencies are installed
- Verify OpenAI API key is valid
