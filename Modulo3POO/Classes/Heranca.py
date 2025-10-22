class Animal:               #Clase principoal (pai)
    def __init__(self,nome,cor,especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie

    def apresentar(self):
        print(f'Eu sou um {self.especie} chamado {self.nome}')

class Gato(Animal):                                                                                                      #Classe filha, onde é necessário apenas passar os dados do gato, utilizando métodos dentro da classe pai
    def emitirsom(self):
        print('Miau')
    def arranhar(self):
        print('O gato está arranhando')

class Cachorro(Animal):
    def emitirsom(self):
        print('AuAuAu')

class Elefante(Animal):
    def emitirsom(self):
        print('bruuu')



gato1 = Gato('tom', 'branco' , 'Siamese')
gato1.apresentar()
gato1.emitirsom()
gato1.arranhar()
print('\n')

cachorro1 = Cachorro('Tobby', 'Preto', 'Poodle')
cachorro2 = Cachorro('Jacob', 'Preto', 'Maltese')
cachorro1.apresentar()
cachorro1.emitirsom()
cachorro2.apresentar()
print('\n')

elefante1 = Elefante('Fred', 'Cinza', 'Asiatico')
elefante1.apresentar()
elefante1.emitirsom()





#As classes filhas podem utilizar tudo que estiver dentro da classe pai, e as classes filhas podem ter suas próprias difinições, mas as outras não poderão utilizar

