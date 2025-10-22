class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
        def __init__(self, nome, idade,matricula):
            super().__init__(nome, idade)
            self.matricula = matricula
            print(f'Aluno: {self.nome} possui {self.idade}anos, de matricula {self.matricula}')

class Falar(Pessoa):

    def __init__(self, nome, idade,matricula):
        super().__init__(self, nome, idade)
        print(f'Me chamo {self.nome}, tenho {self.idade} de matricula {matricula}')

class Professor(Pessoa):
    def __init__(self, nome, idade,materia):
        super().__init__(nome, idade)
        self.materia = materia
        print(f'Professor {self.nome} possui {self.idade} de materia {self.materia}')

a1 = Aluno('beto', 18, 402781)
p1 = Professor('Beto', 18, 'Historia')


