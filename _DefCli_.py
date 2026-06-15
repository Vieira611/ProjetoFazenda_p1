import requests

def buscar_cep():
    cep = 58900000
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    if resposta.status_code != 200:
        return None
    dados = resposta.json()
    if "erro" in dados:
        return None

    return {
        "logradouro": dados.get("logradouro", ""),
        "bairro": dados.get("bairro", ""),
        "cidade": dados.get("localidade", ""),
        "estado": dados.get("uf", "")
    }