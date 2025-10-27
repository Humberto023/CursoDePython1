#Maior dos números

#Utilizando o for, mas de uma forma mais simplificada teria que ser feito n1,n2,n3 e adicionar um if  tipo if n1 >= n2 and n1 >=3....
numeros = []

for i in range(3):
    num = int(input('Digite um número: '))
    numeros.append(num)

#Verificará o maior número
maior = numeros [0]
for n in numeros:
    if n > maior:
        maior = n


print(maior)

