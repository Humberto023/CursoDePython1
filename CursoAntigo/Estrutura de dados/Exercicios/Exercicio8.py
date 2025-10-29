# Questão 8 - Zip com duas listas
# Você tem:
# python nomes = ["Ana", "Bruno", "Carlos"]
# idades = [25, 30, 28]
# Use zip() para criar pares e imprima: "Ana tem 25 anos"

nomes = ["Ana", "Bruno", "Carlos"]
idades = [25, 30, 28]

for nome,idade in zip(nomes, idades):
    print(f'{nome} tem {idade} anos')


