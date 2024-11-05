from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("CHAT_GPT_API_KEY")
client = OpenAI(api_key=api_key)

def askGPT(data):
    prompt = f"Hi GPT, you are an expert at crossmatching water quality parameters, reported fish mortalities, feed type and average reported weight for fish in an aquaculture system.\
        Analyse this data set provided and proffer status for feed efficiency, growth performance, water quality trends and fish health stress signals. Also, provide recommendations for improving\
        the growth curve and improving mortality risks. Here is the data: "
    messages = []

    try:
        messages.append({"role": "system", "content": f"{prompt} {data}"})
        response = client.chat.completions.create(
                model="gpt-4",
                messages=messages
                )
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        print(e)
        return None
    return reply
