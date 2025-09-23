class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def andar(self):
  	print(f"{self.name} esta andando")
    
  def correr(self):
  	print(f"{self.name} esta correndo, com idade{self.age}")
    
  def dormir(self):
    print(f"{self.name} esta dormindo")

  def falar(self, msg="esta falando"):
  	return f"{self.name} {msg}"

p1 = Person("John", 36)
p2 = Person("edilberto", 35)

p1.andar()
p1.correr()
print("--------------------------------")
p2.andar()
p2.correr()
p2.dormir()

p2.falar("casa")
print(p2.falar())
