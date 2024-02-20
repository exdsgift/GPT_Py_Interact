from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("OPENAI_API_KEY non è stato impostato nel file .env")

client = OpenAI(api_key=api_key)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": 'What is the capital of France?'}
  ]
)
print(completion.choices[0].message)