def verificar_senha(senha):
    # Critério A: pelo menos 8 caracteres
    if len(senha) < 8:
        return "Senha fraca: deve ter pelo menos 8 caracteres."

    # Critério B: pelo menos um número
    if not any(char.isdigit() for char in senha):
        return "Senha fraca: deve conter pelo menos um número."

    return "Senha forte!"

# Solicita a senha do usuário
senha_usuario = input("Digite sua senha: ")
resultado = verificar_senha(senha_usuario)

print(resultado)