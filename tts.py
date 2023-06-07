from playsound import playsound
from gtts import gTTS
import os

def say(text):
    text = text
    tts = gTTS(text=text, lang='fr')
    tts.save("say.mp3")
    audio_file = os.path.dirname(__file__) + '\\say.mp3'
    playsound(audio_file)
