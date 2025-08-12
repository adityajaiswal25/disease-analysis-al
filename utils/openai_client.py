import os
from openai import OpenAI

def get_openai_client():
    """Initialize and return OpenAI client"""
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        # For development/testing - replace with your actual key
        api_key = os.getenv('OPENAI_API_KEY_DEV')
    
    if api_key:
        return OpenAI(api_key=api_key)
    else:
        print("Warning: OpenAI API key not found. Please set OPENAI_API_KEY environment variable.")
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
