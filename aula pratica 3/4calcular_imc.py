#fazer calculadora simples de imc

# IMC = peso / (altura ** 2) 



def calcular_imc():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    imc = peso / (altura ** 2)

    print(f"\nSeu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc < 24.9:
        print("Classificação: Peso normal")
    elif imc < 29.9:
        print("Classificação: Sobrepeso")
    else:
        print("Classificação: Obesidade")

calcular_imc()
