def registrar_notas():
    notas = []
    while True:
        entrada = input("Digite a nota do aluno (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Por favor, digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número ou 'sair'.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\nNotas registradas: {notas}")
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhuma nota foi registrada.")

registrar_notas()