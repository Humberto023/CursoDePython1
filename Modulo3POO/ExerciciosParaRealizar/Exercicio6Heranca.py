class Animal:
    def __init__(self, nome, raca, idade, dados):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.dados = dados


class Cachorro(Animal):
    def __init__(self, nome, raca, idade, dados):
        super().__init__(nome, raca, idade, dados)


class Gato(Animal):
    def __init__(self, nome, raca, idade, dados):
        super().__init__(nome, raca, idade, dados)


class Falar(Animal):
    def __init__(self, nome, raca, idade, dados):
        super().__init__(nome, raca, idade, dados)

    def falar(self):
        print(f'Eu sou o {self.nome}, sou um {self.dados}, tenho {self.idade} anos e sou da raça {self.raca}.')


cachorro = Falar('Tobby', 'poodle', 4,'cachorro')
cachorro.falar()
gato = Falar('Tony', 'poodle', 4, 'gato')
gato.falar()