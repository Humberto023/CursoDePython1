class Animail:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

class Mamifero(Animail):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)

class Cachorro(Mamifero):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)

    def latir(self):
        print(f'Eu sou o {self.nome} cachorro de latir')

class Golfinho(Mamifero):
    def __init__(self,nome,idade,tipo):
        super().__init__(nome,idade)
        self.tipo = tipo

    def apresentar(self):
        print(f'Eu sou {self.tipo}, me chamo {self.nome} tenho {self.idade}')

c = Cachorro('Cachorro',18)
c.latir()
g = Golfinho('Tobby',18,'Golfinho')
g.apresentar()