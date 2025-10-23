
compra_confirmada = True
dados_compra = 'Compra no valor de 12.50, e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('detalhes enviados para o seu e-mail')
        break
    else:
        print('Compra negada')
