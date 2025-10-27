

def calculadora(operacao,num1,num2):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        return num1 / num2

x = calculadora('multiplicacao',24,56)

print(x)