# Questão 14 - Função validadora de senha
# Crie uma função validar_senha(senha, tamanho_minimo=8, requer_numero=True, requer_maiuscula=True) que:
#
# Verifica se a senha tem pelo menos tamanho_minimo caracteres
# Se requer_numero=True, verifica se tem pelo menos 1 número
# Se requer_maiuscula=True, verifica se tem pelo menos 1 letra maiúscula
# Retorna True se válida, False se não

def validar_senha(senha,tamanho_minimo = 8,requer_numero=True, requer_maiuscula = True):
    #Irá contar quantos digitos possui a string e será comparado com o tamanho mínimo já definido
    if len(senha) < tamanho_minimo:
        return False #Se a quantidade de digitos da senha for menor, retornaraá falso

        #So executará se requer_numero for TRUE, se for false nem verifica
        #"For req" percorre cada caractere
        #is.digit irá verificar se o caractere é um numero, sendo req cada letra ou numero
        #Any retornara TRUE se ao menos 1 caractere tiver presente
        #Mas como tem o "And not" ficará dessa forma
        #Se requer numero exige UM numero e NÃO tem número, retorne false
    #se precisa de num e não TEM "req" = numero dentro de senha, retorne falso
    if requer_numero and not any(req.isdigit() for req in senha):  #req irá verificar se o caractere digitado é um número, o any serve para retornar true se qualquer número for digitado
        return False #

    #req.issupper irá verificar cada caracetere para ver se é maisuculo
    #se quer maiusculo e NÃO TEM "req" = maisuculo dentro de senha, retorne falso
    if requer_maiuscula and not any(req.isupper() for req in senha):  #req verificará se a letra digitada é maiuscula, o any retorna true se houver ao menos uma letra maiuscula
        return False

    return True

print(validar_senha("Abc12345"))  # ✅ True
print(validar_senha("abc12345"))  # ❌ False (sem maiúscula)
print(validar_senha("ABCDEFGH"))  # ❌ False (sem número)
print(validar_senha("Abc1"))      # ❌ False (curta)