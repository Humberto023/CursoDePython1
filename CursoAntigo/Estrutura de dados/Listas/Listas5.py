#Extrair variáveis de entro de uma lista


produtos = ['arroz', 'feijão', 'Laranja','banana',5,6,7,8]
          #  0         1         2         3

item1, item2,*outros, item8  = produtos



print(item1)
print(item2)
print(item8)
print(*outros)
