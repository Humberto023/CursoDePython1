

def soma_todos(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

print(soma_todos(2,3,4,7,10))

