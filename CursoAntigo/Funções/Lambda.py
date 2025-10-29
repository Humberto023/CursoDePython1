#Lambda Function
    #É uma função pequena sem nome
    # Pode ter vários argumentos mas somente 1 expressão
    # Muito utilizado dentro de outras funções
    # codigo mais clean


# def somar (x):
#     return x + 10
#
# print(somar(2))
          #argumento   #expressao
somar10 = lambda x, y : x + y + 10
print(somar10(2,4))