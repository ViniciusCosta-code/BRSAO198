import random
import string

def gerar_senha(tamanho):
    # Define os caracteres que serão usados na senha
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera a senha escolhendo caracteres aleatórios
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    
    return senha

# Interação com o usuário
print("Gerador de Senhas Aleatórias")
try:
    tamanho = int(input("Digite o tamanho desejado para a senha (mínimo 6 caracteres): "))
    if tamanho < 6:
        print("Recomenda-se uma senha com pelo menos 6 caracteres para maior segurança.")
    senha_gerada = gerar_senha(tamanho)
    print(f"Senha gerada: {senha_gerada}")
except ValueError:
    print("Por favor, digite um número válido para o tamanho da senha.")