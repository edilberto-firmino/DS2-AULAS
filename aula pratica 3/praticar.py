def teste():
    print("Hello, World!")
    nome = input("Qual é o seu nome? ")
    idade = int(input("Quantos anos você tem? "))


    if idade > 18:
        print(f"Olá, {nome} Você tem {idade} anos, logo você é maior de idade.")
    else:
        print(f"Olá, {nome} Você tem {idade} anos, logo você é menor de idade.")


teste()