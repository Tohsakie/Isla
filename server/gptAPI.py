import requests
import json

def callChatGPT(question):
    API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
    API_KEY = loadConf()

    messages = [
        {"role": "system", "content": "Tu es un assistant qui se nome ISLA et qui aide."},
        {"role": "user", "content": question}
    ]
    
    reponse_chatgpt = generate_chat_completion(messages, API_KEY, API_ENDPOINT, model="gpt-3.5-turbo", temperature=1, max_tokens= None)
    return reponse_chatgpt

def generate_chat_completion(messages, API_KEY, API_ENDPOINT, model="gpt-3.5-turbo", temperature=1, max_tokens= None):
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
    
def loadConf():
    with open('conf.json') as json_file:
        data = json.load(json_file)
    return data["keyAPI"]
