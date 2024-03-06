import speech_recognition as sr
import tts as tts
import os
import time
import emoji
import pygame
from threading import Thread
import api
import re

pygame.init()

screen_width = 1280
screen_height = 720 
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

image_path = os.path.join(os.path.dirname(__file__), "image.png")
image = pygame.image.load(image_path)

image_width = 300  
image_height = 300 
image = pygame.transform.scale(image, (image_width, image_height))

imagePosition = [[50,350], [450,0], [900,350]]

trigger_vocal = "géraldine"

os.system('cls' if os.name == 'nt' else 'clear')


current_image = image

def callback(recognizer, audio):
    global current_image  
    try:
        msg = recognizer.recognize_google(audio, language="fr-FR")
        print("Écoute OK, Traitement...")

        if trigger_vocal in msg.lower():
            user_request = msg.lower().split(f"{trigger_vocal} ")[-1]

            response_chatgpt = api.ask(user_request, "fee18e97-a5c4-4d72-9bbc-24c5d2edd67a")

            if response_chatgpt:

                response_chatgpt = response_chatgpt['response']['response']
                contenu_entre_crochets = re.findall(r'\[(.*?)\]', response_chatgpt)

                if contenu_entre_crochets:
                    emoji = contenu_entre_crochets[0]
                else:
                    emoji = "❓"
                emoji = emoji_to_name(emoji)

                name_file = emoji_to_name(emoji).replace(":","") + "_3d.png"
                name_folder = name_to_folder(emoji_to_name(emoji))

                image_path = os.path.join(os.path.dirname(__file__), "assets", name_folder, "3D", name_file)
                print(image_path)
                current_image = pygame.image.load(image_path)
                current_image = pygame.transform.scale(current_image, (image_width, image_height))
                
                print(response_chatgpt)
                tts.say(response_chatgpt)
                pass

    except (LookupError, sr.UnknownValueError):
        print("(!) Erreur de compréhension")

def ecoute_background():
    r = sr.Recognizer()
    r.listen_in_background(sr.Microphone(), callback)
    print("Écoute en cours...")

def emoji_to_name(emoji_char):
    try:
        emoji_name = emoji.demojize(emoji_char)
        return emoji_name
    except Exception as e:
        print("Une erreur s'est produite lors de la conversion de l'emoji en nom :", e)
        return None

def name_to_folder(emoji_name):
    try:
        emoji_folder = emoji_name.replace(":","").replace("_", " ").capitalize()
        return emoji_folder
    except Exception as e:
        print("Une erreur s'est produite lors de la conversion du nom d'emoji en nom de dossier :", e)
        return None

# Lancer l'écoute en arrière-plan
ecoute_thread = Thread(target=ecoute_background)
ecoute_thread.daemon = True
ecoute_thread.start()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0)) 
    
    for idx, (x, y) in enumerate(imagePosition):
        if idx == 0:
            rotated_image = pygame.transform.rotate(current_image, 90)
        elif idx == 2:  
            rotated_image = pygame.transform.rotate(current_image, -90) 
        else:  
            rotated_image = pygame.transform.rotate(current_image, 0) 
        
        screen.blit(rotated_image, (x, y))

    pygame.display.flip()

# Quitter Pygame
pygame.quit()
