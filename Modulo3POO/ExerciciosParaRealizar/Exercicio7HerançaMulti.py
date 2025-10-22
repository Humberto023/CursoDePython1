#Isso é uma herança multipla, por conta que há uma classe utilizando todas anteriores, mas não de forma linear
#Tipo, A>b>c e sim está A / B /  A =B >c, C depende das outras duas, mas as outras duas não estãoo em uma ordem de Avo>pai>filho e sim de Pai pai filho


class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Terrestre:
    def andar(self):
        print("Eu sou um carro que anda na terra")

class Motorizado:
    def ligar_motor(self):
        print("Eu sou também motorizado")

class Carro(Veiculo, Terrestre, Motorizado):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def falar(self):
        print(f'Sou da marca {self.marca} modelo {self.modelo}')

c1 = Carro('Hyundai', 'HB20')
c1.falar()
c1.andar()
c1.ligar_motor()
