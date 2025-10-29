# Questão 15 - Funções em sets
# Crie um set vazio e:
#
# Adicione 5 números diferentes usando .add()
# Tente adicionar um número repetido
# Remova um número usando .remove()
# Verifique se um número existe no set

numeros = []

num = set(numeros)

num.add(1)
num.add(30)
num.add(20)
num.add(10)
num.add(43)
#Irá tentar adicionar o numero repetido
num.add(43)
#Como no set numeros não mostram-se repetidos ele apaga o 43 que tinha já
num.remove(43)
existe = 40 in numeros
print(num)
print(existe)
