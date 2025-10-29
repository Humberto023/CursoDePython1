#List comprehension
    #Mais simples de se escrever
    #Utilizado quando você precisa criar uma nova lista a partir de uma existente

frutas1 = [ 'abacate', 'banana', 'morango', 'kiwi', 'abacaxi']




# frutas2 = [ ]

# for iten in frutas1:
#     if 'b' in iten:
#         frutas2.append(iten)


frutas2 = [iten for iten in frutas1 if 'n' in iten]

print(frutas2)