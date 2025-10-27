
media = 0

for i in range(1,6):
    nota = int(input('Digite sua nota: '))
    media +=nota

resultado = media / 5

if resultado >= 6:
    print(f'Aprovado {resultado}')
else:
    print(f'Reprovado {resultado}')
