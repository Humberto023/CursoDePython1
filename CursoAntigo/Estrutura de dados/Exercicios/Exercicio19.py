# Questão 19 - Looping em dicionários
# Crie um dicionário de produtos:
# pythonprodutos = {
#     "arroz": 20.00,
#     "feijão": 8.50,
#     "macarrão": 5.00,
#     "óleo": 7.50
# }
# Use um loop para imprimir: "arroz custa R$ 20.00"


produtos = {
    'Arroz': 20.00,
    'Feijão': 8.50,
    'macarrao': 5.00,
    'Oleo': 7.50
}

for nome,valor in produtos.items():
    print(f'{nome}: {valor}')