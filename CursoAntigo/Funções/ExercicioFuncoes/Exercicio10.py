def exibir_dados(**dados):
    print("=== DADOS DO USUÁRIO ===")
    for chave, valor in dados.items(): #Sempre que for lido um dado no for, ele irá fazer a print abaixo   #Roda 1 vez, repete
        print(f'{chave}: {valor}') #dessa forma printando a cada dado aplicado dentro do for    #Roda 1 vez e repete até que não tenha mais nada na lista
    print("========================")

exibir_dados(nome='João', cidade='São Paulo', idade=29, profissao='Dev')
