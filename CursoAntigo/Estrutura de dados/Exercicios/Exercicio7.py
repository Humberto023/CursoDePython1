# Questão 7 - Verificando itens
# Dada a lista cores = ["vermelho", "azul", "verde", "amarelo"]:
#
# Verifique se "azul" está na lista
# Verifique se "roxo" está na lista
# Conte quantas vezes "azul" aparece na lista

cores = ["vermelho", "azul", "verde", "amarelo"]

if 'vermelho' in cores:
    print('Em estoque')
else:
    print('Em falta')

if 'verde' in cores:
    print('Em estoque')
else:
    print('Em falta')

if 'amarelo' in cores:
    print('Em estoque')
else:
    print('Em falta')

quantas = cores.count('azul')
print(quantas)
