import ear
import api
import tts
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')

ear.ecoute_background()

while True:

    """audio = ear.enregistrer_audio()
    texte_reconnu = ear.transcrire_audio(audio)
    print(texte_reconnu)"""

    time.sleep(0.1)
    """reponse_chatgpt = api.appeler_api_chatgpt(texte_reconnu)
    print(reponse_chatgpt)
    tts.say(reponse_chatgpt)"""
