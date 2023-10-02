import speech_recognition as sr
import tts
import api

def enregistrer_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Parlez maintenant...")
        audio = r.record(source, duration=5)
        print("Enregistrement terminé.")
    return audio

def transcrire_audio(audio):
    r = sr.Recognizer()
    try:
        texte = r.recognize_google(audio, language="fr-FR")
        return texte
    except sr.UnknownValueError:
        print("Impossible de reconnaître le texte.")
    except sr.RequestError as e:
        print("Erreur lors de la demande au service de reconnaissance vocale : {0}".format(e))

def callback(recognizer, audio):                          # this is called from the background thread
    try:
        msg = recognizer.recognize_google(audio, language="fr-FR")

        if "la mère de grégor" in msg.lower():
            print(msg.lower().split("la mère de grégory ")[-1])
            
            reponse_chatgpt = api.appeler_api_chatgpt(texte_reconnu)
            print(reponse_chatgpt)
            tts.say(reponse_chatgpt)

            pass
    except LookupError:
        print("Oops! Didn't catch that")

def ecoute_background():
    r = sr.Recognizer()
    r.listen_in_background(sr.Microphone(), callback)