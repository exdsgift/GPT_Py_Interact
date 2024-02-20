from openai import OpenAI
from dotenv import load_dotenv
import os

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Recupera l'API key da una variabile d'ambiente
api_key = os.getenv("OPENAI_API_KEY")

# Assicurati che l'API key sia stata correttamente recuperata
if api_key is None:
    raise ValueError("OPENAI_API_KEY non è stato impostato nel file .env")

# Utilizza l'API key per creare un'istanza del client OpenAI
client = OpenAI(api_key=api_key)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": 'What is the capital of France?'}
  ]
)
print(completion.choices[0].message)