import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

genai.configure(api_key=GEMINI_API_KEY)

async def process_query(query: str):
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    
    system_prompt = """
You are an expert financial assistant.
Your task is to analyze the user's question.
1. First, determine if the user is asking about investing in, buying, or the price of gold.
2. If they are, respond with a short, interesting fact about gold. Then, gently nudge them to invest by asking if they'd like to purchase digital gold. Your response MUST end with the JSON object: {"action": "PROMPT_PURCHASE"}.
3. If the question is NOT about gold investment, provide a normal helpful answer to the query. Your response MUST end with the JSON object: {"action": "REJECT"}.

User Query: {user_query_goes_here}
"""

    
    full_prompt = system_prompt.replace("{user_query_goes_here}", query)
    
    response = await model.generate_content_async(full_prompt)
    
    response_text = response.text
    
    # Attempt to parse the action JSON from the end of the response
    action = "UNKNOWN"
    try:
        # Find the last occurrence of a JSON object
        json_start = response_text.rfind('{')
        if json_start != -1:
            json_str = response_text[json_start:]
            parsed_json = json.loads(json_str)
            if "action" in parsed_json:
                action = parsed_json["action"]
                response_text = response_text[:json_start].strip() # Remove JSON from text
    except json.JSONDecodeError:
        pass # If parsing fails, action remains UNKNOWN or default

    return response_text, action