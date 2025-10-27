'''
Criar um retangulo 6x6
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
'''

linhas = 6
colunas = 6
simbolo = '#'

for l in range(linhas):      #6x      1   2
    for c in range(colunas):
        print(simbolo, end='')  #6x     000000    000000
    print()                    #Enter