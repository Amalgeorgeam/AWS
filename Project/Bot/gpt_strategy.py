
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_market_input(human_text):
    prompt = f"""
You are an options trading assistant. Analyze the input and return one trading decision as JSON with action, symbol, strike_price, option_type (CALL or PUT), and reason.

Example:
Input: Market sentiment shows bullish trend in NIFTY, resistance broken at 24000.
Output:
{{
    "action": "BUY",
    "symbol": "NIFTY",
    "strike_price": 24000,
    "option_type": "CALL",
    "reason": "Bullish sentiment with resistance breakout"
}}

Input: {human_text}
Output:
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    import json
    try:
        result = json.loads(response.choices[0].message["content"])
        return result
    except:
        return {"error": "Invalid GPT response"}
