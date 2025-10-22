class Carro:
    def __init__(self, cor, ano):
        self.cor= cor
        self.ano = ano
        self.ligado = True
        self.seta = None

    def informacoes (self):
        print(f'A cor do carro é {self.cor}')
        print(f'O ano do carro é {self.ano}')

    def ligar(self):
        if not self.ligado:             #Vai verificar o valor oposta para fins de teste, ou se tornara false
            self.ligado = True
            print('O carro foi ligado') #Se o carro estiver desligado(False) informa que o carro será ligado
        else:
            print('O carro já estava ligado') #Se estiver TRUE, ou seja, o carro já está ligado

    def desligar(self):
        if self.ligado:
            self.ligado = False             #Se estiver ligado TRUE o "Desligue ele" = carro será desligado
            print('O carro foi desligado')
        else:
            print('O carro já estava desligado') #Se já estiver desligado FALSE, informa que já estava desligado

    def ligar_serta(self, direcao):
        if not self.ligado:
            print('Ligue o carro primeiro')
            return

        self.seta = direcao
        print(f'Seta ligada para a {self.seta}')

carro1 = Carro('Preto', 2021)
carro1.informacoes()
carro1.ligar()
carro1.ligar_serta('Direita')