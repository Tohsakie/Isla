from playsound import playsound
from gtts import gTTS
import os

def say(text):
    text = text
    tts = gTTS(text=text, lang='fr')
    tts.save("say.mp3")
    playsound("say.mp3", True)
    os.remove("say.mp3")
