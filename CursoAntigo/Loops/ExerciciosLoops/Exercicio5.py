#Tabuada de 1 até 10

num = int(input('Digite um número onde será mostrado a tabuada dele: '))
#Loop de 1 até 10
for i in range(1, 11):
    #Calcula o número da multiplicação com o contador 1, 2,3 ,4,5, etc
    resultado = num * i
    #Exibirá o cálculo do contador
    print(f'{num} x {i} = {resultado}')

