from openai import OpenAI
from dotenv import load_dotenv
import models.recommendation as rec
import os
import json
import numpy as np
import pandas as pd

load_dotenv()

api_key = os.getenv("CHAT_GPT_API_KEY")
client = OpenAI(api_key=api_key)
num_datasets = 5

def generate_data():
    data = {
    'water_temperature': np.random.uniform(24, 32, num_datasets),
    'dissolved_Oxygen': np.random.uniform(2, 8, num_datasets),
    'dissolved_solids': np.random.uniform(75, 140, num_datasets),
    'ammonia_concentration': np.random.uniform(0, 0.7, num_datasets),
    'pH': np.random.uniform(5.5, 8.5, num_datasets),
    }
    df = pd.DataFrame(data)
    data_to_send = df.to_dict()
    return data_to_send

def askGPT(data):
    prompt = f"Hi GPT, you are an expert at crossmatching water quality parameters, reported fish mortalities, feed type and average reported weight for fish in an aquaculture system.\
        Analyse this data set provided and proffer status for feed efficiency, growth performance, water quality trends and fish health stress signals. Also, provide recommendations for improving\
        the growth curve and improving mortality risks. Here is the data: "
    dataset = generate_data()
    for k, v in data.__dict__.items():
        dataset[k] = v
    messages = []

    try:
        messages.append({"role": "system", "content": f"{prompt} {dataset}"})
        response = client.chat.completions.create(
                model="gpt-4",
                messages=messages
                )
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        recommendation = rec.Recommendation(recommendation_text=reply)
    except Exception as e:
        print(e)

    return recommendation.recommendation_text
