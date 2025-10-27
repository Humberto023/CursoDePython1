
def criar_perfil(nome,idade,*hobbies,**contatos):
    return nome,idade


x= criar_perfil('Paulo', 18, atividade_fisica = 'Futebol', email='betinho0408905@gmial.com')
print(x)

