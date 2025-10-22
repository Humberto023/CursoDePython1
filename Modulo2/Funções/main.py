from funcao import verificar_maioridade, saudacao, soma

minha_idade = int(input('Digite sua idade: '))

if verificar_maioridade(minha_idade):
    print('Você é maior de idade!')
else:
    print('Você é menor de idada!')

