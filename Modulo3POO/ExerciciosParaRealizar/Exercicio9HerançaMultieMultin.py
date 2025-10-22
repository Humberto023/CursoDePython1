class Robo:
    def __init__(self,nome):
        self.nome = nome
        self.ativado = False  #O robo inicia-se desativado

    def ativacao(self):
        self.ativado = False


class Domestico(Robo):
    def __init__(self,nome):
        super().__init__(nome)


class Industrial(Robo):
    def __init__(self,nome):
        super().__init__(nome)

class Limpeza:
    def limpar (self):
        if self.ativado:
            print(f'O robo {self.nome} está ativo para limpeza')
        else:
            print(f'O Robo {self.nome} precisa ser ativado para limpeza')

class Solda:
    def soldar (self):
            if self.ativado:
                print(f'O robo {self.nome} está ativo para soldar')
            else:
                print(f'O Robo {self.nome} precisa ser ativado para soldar')



class Aspirador(Domestico, Limpeza):
    def __init__(self,nome):
        super().__init__(nome)


class Soldador(Industrial, Solda):
    def __init__(self,nome):
        super().__init__(nome)

a = Aspirador('T-kezz')
a.ativacao()
a.limpar()

s = Soldador('Topo')
s.ativacao()
s.soldar()