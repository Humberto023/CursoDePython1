class Motor:
    def __init__(self, marca, potencia):
        self.marca = marca         #Referencia o valor que possui
        self.potencia = potencia

class Carro:
    def __init__(self):
        self.motores = []

    def adicionar_motor(self,motor):
        self.motores.append(motor)    #append adiciona um item à lista

    def listar_motores(self):          #Metodo
        for motor in self.motores:
            print(f'Motor: {motor.marca} - {motor.potencia}CV de potência')

#Criando os Motores (objetos)

motor_v6 = Motor ('Ford', 300)
motor_v8 = Motor('Ferrari', 400)
motor_v12 = Motor('Lamborghini', 950)
#Criar o carro e adicionar o motor à ele
carro = Carro()
carro.adicionar_motor(motor_v6)
carro.adicionar_motor(motor_v8)
carro.adicionar_motor(motor_v12)


#Listar os motores

carro.listar_motores()