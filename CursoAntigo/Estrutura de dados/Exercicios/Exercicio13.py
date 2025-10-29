# SETS (Questões 13-16)
# Questão 13 - Criando sets
# Crie dois sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Descubra:
#
# Quais números aparecem nos dois sets? (interseção)
# Quais números são exclusivos de cada set? (diferença)
# União de todos os números


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set3 = set1.intersection(set2)
set4 = set1.difference(set2)
set5 = set1.union(set2)
print(set3)
print(set4)
print(set5)