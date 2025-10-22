#Herança Multipla e herança de multinivel
#Classe avo

class Animal:
    def __init__(self, nome):
        self.nome = nome


#Classes pai
class Predador(Animal):
    def cacando(self):
        print(f"O Animal {self.nome} está cancando")

class Presa(Animal):
    def fugindo(self):
        print(f'O animal {self.nome} está fugindo')
#Clases filho

class Coelho(Presa):
    pass

class Tigre(Predador):
    pass

class Golfinho(Presa,Predador):
    pass

coelho1 = Coelho('Bunny')
tigre1 = Tigre('Dentinho')
golfinho1 = Golfinho('Billy')

golfinho1.cacando()
tigre1.cacando()
coelho1.fugindo()