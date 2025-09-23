#fazer ficha de cadastro de pets 
#nome
#tipo
#raca
#idade






def cadastro_pet():
    pet = {}

    pet["nome"] = input("Nome do pet: ")
    pet["tipo"] = input("Tipo do pet (cachorro, gato, etc.): ")
    pet["raca"] = input("Raça: ")
    pet["idade"] = int(input("Idade: "))

    print("\n--- FICHA DO PET ---")
    for chave, valor in pet.items():
        print(f"{chave.capitalize()}: {valor}")

cadastro_pet()
