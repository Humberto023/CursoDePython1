usuario = input('Digite o seu usuário ')
senha = input('Digite sua senha ')

login_valido = usuario == 'Beto' and senha == '123456'

print(f'login permitido: {login_valido}')