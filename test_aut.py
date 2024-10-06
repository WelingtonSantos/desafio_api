import requests
import pytest

# Definir a URL do endpoint para verificar autorização
url = 'https://demoqa.com/Account/v1/Authorized'

# Dados do usuário
data = {
    "userName": "wesantos",  # Substitua pelo nome de usuário real
    "password": "Nome@208"   # Substitua pela senha real
}

# Headers
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# Fazendo a requisição POST
response = requests.post(url, json=data, headers=headers)

# Verificando a resposta
if response.status_code == 200:
    print("Autorizado!")
elif response.status_code == 401:
    print("Não autorizado. Verifique as credenciais.")
else:
    print(f"Erro: {response.status_code}")
    print(f"Resposta da API: {response.text}")
