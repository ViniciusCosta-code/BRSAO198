import requests

def buscar_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Vai gerar erro se o status não for 200
        
        dados = resposta.json()
        usuario = dados['results'][0]
        
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        print("Usuário aleatório encontrado:")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
        
    except requests.exceptions.RequestException:
        print("Falha na conexão. Não foi possível obter o usuário.")

# Executa o programa
buscar_usuario_aleatorio("Vinicius")