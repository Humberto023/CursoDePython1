# Somas dos pares
soma = 0 #variável que irá acumular apenas os números pares

for i in range(1,10):  #Irá de 1 até 10
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num

print(soma)