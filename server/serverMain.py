from flask import Flask, request, jsonify

import gptAPI as gptAPI

app = Flask(__name__)

token_data = {
    'id': 'c9914832-aabb-4830-8962-7ed78ca2e97e',
    'user_id': 'dc92bf38-cce2-4f32-8fe3-b52806f8c352',
    'expire_date': '2023-12-31T23:59:59Z',
    'credits': 10  
}

user_data = {
    'user_id': 'dc92bf38-cce2-4f32-8fe3-b52806f8c352',
    'username': 'XxIsla30xX',
    'firstName': 'John',
    'lastName': 'James',
    'email': 'john@email.com',
    'password': '12345'
}

@app.route('/token', methods=['GET'])
def get_token():
    user_id = request.args.get('user_id')
    if user_id:
        return jsonify(token_data), 200
    else:
        return jsonify({'error': 'Paramètre user_id manquant'}), 400

@app.route('/sendapi', methods=['POST'])
def send_api():
    data = request.json
    user_id = data.get('user_id')
    phrase = data.get('phrase')
    action = data.get('action')

    if not user_id or not phrase or not action:
        return jsonify({'error': 'Paramètres user_id, phrase et action requis'}), 400

    # Vérification du token et des crédits disponibles
    if user_id == token_data['user_id'] and token_data['credits'] > 0:

        if action == 'chatGPT':
            token_data['credits'] -= 1
            gptAPI.callChatGPT(phrase)

        response = {'message': f'Phrase envoyée avec succès. Crédits restants : {token_data["credits"]}'}
        return jsonify(response), 200
    
    else:
        return jsonify({'error': 'Token invalide ou crédits épuisés'}), 403

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
