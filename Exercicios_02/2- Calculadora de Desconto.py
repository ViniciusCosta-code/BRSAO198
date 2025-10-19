# Cálculo de desconto em um produto

nome_produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20  # em %

# Calculando o valor do desconto
valor_desconto = (percentual_desconto / 100) * preco_original

# Calculando o preço final com desconto
preco_final = preco_original - valor_desconto

# Exibindo os detalhes
print("Produto:", nome_produto)
print("Preço original: R$ {:.2f}".format(preco_original))
print("Desconto: {}%".format(percentual_desconto))
print("Valor do desconto: R$ {:.2f}".format(valor_desconto))
print("Preço final: R$ {:.2f}".format(preco_final))

