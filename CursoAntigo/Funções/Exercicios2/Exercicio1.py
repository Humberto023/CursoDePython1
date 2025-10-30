#sistema de biblioteca

def cadastrar_livro(titulo, autor, ano,  *generos, **informacoes):
    livro = {
        'Titulo': titulo,
        'Autor': autor,
        'Ano': int(ano),
        'Genero': list(generos),
        'informacoes': informacoes,
    }
    return livro

def mostrar_livro(livro):
    print('Titulo:', livro['Titulo'])
    print('Autor:', livro['Autor'])
    print('Ano:', livro['Ano'])
    #Generos
    if livro['Genero']: #Irá verificar se um gênero foi adicionado
        #Join é utilizado para unir todos os dados da lista em uma única string
        print('Genero: ', ', '.join(livro['Genero']))
    else:
        print('Genero: Não informado')

    if livro['informacoes']:
        for dados, itens in livro['informacoes'].items():
            print(f' - {dados}: {itens}')
    else:
        print("Dados não informados")
    return livro

livro1 = cadastrar_livro(
    "As cronicas de narnia",
    "Humberto",
    1998,
    "Drama","Fantasia","acao",
    quantidade_paginas = 397,
    volumes = 9,

)

mostrar_livro(livro1)