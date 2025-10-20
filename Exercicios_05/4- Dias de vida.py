from datetime import datetime

def calcular_dias_vivo(data_nascimento):
    # Data atual
    hoje = datetime.today()
    
    # Calcula a diferença entre hoje e a data de nascimento
    diferenca = hoje - data_nascimento
    
    # Retorna o número de dias
    return diferenca.days

# Interação com o usuário
print("Calculadora de dias vivos")

# Solicita a data de nascimento
data_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")

try:
    # Converte a string para objeto datetime
    data_nasc = datetime.strptime(data_str, "%d/%m/%Y")
    
    # Calcula os dias vivos
    dias = calcular_dias_vivo(data_nasc)
    
    print(f"Você está vivo(a) há {dias} dias.")
except ValueError:
    print("Data inválida! Por favor, digite no formato dd/mm/aaaa.")