import speech_recognition as sr
import api as api
import tts as tts
import os
import time

trigger_vocal = "géraldine"

os.system('cls' if os.name == 'nt' else 'clear')

def callback(recognizer, audio):
    try:
        msg = recognizer.recognize_google(audio, language="fr-FR")
        print("Écoute OK, Traitement...")

        if trigger_vocal in msg.lower():
            theTexte = msg.lower().split(f"{trigger_vocal} ")[-1]
            print(theTexte)
            reponse_chatgpt = api.ask(theTexte)
            #reponse_chatgpt = "Ceci est un test, voici vos paroles : " + theTexte

            print(reponse_chatgpt)
            tts.say(reponse_chatgpt)
            pass

    except LookupError:
        print("(!) Erreur de compréhension")

def ecoute_background():
    r = sr.Recognizer()
    r.listen_in_background(sr.Microphone(), callback)
    print("Écoute en cours...")




ecoute_background()

while True:
    time.sleep(0.1)
