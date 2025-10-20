import requests
from datetime import datetime

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        dados = resposta.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Moeda não encontrada.")
            return

        cotacao = dados[chave]
        
        valor_atual = float(cotacao["bid"])
        valor_max = float(cotacao["high"])
        valor_min = float(cotacao["low"])
        timestamp = int(cotacao["timestamp"])
        data_hora = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

        print(f"\nCotação {moeda}/BRL")
        print(f"Valor atual: R$ {valor_atual:.2f}")
        print(f"Valor máximo: R$ {valor_max:.2f}")
        print(f"Valor mínimo: R$ {valor_min:.2f}")
        print(f"Última atualização: {data_hora}")

    except requests.exceptions.RequestException:
        print("Erro de conexão. Verifique sua internet.")
    except Exception:
        print("Erro ao processar os dados. Verifique se a moeda está correta.")

# Interação com o usuário
moeda_input = input("Digite a sigla da moeda que deseja consultar (ex: USD, EUR, BTC): ").upper()
consultar_cotacao(moeda_input)