class Passaro:
    def falar(self):
        print("Piu")

class Gato:
    def falar(self):
        print("Miau")

class Cachorro:
    def falar(self):
        print("Au Au")
        
    def brincar(self):  
        print("esse cachorro é muito fofo")
        
def som_animal(animal):
    animal.falar()
    
    
# Usando o polimorfismo
som_animal(Passaro())  # Saída: Piu
som_animal(Gato())     # Saída: Miau
som_animal(Cachorro()) # Saída: Au Au