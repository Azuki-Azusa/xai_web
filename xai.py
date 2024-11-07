import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

XAI_API_KEY = os.getenv("XAI_API_KEY")
client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)

def chat(messages: list[dict]):
    if len(messages) > 10:
        messages = messages[-10:]
    else:
        messages = messages
        
    completion = client.chat.completions.create(
        model="grok-beta",
        messages=messages,
    )

    print(completion.choices[0].message.content)

    return completion.choices[0].message.content

