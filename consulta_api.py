import requests
import pytest

# Função para obter os dados do usuário
def get_user_by_uuid(wesantos):
    url = f'https://demoqa.com/Account/v1/User/wesantos'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    return response

# Teste com pytest
def test_get_user_by_uuid():
    uuid = "wesantos"  # Substitua pelo UUID real
    
    response = get_user_by_uuid(uuid)
    
    # Verificando se o status da resposta é 200 OK
    assert response.status_code == 200, f"Erro: {response.status_code} - {response.text}"

# Para executar o teste:
# pytest -v
