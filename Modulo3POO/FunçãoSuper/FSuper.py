#Sistema de Escola

class Escola():
    def __init__(self, nome, idade, status):
        self.nome = nome
        self.idade = idade
        self.status = status
    def verificar_status(self):
        print(f'Status: {"ATIVO" if self.status else "INATIVO"}')  #Se o status for verdadeiro, retorna o "ATIVO" antes do self, se for falso, retorna o ultimo negocio digitado o "INATIVO"
 

    def Apresentar(self):
        print(f'Meu nome é {self.nome}')



class Aluno(Escola):
    def __init__(self, nome,idade,status,ano):
        super().__init__(nome,idade,status)
        self.ano = ano

    def Apresentar(self):
        super().Apresentar()
        print(f'Eu sou um aluno da escola')

class Professor(Escola):
    def __init__(self, nome,idade,status ,materia):
      super().__init__(nome, idade,status)
      self.materia = materia

    def Apresentar(self):
        super().Apresentar()
        print(f'Eu sou um professor da escola')

class Assistente(Escola):
    def __init__(self, nome,idade,status ,bloco):
        super().__init__(nome, idade,status)
        self.bloco = bloco

    def Apresentar(self):
        super().Apresentar()
        print(f'Eu sou um assistente da escola')

a1 = Aluno('Gustavo',18,True ,'3',)

p1 = Professor('Rafael',45,True,'História')

as1 = Assistente('Thais', 29 ,False , 'B')

as1.Apresentar()
as1.verificar_status()

