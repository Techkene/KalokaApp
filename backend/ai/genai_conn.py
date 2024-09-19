from openai import OpenAI
from dotenv import load_dotenv
import models.recommendation as rec
import os

load_dotenv()

api_key = os.getenv("CHAT_GPT_API_KEY")
client = OpenAI(api_key=api_key)

def askGPT(line):
    prefix = f"Hi GPT, You are an Expert in Agro Allied Businesses. Analyse this data and profer recommendations to improve the quality of the products from this farm. Here's the Data: {line}"
    messages = []

    messages.append({"role": "system", "content": prefix})
    response = client.chat.completions.create(
            model="gpt-4",
            messages=messages
            )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    recommendation = rec.Recommendation(recommendation_text=reply)
    print(recommendation.recommendation_text)
    return recommendation.recommendation_text
