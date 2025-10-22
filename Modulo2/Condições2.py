'''usuario = input('Digite seu usuario: ')
senha = input('Digite sua senha: ')

if usuario == 'Admin' and senha == '1234':
    print('login valido')
else:
    print('Verifique o usuário ou senha!')'''


idade = int(input('Digite sua idade: '))
autorizacao_pais = input(' Tem autorização dos pais?: s/n? : ')

if idade >=18:
    print('acesso liberado')
elif idade>= 16 and autorizacao_pais == 's':
    print('Acesso liberado via autorização')
else:
    print('ACESSO NEGADO')