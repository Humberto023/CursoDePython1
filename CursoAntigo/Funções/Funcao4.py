
#default = aquele que você define o valor do parametro  (caso fosse colocar quantidade = algo)
#Non-defaulta = aquele que você não define o valor do parametro   (seria o nome) 


def boas_vindas(nome,quantidade=6 ):
    print(f'Ola {nome}')
    print(f'Temos {str(quantidade)} laptopes em stoque')

boas_vindas('Bob')