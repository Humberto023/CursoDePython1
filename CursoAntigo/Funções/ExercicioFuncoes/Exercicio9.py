

def encontrar_maior(*numeros):
    inicial = 0 #Iniciará em 0
    for num in numeros: #Para todo numero em numeros
        if num > inicial: #Compare o valor atual com o inicial
            inicial = num #Se for maior ele será o novo numero a ser comparado
    return inicial

x = encontrar_maior(2,3,4,7,8,29,45,37)

print(x)