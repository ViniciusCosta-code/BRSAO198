def calcular_desconto(preco_original, porcentagem_desconto):
    # Calcula o valor do desconto
    desconto = preco_original * (porcentagem_desconto / 100)
    
    # Calcula o preço final
    preco_final = preco_original - desconto
    
    # Arredonda para 2 casas decimais
    desconto = round(desconto, 2)
    preco_final = round(preco_final, 2)
    
    return desconto, preco_final

# Interação com o usuário
print("Calculadora de Desconto")

# Entrada de dados
preco = float(input("Digite o preço original do produto (R$): "))
desconto_percentual = float(input("Digite a porcentagem de desconto (%): "))

# Processa os dados
desconto, preco_com_desconto = calcular_desconto(preco, desconto_percentual)

# Mostra o resultado
print(f"\nDesconto aplicado: R$ {desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_com_desconto:.2f}")
