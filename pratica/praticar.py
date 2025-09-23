def cadastro():
    idade = int(input("Digite sua idade: "))
    if idade < 18:
        print("Você é menor de idade, não pode se cadastrar.")
    else:
        print("continue...")

        nome = input("Digite seu nome: ")
        cpf = input("Digite cpf: ")
        endereco = input("Digite seu endereço: ")

        print("\n--- FICHA DE CADASTRO ---")
        print("meu nome é: ", nome)
        print("meu cpf é: ",  cpf)
        print("meu endereco é: ", endereco)

def carro():
    idade = int(input("Digite sua idade: "))
    if idade < 18:
        print("Você é menor de idade, não pode se cadastrar.")
    else:
        print("continue...")

        nome = input("Digite seu nome: ")
        cpf = input("Digite cpf: ")
        endereco = input("Digite seu endereço: ")

        print("\n--- FICHA DE CADASTRO ---")
        print("meu nome é: ", nome)
        print("meu cpf é: ",  cpf)
        print("meu endereco é: ", endereco)

cadastro()
carro()