from flask import Flask, request, jsonify

app = Flask(__name__)

controller_db = '172.32.0.4:8081'
choix = '172.32.0.5:8082'

@app.route('/operate', methods=['POST'])
def operate():
    data = request.json
    user_id = data.get('user_id')
    sentence = data.get('request')

    if check_params(user_id, sentence):
        return jsonify({'error': 'Paramètres user_id et request requis'}), 400
    else:
        base_url = controller_db + "/token/"
        url = base_url + user_id
        token = request.get(url)
        if token.status_code == 200:
            params = {'sentence': sentence}
            url = choix + "/getresponse"
            response = request.post(url, data=params)
            if response.status_code == 200:
                return jsonify({'response': response.json()}), 200
        else:
            return jsonify({'error': 'Aucun token trouvé'}), 400


if __name__ == '__main__':
    app.run(host='localhost', port=8080)


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