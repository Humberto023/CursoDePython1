#Print ou Return em Funções
#Print é uma tarefa realizada, aquilo que foi pedido, mas não foi armazenado nada

#Return,
def cliente1(nome):
    print(f'Ola {nome}')


def cliente2(nome):
    return f'Ola {nome}'


cliente1('Maria')
y = cliente2('Jose')


print(y)


'''Basicamente o return apenas guarda a infromação que foi lhe passada e aguarda para que seja chamado em um outro momento,
O que foi que ocorreu na parte do Y, onde foi atribuido um valor 'Return' para o Y, assim apresentando'''