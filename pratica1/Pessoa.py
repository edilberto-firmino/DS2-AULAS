class SerVivo:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def respirar(self):
        
        print(f"{self.nome} está respirando...")

    def dormir(self):
        print(f"{self.nome} está dormindo...")

class Pessoa(SerVivo):
    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}")

    def andar(self, destino):
        print(f"{self.nome} está andando até {destino}.")

    def comer(self, comida):
        print(f"{self.nome} está comendo {comida}.")

# Criando objetos
p1 = Pessoa("Edilberto", 25)
p2 = Pessoa("Maria", 30)

# Chamando ações
p1.respirar()
p1.falar("Olá, mundo!")
p1.andar("a escola")
p1.comer("pizza")

print("-----")

p2.dormir()
p2.falar("Estou estudando POO!")
