# Questão 20 - Keys, Values e Items
# Usando o dicionário da questão 19:
#
# Imprima apenas as chaves (nomes dos produtos) usando .keys()
# Imprima apenas os valores (preços) usando .values()
# Imprima pares chave-valor usando .items()
# Calcule o total de todos os produtos


produtos = {
    'Arroz': 20.00,
    'Feijão': 8.50,
    'macarrao': 5.00,
    'Oleo': 7.50
}

p= produtos.keys()
v = produtos.values()
pares = produtos.items()
total = sum(produtos.values()) #Soma todos os elementos de uma sequencia
print(v)
print(pares)
print(total)