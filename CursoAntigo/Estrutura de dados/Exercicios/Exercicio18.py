# Questão 18 - Atualizando dicionários
# Usando o dicionário da questão anterior:
#
# Mude a nota para 9.0
# Adicione uma nova chave "cidade" com valor "Rio de Janeiro"
# Remova a chave "curso"
# Imprima o dicionário atualizado

aluno = {
    'Nome': 'Maria',
    'Idade': 22,
    'Curso': 'Ciencia da computacao',
    'Nota': 8.7
}

aluno.update({'Nota': 9})
aluno.update({'Cidade': 'Rio de Janeiro'})
del aluno['Curso']

for k, v in aluno.items():
    print(f'{k}: {v}')


