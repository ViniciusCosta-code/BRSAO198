def calcular_gorjeta(valor_conta, porcentagem):
    gorjeta = valor_conta * (porcentagem / 100)
    return gorjeta

# Exemplo de uso:
valor = float(input("Digite o valor da conta: R$ "))
percentual = float(input("Digite a porcentagem da gorjeta (%): "))

gorjeta_calculada = calcular_gorjeta(valor, percentual)
print(f"Gorjeta: R$ {gorjeta_calculada:.2f}")
print(f"Total com gorjeta: R$ {valor + gorjeta_calculada:.2f}")