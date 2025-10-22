class casa: # Classe
    def __init__(self, cor, quartos,banheiros): #Construtor
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros

    def mostrar_cor(self):        #Métodos
        print(f'A cor da casa é {self.cor}')

    def mostrar_quartos(self):
        print(f'Esta casa tem {self.quartos} quartos')

    def mostrar_banheiros(self):
        print(f'Esta casa tem {self.banheiros} banheiros')

    def adicionar_quarto(self):
        self.quartos +=1
        print(f'Esta casa tem {self.quartos} quartos')

    def mudar_cor(self, nova_cor):

        print(f'Pintando a casa agora de {self.cor} para {nova_cor}')



casa1 = casa('Amarelo', 4, 2)
casa2 = casa('Azul',6 ,2)

print('\nCasa1: ')
casa1.mostrar_cor()                  # Instâncias da classe
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.adicionar_quarto()
casa1.mudar_cor('rosa')


print('\nCasa2: ')
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()
casa2.adicionar_quarto()