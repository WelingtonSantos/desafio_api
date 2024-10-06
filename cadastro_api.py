import requests
import requests
import json

# Configuração da URL e dos Headers
url = 'https://demoqa.com/Account/v1/User'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# Dados do corpo da requisição
payload = {
    "userName": "wesantos",  # Substitua 'string' pelo nome de usuário desejado
    "password": "Nome@208"   # Substitua 'string' pela senha adequada
}

# Fazendo a requisição POST
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Verificando a resposta
if response.status_code == 201:  # Verifica se o status da resposta é "201 Created"
    print("Usuário criado com sucesso!")
else:
    print(f"Erro: {response.status_code}")
    print(f"Resposta da API: {response.text}")
