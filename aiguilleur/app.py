import json

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

controller_db = 'http://172.32.0.4:8081'
choix = 'http://172.32.0.5:8082'


def check_params(user_id, sentence):
    return not user_id or not sentence


# TEST
def test_check_params():
    assert check_params('fee18e97-a5c4-4d72-9bbc-24c5d2edd67a', 'Coucou, comment vas-tu ?') == False
    assert check_params('fee18e97-a5c4-4d72-9bbc-24c5d2edd67a', '') == True
    assert check_params('', 'Coucou, comment vas-tu ?') == True
    assert check_params('', '') == True
    assert check_params(None, None) == True
    assert check_params(None, 'Coucou, comment vas-tu ?') == True
    assert check_params('fee18e97-a5c4-4d72-9bbc-24c5d2edd67a', None) == True


@app.route('/operate', methods=['POST'])
def operate():
    data = request.json
    user_id = data.get('user_id')
    sentence = data.get('request')

    if check_params(user_id, sentence):
        return jsonify({'error': 'Paramètres user_id et request requis'}), 400
    else:
        nb_token = 0
        url = controller_db + "/token/" + user_id
        payload = {}
        headers = {
            'api_key': '2aacc7b2-d05b-4ade-9f83-5c654e0a602f'
        }
        token = requests.request("GET", url, headers=headers, data=payload)
        token_response = token.json()
        if token_response:
            first_item = token_response[0]
            nb_token = first_item.get('credit')

        if token.status_code == 200 and nb_token > 0:
            url = choix + "/getresponse"
            payload = json.dumps({
                "sentence": sentence
            })
            headers = {
                'Content-Type': 'application/json',
                'api_key': '2aacc7b2-d05b-4ade-9f83-5c654e0a602f'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            if response.status_code == 200:
                return jsonify({'response': response.json()}), 200
            else:
                return jsonify({'error': 'Erreur lors de la requête vers choix'}), 500
        else:
            return jsonify({'error': 'Aucun token trouvé ou nombre de jetons insuffisant'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
