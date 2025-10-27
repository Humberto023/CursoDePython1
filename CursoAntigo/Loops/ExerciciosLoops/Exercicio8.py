#Contador de vogais

palavra = input('Digite uma palavra: ')
vogais = 0
consoantes = 0

for letra in palavra:
    #verifica se a letra é uma vogal minuscula ou maiuscula
    if letra.lower() in 'aeiou':
        vogais += 1
    elif letra.lower() in 'bcdfghjklmnpqrstvwxyz':
        consoantes += 1

print(f'A quantidade de vogais que {palavra} possui é de {vogais} e {consoantes} consoantes')
