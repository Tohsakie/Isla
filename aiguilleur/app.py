from flask import Flask, request, jsonify

app = Flask(__name__)

controller_db = '0.0.0.0:8080'
choix = '0.0.0.0:8080'

@app.route('/operate', methods=['POST'])
def operate():
    data = request.json
    user_id = data.get('user_id')
    sentence = data.get('request')

    if not user_id or not sentence:
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