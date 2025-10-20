def calculadora():
    print("Calculadora Básica")
    print("Operações disponíveis: +, -, *, /")

    # Solicita os números e a operação
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    # Executa a operação
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida.")
            return
    else:
        print("Operação inválida.")
        return

    print(f"Resultado: {num1} {operacao} {num2} = {resultado}")

# Executa a calculadora
calculadora()
