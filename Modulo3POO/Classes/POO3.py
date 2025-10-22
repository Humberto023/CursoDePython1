class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Cargo: {self.cargo}')

    def promover(self, novo_cargo):
            print(f'{self.nome} foi promovido para nova funcao de {novo_cargo}!')

    def atualizar_idade(self, nova_idade):
        if nova_idade > self.idade:
            print(f'Atualizando idade de {self.idade} para {nova_idade}')
        else:
            print('A nova idade tem que ser maior que a antiga')




colaborador1 = Pessoa('Ana', 36 , 'Assistente junior')
colaborador2 = Pessoa('Joao', 23 , 'Dev Junior')



colaborador1.informacoes()
colaborador1.promover('Assistente pleno')
colaborador1.atualizar_idade(32)
