duracaoProduto = int(input('Qual a duração do produto?: '))
porcoes = int(input('Quantas porções irá utilizar por dia?: '))

qDias = duracaoProduto / porcoes

print(f'A quantidade de dias que irá durar será de {qDias:.0f} dias!')