def multiiplicar_print(x,y):
    print(x)
    print(y)

def multipicar_return(x,y):
    return x , y


resultado = multiiplicar_print(9,5)
x = multipicar_return(9,5)

print(x)
print(resultado)  #retornara none, por conta que o print não armazena nada, apenas coloca as info na tela, diferente do return que pode ser usado a qualquer momento