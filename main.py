# -*- coding: utf-8 -*-

import requests 
import json
import os

import time

from pygame import mixer
from gtts import gTTS
from io import BytesIO

with open('conf.json') as json_file:
    data = json.load(json_file)

API_KEY = data["keyAPI"]
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

def generate_chat_completion(messages, model="gpt-3.5-turbo", temperature=1, max_tokens= None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens
    
    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")
    

os.system('cls' if os.name == 'nt' else 'clear')


while True:

    text = input('>> ')

    messages = [
        {"role": "system", "content": "Tu es un assistant qui se nome ISLA et qui aide."},
        {"role": "user", "content": text}
    ]


    responseGPT = generate_chat_completion(messages)
    print(responseGPT)

    def speak(responseGPT):
        mp3_fp = BytesIO()
        tts = gTTS(responseGPT, lang='fr')
        tts.write_to_fp(mp3_fp)
        return mp3_fp

    mixer.init()
    sound = speak(responseGPT)
    sound.seek(0)
    mixer.music.load(sound)
    mixer.music.play()

    time.sleep(5)

