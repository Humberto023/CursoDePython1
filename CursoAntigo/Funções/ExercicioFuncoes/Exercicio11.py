
def criar_perfil(nome,idade,*hobbies,**contatos):

    '''
    Cria um perfil completo do usuário:

    nome: Obrigatório
    idade: obrigatório
    *hobbies: quantidade variávels de hobbies
    **contatos: informações de contato nomeadas

    '''


    perfil = {
        'Nome': nome,
        'Idade': idade,
        'Hobbies': list(hobbies),
        'Contatos': contatos
    }
    return perfil

# ========================================
# TESTANDO A FUNÇÃO1
# ========================================

print("=" * 50)
print("teste 1' : Perfil completo")
print("=" * 50)

# perfil1 = criar_perfil(
#     "Humberto Junior",
#     28,
#     "Violao","volei","programação",
#     email = "Betinho040805@gmail.com",
#     telefone = 83998111142,
#     instagram = "@083_beto"
# )

# Criando uma função para que seja utilizado em todo dicionário
def exibir_perfil_bonito(perfil):
    print("Nome", perfil['Nome'])
    print("Idade", perfil['Idade'])
    #Hobbies
    if perfil['Hobbies']:
        print("Hobbies", ", ".join(perfil['Hobbies']))
    else:
        print("Hobbies: Não informado")

    if perfil['Contatos']:
        for tipo, info in perfil['Contatos'].items():
            print(f' - {tipo}: {info}')
    else:
        print("Contatos: Não informado")
#
# print("Nome", perfil1['Nome'])
# print("Idade", perfil1['Idade'])
# print("Hobbies",", ".join(perfil1['Hobbies']))
# print("Contatos")
# for tipo, info in perfil1['Contatos'].items():
#     print(f' - {tipo}: {info}')
#
# print("\n" + "=" * 50)
# print("TESTE 2: Só o básico (sem hobbies e contatos)")
# print("=" * 50)
#
# perfil2 = criar_perfil(
#     "Vera Lucia",
#     57,
#     "Brigar","Fazer faxin", "Cuidar de tobby",
#     email = "Veralucia110171@gmailcom",
#     telefone = 83987735237,
#     linkedin = "VeraLcNascimento"
# )
#
# print("Nome", perfil2['Nome'])
# print("Idade", perfil2['Idade'])
# print("Hobbies",", ".join(perfil2['Hobbies']))
# print(f"Contatos:")
# for tipo, info in perfil2['Contatos'].items():
#     print(f' - {tipo}: {info}')


perfil4 = criar_perfil(
    "Humberto Nascimento",
    53,
    "Consertar carro","Pintar paredes", "Dormir cedo",
    email= "humberto_autoeletrica@outlook.com",
    telefone = 8398078465,
    instagram = "betoautoeletrica"
)

exibir_perfil_bonito(perfil4)