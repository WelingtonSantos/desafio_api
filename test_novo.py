import requests
import pytest

# Definir a URL do endpoint para verificar autorização
url = 'https://demoqa.com/Account/v1/Authorized'

# Função para verificar autorização
def authorize_user(user_data):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=user_data, headers=headers)
    return response

# Dados do usuário (use credenciais válidas para os testes)
user_data = {
    "userName": "wesantos",  # Substitua pelo nome de usuário real
    "password": "Nome@208"   # Substitua pela senha real
}

# Teste para verificar autorização
def test_authorization():
    response = authorize_user(user_data)

    # Verificando a resposta
    assert response.status_code == 200, f"Erro: {response.status_code} - {response.text}"
    
    # Tente converter a resposta para JSON e verifique se é um dicionário
    json_response = response.json()
    
    # Verifique se o campo esperado está presente na resposta
 #   assert isinstance(json_response, dict), "A resposta não é um dicionário."
 #   assert "some_expected_field" in json_response, "O campo esperado não foi encontrado na resposta."

