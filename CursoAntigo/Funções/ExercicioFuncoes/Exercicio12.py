def calcular_media(*notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

print(calcular_media(5,4,6,7,8))




