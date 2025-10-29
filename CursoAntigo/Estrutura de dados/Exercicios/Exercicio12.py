#  ARRAYS (Questão 12)
# Questão 12 - Trabalhando com arrays
# Importe o módulo array e crie um array de inteiros:
# pythonfrom array import array
# numeros = array('i', [10, 20, 30, 40, 50])
#
# Adicione o número 60
# Remova o número 20
# Imprima o array
from array import array


numeros = array('i', [10, 20, 30, 40, 50])

numeros.append(60)
numeros.remove(20)
print(numeros)