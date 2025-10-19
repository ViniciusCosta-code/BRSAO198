# Função para converter temperatura
def converter_temperatura(valor, origem, destino):
    # Converte a temperatura para Celsius como base
    if origem == "C":
        celsius = valor
    elif origem == "F":
        celsius = (valor - 32) * 5 / 9
    elif origem == "K":
        celsius = valor - 273.15
    else:
        return "Unidade de origem inválida."

    # Converte de Celsius para a unidade de destino
    if destino == "C":
        return celsius
    elif destino == "F":
        return (celsius * 9 / 5) + 32
    elif destino == "K":
        return celsius + 273.15
    else:
        return "Unidade de destino inválida."

# Entrada do usuário
valor = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

# Realiza a conversão
resultado = converter_temperatura(valor, origem, destino)

# Exibe o resultado
if isinstance(resultado, str):
    print(resultado)  # Mensagem de erro
else:
    print(f"\n{valor}°{origem} é igual a {resultado:.2f}°{destino}")