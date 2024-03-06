import requests
import json

ca_cert = './certs/RootCA.pem'
client_cert = './certs/client01-chain.pem'
client_key = './certs/client01.key'

client_tls = (client_cert, client_key)

def ask(question, user_id):
    url = 'http://159.31.69.199:8085/operate'
    payload = json.dumps({
        'user_id': user_id,
        'request': question
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request('POST', url, headers=headers, data=payload,
                                cert=client_tls, verify=ca_cert)

    if response.status_code == 200:
        return response.json()
    else:
        return None


# print(ask("Quel temps fait-il à Paris ?", "fee18e97-a5c4-4d72-9bbc-24c5d2edd67a"))
