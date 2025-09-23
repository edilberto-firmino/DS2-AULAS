frutas = {"maçã", "banana", "laranja"}
numeros = set([1,2,3,4,5])


conjunto1 = {1,2,3}
conjunto2 = {3,4,5}

uniao = conjunto1 | conjunto2
insercao = conjunto1 & conjunto2
diferenca = conjunto1 - conjunto2
diferenca_simetrica = conjunto1 ^ conjunto2

print(uniao)
print(insercao)
print(diferenca)
print(diferenca_simetrica)




frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()