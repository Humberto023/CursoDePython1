# Questão 16 - Sets com strings
# Dada a string texto = "banana":
#
# Converta para set e veja quais letras únicas existem
# Quantas letras únicas tem?


texto = 'banana'

letras_unicas = set(texto)

print(letras_unicas) #Irá imprimir todas letras que não se repetem, e quando se repte irá contar apppenas 1 vez
print(len(letras_unicas)) #Irá contar quantas há