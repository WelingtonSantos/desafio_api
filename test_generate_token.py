# test_generate_token.py

import requests
import pytest

def generate_token(user_data):
    url = 'https://demoqa.com/Account/v1/GenerateToken'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json=user_data, headers=headers)
    return response

def test_generate_token():
    # Substitua com um nome de usuário e senha válidos
    user_data = {
        "userName": "wesantos",  # Nome de usuário
        "password": "Nome@208"   # Senha
    }

    response = generate_token(user_data)

    # Verifique se o status da resposta é 200 (OK)
    assert response.status_code == 200, f"Erro: {response.status_code} - {response.text}"

    # Você também pode verificar se o token foi retornado
    json_response = response.json()
    assert "token" in json_response, "Token não encontrado na resposta."
