# Adivinhação

# Primeiro chute
num = int(input("Digite um número: "))

# Enquanto o chute for diferente de 8
while num != 8:
    print('Número errado!')

    # Pede um novo chute
    num = int(input('Digite novamente: '))

    # Dá dicas
    if num >= 100:  # números muito grandes
        print('Está muito longe')
    elif num < 8:   # números menores que 8
        print('Um pouco mais')
    elif num > 8:   # números maiores que 8 (e menores que 100)
        print('Um pouco menos')

# Quando sair do loop, o usuário acertou
print('Número correto!')
