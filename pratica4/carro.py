# ======================================================
# EXEMPLO 2: CLASSE CARRO
# ======================================================

class Carro:
    def __init__(self, marca, modelo, ano, cor, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade

    def detalhes(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - Cor: {self.cor}, Velocidade: {self.velocidade} km/h"

    def acelerar(self, aumento):
        self.velocidade += aumento
        return f"{self.modelo} acelerou para {self.velocidade} km/h!"

    def frear(self, reducao):
        self.velocidade -= reducao
        if self.velocidade < 0:
            self.velocidade = 0
        return f"{self.modelo} reduziu para {self.velocidade} km/h."


def executar_exemplo():
    carro1 = Carro("Toyota", "Corolla", 2020, "Preto")
    carro2 = Carro("Honda", "Civic", 2019, "Vermelho")

    print(carro1.detalhes())
    print(carro2.detalhes())

    print(carro1.acelerar(50))
    print(carro2.acelerar(30))

    print(carro1.frear(20))
    print(carro2.frear(15))

    print(carro1.detalhes())
    print(carro2.detalhes())
    
executar_exemplo()
