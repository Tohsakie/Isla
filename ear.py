import speech_recognition as sr

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