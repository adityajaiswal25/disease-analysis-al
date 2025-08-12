import os
from openai import OpenAI
import streamlit as st

def get_openai_client():
    """Initialize and return OpenAI client with multiple fallback options"""
    
    api_key = None
    
    # Method 1: Try Streamlit secrets first
    if hasattr(st, 'secrets'):
        try:
            api_key = st.secrets.get("OPENAI_API_KEY")
        except:
            pass
    
    # Method 2: Try environment variable
    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")
    
    # Method 3: Try .env file
    if not api_key:
        try:
            from dotenv import load_dotenv
            load_dotenv()
            api_key = os.getenv("OPENAI_API_KEY")
        except ImportError:
            pass
    
    if api_key:
        return OpenAI(api_key=api_key)
    else:
        # Enhanced error message with clear instructions
        error_msg = """
        ❌ OpenAI API Key Not Found!
        
        To fix this, please:
        1. Get your API key from: https://platform.openai.com/api-keys
        2. Create a .env file in your project root with:
           OPENAI_API_KEY=your-actual-key-here
        3. Or set the environment variable:
           Windows: set OPENAI_API_KEY=your-key
           Linux/Mac: export OPENAI_API_KEY=your-key
        
        For Streamlit Cloud, add the key in Settings > Secrets
        """
        st.error(error_msg) if hasattr(st, 'error') else print(error_msg)
        return None

def try_parse_json(text):
    """Parse JSON from text response"""
    import json
    try:
        first_brace = text.find('{')
        last_brace = text.rfind('}')
        if first_brace == -1 or last_brace == -1:
            # Try array format
            first_bracket = text.find('[')
            last_bracket = text.rfind(']')
            if first_bracket != -1 and last_bracket != -1:
                json_str = text[first_bracket:last_bracket + 1]
                return json.loads(json_str)
            return None
        json_str = text[first_brace:last_brace + 1]
        return json.loads(json_str)
    except Exception:
        return None
