#Verificando itens em uma lista

cor_cliente = input('Digite a cor desejada: ')

cores = ['amarelo', 'verde','azul', 'vermelho']
                 #Isso serve para converter todas as letras para minuscula 
if cor_cliente.lower() in cores:
    print('Em estoque')
else:
    print('Em falta')