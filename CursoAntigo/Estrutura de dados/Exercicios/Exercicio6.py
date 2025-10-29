# Questão 6 - Looping em listas
# Crie uma lista animais = ["cachorro", "gato", "coelho", "papagaio"] e:
#
# Use um for para imprimir cada animal
# Use enumerate() para imprimir o número e o animal (ex: "1. cachorro")

animais = ["cachorro", "gato", "coelho", "papagaio"]

for x in animais:
    print(x) #Enquanto houver x valor em animais irá ilustrar o valor na lista

print()

#enumarate é uma função para obter o indice e o valor da lista
for i,x in enumerate(animais):
    print(f'{i}.{x}')