class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}')

    def anversario(self):
        self.idade += 1
        print(f'Sua idade daqui 1 ano será {self.idade}')

p1 = Pessoa('Humberto', 20)
p1.mostrar_dados()
p1.anversario()
p1.mostrar_dados()