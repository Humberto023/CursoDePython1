class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'O meu nome é {self.nome} e tenho {self.idade} anos.')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)   #sempre que for adicionar algo que não esteja dentro do parâmetro pai, é necessário usar uma função imbutida "Super" para que assim seja permitido aplicar algo diferente do que havia. Assim, colocando as coisas que precisa PUXAR
        self.cargo = cargo

    def trabalhar(self):
        print(f'{self.nome} está trabalhando como {self.cargo} ')


class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome, idade)
        self.saldo = saldo

    def comprar(self, valor_compra):
        if valor_compra <= self.saldo:
            self.saldo -= valor_compra
            print(f'Olá {self.nome} sua compra de {valor_compra} foi aprovadda! Seu saldo atual é de R$ {self.saldo}')
        else:
            print('Olá {self.nome} o seu saldo foi insuficiente')




f1 = Funcionario('Maria', 38, 'Gerente de contas')
# f1.apresentar()
# f1.trabalhar()



c1 = Cliente('Joao', 67, 500)
c2 = Cliente('Jose', 26, 50)
# c1.apresentar()
c1.comprar(50)
c2.comprar(30)