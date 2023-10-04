import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import requests

def predict_api(sentence):
    model = tf.keras.models.load_model("isla.h5", custom_objects={'Adam': tf.keras.optimizers.Adam})
    tokenizer = Tokenizer()
    max_sequence_length = 14
    etiquettes = ["meteo", "chatGPT", "news", "domotique"]
    sequence = tokenizer.texts_to_sequences([sentence])
    sequence = pad_sequences(sequence, maxlen=max_sequence_length, padding='post')
    prediction = model.predict(sequence)
    predicted_label_index = np.argmax(prediction)
    return etiquettes[predicted_label_index]


def ask(reponse):
    api = predict_api(reponse)

    # Force l'api chat gpt
    api = "chatGPT"

    print("api.py/ask --> API {}".format(api))

    if api == "meteo":
        return callMeteo(reponse)
    elif api == "chatGPT":
        return callChatGPT(reponse)
    elif api == "news":
        return callNews(reponse)
    elif api == "domotique":
        return callDomotique(reponse)
    else:
        return "Je n'ai pas compris votre demande"
    


def send_api(user_id, phrase, action):

    api_url = 'http://localhost:8080/sendapi' 

    data = {
        'user_id': user_id,
        'phrase': phrase,
        'action': action
    }

    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        result = response.json()
        return result['message']
    elif response.status_code == 400:
        return 'Erreur: Paramètres user_id, phrase et action requis'
    elif response.status_code == 403:
        return 'Erreur: Token invalide ou crédits épuisés'
    else:
        return 'Erreur inattendue'    

# # # # # # # # FONCTIONS API # # # # # # # #


def callMeteo(ville):
    return 0

def callDomotique(ville):
    return 0

def callNews(ville):
    return 0

def callChatGPT(question):
    user_id = 'dc92bf38-cce2-4f32-8fe3-b52806f8c352'
    phrase = 'Comment va tu ?'
    action = 'chatGPT'
    return send_api(user_id, phrase, action)

