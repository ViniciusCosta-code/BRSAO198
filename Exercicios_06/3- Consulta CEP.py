import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        dados = resposta.json()
        
        if "erro" in dados:
            print("CEP não encontrado.")
            return
        
        logradouro = dados.get("logradouro", "Não informado")
        bairro = dados.get("bairro", "Não informado")
        cidade = dados.get("localidade", "Não informado")
        estado = dados.get("uf", "Não informado")
        
        print(f"Logradouro: {logradouro}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")
        
    except requests.exceptions.RequestException:
        print("Erro na requisição. Verifique sua conexão ou o CEP informado.")

# Interação com o usuário
cep_input = input("06186073")
consultar_cep(cep_input)