class Carro:
    def __init__(self,marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = True

    def ligar(self):
        if not self.ligado:
            self.ligado = False
            print('O carro será ligado')
        else:
            print('O carro já estava ligado')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('O carro será desligado')

        else:
            print('O carro já estava desligado')

c1 = Carro('Hyundai', 'hb20', 2005)
c1.ligar()
c1.desligar()


