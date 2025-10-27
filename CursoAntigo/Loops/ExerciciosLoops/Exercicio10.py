#Numero negativo e positivo
# contadorPos = 0
# contadorNeg= 0
#
# for i in range(1,8):
#     num = int(input('Digite um numero: '))
#     if num > 0:
#         print('Numero positivo!')
#         contadorPos += 1
#     else:
#         print('Numero negativo!')
#         contadorNeg +=1
#
# print(f'Você digitou {contadorPos} numeros positivos e {contadorNeg} numeros negativos')

p = 0
n = 0
z = 0
for i in range(7):
    num =int(input('Digite um numero: '))


    if num > 0:
        p += 1
    elif num < 0 :
        n += 1
    else:
        z += 1

print(f'Você digitou {p} números positivos e {n} negativos e {z} zero')
