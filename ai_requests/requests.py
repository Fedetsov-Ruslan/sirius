from openai import OpenAI
from fastapi import requests

from config import AI_TOKEN

client = OpenAI(api_key=AI_TOKEN)


def ask_requests(client: OpenAI, question: str) -> str:
    response = client.chat.completions.create(
        model= "gpt-4o-mini",
        messages=question,
        temperature=0.7,
        max_tokens=1600
    )
    return response.choices[0].message.content


    
    

