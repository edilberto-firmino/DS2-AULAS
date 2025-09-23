class Casa:
    def __init__(self, cor=None, quartos=None, banheiros=None, tamanho=None):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros
        self.tamanho = tamanho

    def descrever(self):
        self.cor = input("Qual a cor da casa? ")
        self.quartos = input("Quantos quartos tem a casa? ")
        self.banheiros = input("Quantos banheiros tem a casa? ")
        self.tamanho = input("Qual o tamanho da casa em m²? ")


        return f"Esta casa é {self.cor}, tem {self.quartos} quartos, {self.banheiros} banheiros e {self.tamanho}m²."

cs = Casa()
print(cs.descrever())



class Pessoa:
    def __init__(self, nome=None):
        self.nome = nome
        self.nome = input("quil o seu nome? ")

    def falar(self, mensagem=None):
        self.mensagem = input("O que você quer dizer? ")
        # return f'{self.nome} disse: {self.mensagem}'
    
    def cantar(self, musica=None):
        self.musica = input("Qual música você quer cantar? ")
        # return f'{self.nome} está cantando: {self.musica}'
    
    def estudar(self, materia=None):
        self.materia = input("o que voce está estudando? ")
        # return f'{self.nome} está estudando: {self.materia}'
    
    def eu(self):
        return f'Meu nome é {self.nome}, e eu gostaria de falar {self.mensagem}, eu gosto de cantar a musica {self.musica} e estou estudando {self.materia}.'

p = Pessoa()
p.falar()
p.cantar()
p.estudar()
print(p.eu())

