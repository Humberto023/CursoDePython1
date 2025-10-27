#Parâmetros SEM valor padrão (obrigatórios) devem vir ANTES dos parâmetros COM valor padrão (opcionais)!



def cadastrar_usuario( idade,nome="Anônimo", cidade="Não informada"):
    return f"{nome}, {idade} anos, de {cidade}"

x = cadastrar_usuario(5)
print(x)