class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        print(f"{self.marca} {self.modelo} - {self.ano}")


carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2022)

carro1.exibir_informacoes()
carro2.exibir_informacoes()
