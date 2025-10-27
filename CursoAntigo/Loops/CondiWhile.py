#Condições com WhileLoop
#Publicar um produto com comissão de 10% se for acima de R$20


valor = int(input('Digite um valor: '))

while valor > 20:
    valor = (valor * 0.10) +valor
    print(f'O valor final de seu produto será de R$ {valor:.2f}')
    break