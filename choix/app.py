from urllib import request
from flask import Flask, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import requests

app = Flask(__name__)


def call_chat_gpt(question):
    return "chatgpt"


def call_weather():
    return "weather"


def call_news():
    return "news"


def predict_api(sentence):
    model = tf.keras.models.load_model("isla.h5", custom_objects={'Adam': tf.keras.optimizers.Adam})
    tokenizer = Tokenizer()
    max_sequence_length = 14
    etiquettes = ["meteo", "chatGPT", "news"]
    sequence = tokenizer.texts_to_sequences([sentence])
    sequence = pad_sequences(sequence, maxlen=max_sequence_length, padding='post')
    prediction = model.predict(sequence)
    predicted_label_index = np.argmax(prediction)
    return etiquettes[predicted_label_index]


def ask(question):
    subject = predict_api(question)

    if subject == "meteo":
        return call_weather()
    elif subject == "chatGPT":
        return call_chat_gpt(question)
    elif subject == "news":
        return call_news()
    else:
        return "Je n'ai pas compris votre demande"


@app.route('/getresponse', methods=['POST'])
def getresponse():
    data = request.json
    sentence = data.get('sentence')
    response = ask(sentence)
    return jsonify({'response': response}), 200


if __name__ == '__main__':
    app.run(host='localhost', port=8082)
