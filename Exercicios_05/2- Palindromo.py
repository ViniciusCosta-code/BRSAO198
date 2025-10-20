import string

def eh_palindromo(texto):
    # Remove espaços, pontuação e transforma em minúsculas
    texto_limpo = ''.join(
        char.lower() for char in texto if char.isalnum()
    )
    
    # Verifica se é igual ao invertido
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# Exemplo de uso:
frase = input("Digite uma palavra ou frase: ")
resultado = eh_palindromo(frase)
print(f"É palíndromo? {resultado}")