# Verificação de senha

# Define a senha correta
senha_correta = 'beto'

# Pede a primeira tentativa
senha = input('Digite a senha: ')

# Enquanto a senha digitada for diferente da correta
while senha != senha_correta:
    print('Senha incorreta, tente novamente!')
    senha = input('Digite a senha novamente: ')

# Quando o usuário acerta, o loop termina
print('Senha correta!')
