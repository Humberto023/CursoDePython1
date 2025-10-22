# Cria um dicionário chamado 'aluno' e já pede os dados ao usuário
aluno = {
    'nome': input('Digite o nome do aluno: '),   # Pergunta o nome do aluno e guarda na chave 'nome'
    'idade': input('Digite a idade do aluno: '), # Pergunta a idade do aluno e guarda na chave 'idade'
    'nota': input('Digite a nota do aluno: ')    # Pergunta a nota do aluno e guarda na chave 'nota'
}

# Mostra na tela os dados do aluno de forma organizada
print(f"{aluno['nome']} tem {aluno['idade']} anos de idade e tirou uma nota de {aluno['nota']}")
# {aluno['nome']} → pega o valor da chave 'nome'
# {aluno['idade']} → pega o valor da chave 'idade'
# {aluno['nota']} → pega o valor da chave 'nota'
# Tudo dentro do f-string é convertido em texto e exibido junto com o resto da frase
