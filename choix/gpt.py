from openai import OpenAI
import os
from dotenv import load_dotenv
import emoji

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("La clé API OpenAI n'a pas été définie dans les variables d'environnement.")

client = OpenAI(api_key=api_key)

def appeler_api_chatgpt(question):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ton nom est désormais Géraldine. Tu es une assitante holographique qui à pour but de répondre aux questions. Veille à ce que t'es réponses ne dépassent JAMAIS plus de 500 mots. Au début de chaque réponse, tu écrira UN emoji résumant ta réponse. Si par exemple, je te demande la taille de la tour eiffel, tu commencera ta réponse par [🥖] ."},
            {"role": "user", "content": question}
        ]
    )
    return completion.choices[0].message.content



