
nMaior = int(input('Digite um número: ')) #armazena um número que será o maior

for i in range(5):
    num = int(input("Digite um número: ")) #pergunta o próximo número
    if num > nMaior:
        nMaior = num  #Irá verificar se o novo número é maior que o primeiro
print(nMaior)