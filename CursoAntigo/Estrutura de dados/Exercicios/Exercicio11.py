# Questão 11 - Unpacking com tuples
# Crie uma função que retorna uma tuple:
# def get_info():
#     return ("Python", 1991, "Guido van Rossum")
# Extraia os valores em variáveis separadas e imprima formatado.

def get_info():
    return ("Python", 1991, "Guido van Rossum")

nome, ano , criador = get_info() #Unpacking

print(f'Nome: {nome}, ano: {ano}, criador: {criador}')


