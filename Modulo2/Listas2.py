#Lista se usa quando usa vários itens mutáveis, mudar
#Tuplas, um ou vários itens imutáveis
#Dicionários, quando precisa armazenar um item relacionado à uma chave; Usuários, endereços, produtos, configurações, etc
tarefas = []

tarefas.append('Estudar python com IA')
tarefas.append(' Limpar a casa')
tarefas.append('estudar para a prova')

print('Minhas tarefas diárias: ')
for tarefa in tarefas:
    print(f'Tarefa: {tarefa}')