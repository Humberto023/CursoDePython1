#Para dirigir a pessoa tem que ser maior de 18 e ter carteira de motorista
idade = int(input('Digite sua idade: '))
carteira = False # se tem carteira ou não

verificador = idade >= 18 and carteira   #Se é maior de 18 e também possui carteira
print(verificador)