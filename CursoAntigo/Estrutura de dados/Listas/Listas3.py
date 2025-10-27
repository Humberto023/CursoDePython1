#Funcao dentro da lista

#Manipulando listas

#Armazenar vários dados em uma só variável

cidades = ['Rio de janeiro', 'São Pualo', 'Salvador', 'Goiânia']
#            0                   1            2          3
#      ----> +                                              - <----

cidades[0] = 'Brasilia ' # Isso altera o item
cidades.append('Santa Catarina')  #Adiciona um item ao fim da lista
# cidades.remove('Santa Catarina') #Remove um item da lista
cidades.insert(1, 'Joao pessoa') #Insere um item na posição que deseja
# cidades.pop(3) #Retira uma certa posição
cidades.sort() #Deixa em ordem alfabética
print(cidades)
