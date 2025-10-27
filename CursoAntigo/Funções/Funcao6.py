#Vários argumentos xargs com números

#Criasr uma funão que soma varios numeros


def soma(*numeros):  #O * quer dizer que será muitos números utiizados
    resultado = 0  #Inicia-se em zero
    for num in numeros:  #Para todo 'num' que tiver dentro de 'numeros', pegue o resultado e some com o número
        resultado += num  # ou seja, para todo num que for digitado dentro da função, será imprimido isso
    return resultado

x = (soma(2,3,4,7))

print(x)