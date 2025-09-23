# Classe base Pessoa
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def se_apresentar(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}."

    def envelhecer(self):
        self.idade += 1
        return f"{self.nome} agora tem {self.idade} anos."

    def trabalhar(self):
        return f"{self.nome} está trabalhando como {self.profissao}."


p1 = Pessoa("Ana", 20, "Estudante")
p2 = Pessoa("Carlos", 30, "Professor")
p3 = Pessoa("João", 25, "Programador")

print(p1.se_apresentar())
print(p2.se_apresentar())
print(p3.se_apresentar())

print('\n')

print(p1.envelhecer())
print(p2.envelhecer())
print(p3.envelhecer())

print('\n')

print(p1.trabalhar())
print(p2.trabalhar())
print(p3.trabalhar())
