# ======================================================
# EXEMPLO 1: CLASSE CACHORRO
# ======================================================

class Cachorro:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def latir(self):
        return f"{self.nome} está latindo e tem {self.idade} anos e pesa {self.peso} KG!"

def executar_exemplo():
    dog1 = Cachorro("kadu", 8, 12)
    dog2 = Cachorro("marco", 9, 11)
    dog3 = Cachorro("loki", 3, 40)


    print(dog1.latir())
    print(dog2.latir())
    print(dog3.latir())
