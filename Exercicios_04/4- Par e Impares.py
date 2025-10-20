def analisar_numeros():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número (ou 'sair' para encerrar): ")

        if entrada.lower() == 'sair':
            break

        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} é par.")
                pares += 1
            else:
                print(f"{numero} é ímpar.")
                impares += 1
        except ValueError:
            print("Entrada inválida. Digite um número inteiro ou 'sair'.")

    print("\n--- Resultado Final ---")
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")

# Executa o programa
analisar_numeros()