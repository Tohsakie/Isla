# from urllib import request
import os

from flask import Flask, jsonify, request
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import requests
import meteo
import pytest
import gpt

app = Flask(__name__)


def call_chat_gpt(question):
    return gpt.appeler_api_chatgpt(question)


def call_weather(city_name='Ales', country_code='fr'):
    return meteo.extract_weather_info(city_name, country_code)


def predict_api(sentence):
    name_file = "isla.h5"
    model = tf.keras.models.load_model(os.path.join(os.path.dirname(__file__), name_file), custom_objects={'Adam': tf.keras.optimizers.Adam})
    tokenizer = Tokenizer()
    max_sequence_length = 14
    etiquettes = ["meteo", "chatGPT"]
    sequence = tokenizer.texts_to_sequences([sentence])
    sequence = pad_sequences(sequence, maxlen=max_sequence_length, padding='post')
    prediction = model.predict(sequence)
    predicted_label_index = np.argmax(prediction)
    if 0 <= predicted_label_index < len(etiquettes):
        return etiquettes[predicted_label_index]
    else:
        return "chatGPT"


def ask(question):
    subject = predict_api(question)

    if subject == "meteo":
        return jsonify(call_weather())
    elif subject == "chatGPT":
        return call_chat_gpt(question)
    else:
        return "Je n'ai pas compris votre demande"


@app.route('/getresponse', methods=['POST'])
def getresponse():
    data = request.json
    sentence = data.get('sentence')
    response = ask(sentence)
    return jsonify({'response': response}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)


# TESTS
def test_call_weather():
    with pytest.raises(ValueError):
        call_weather(None)
        call_weather('Ales', None)

    result = call_weather()
    assert result['weather_main'] != None
    assert result['weather_description'] != None
    assert result['weather_icon'] != None
    assert result['temp_min'] != None
    assert result['temp_max'] != None
    assert result['city_name'] != None