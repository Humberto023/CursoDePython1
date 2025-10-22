class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar_dados(self):
        print(f'Nome: {self.nome} com salario de R$ {self.salario:.2f}')

class Gerente(Funcionario):
    def __init__(self, nome, salario,setor):
        super().__init__(nome, salario)
        self.setor = setor

    def mostrar_dados(self):
            print(f'Gerente: {self.nome} com salario de R$ {self.salario:.2f} do setor {self.setor}')

g1 = Gerente('Beto', 18, 'vendas')
g1.mostrar_dados()


