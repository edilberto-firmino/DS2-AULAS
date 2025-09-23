def cadastro():
    # Pede os dados do usuário
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    endereco = input("Digite seu endereço: ")

    # Exibe os dados cadastrados
    print("\n--- FICHA DE CADASTRO ---")
    print("Nome:", nome)
    print("CPF:", cpf)
    print("Endereço:", endereco)

# Chama a função para rodar o cadastro
cadastro()
