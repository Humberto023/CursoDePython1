# Questão 15 - DESAFIO FINAL: Sistema de Pedidos
# Crie uma função fazer_pedido(cliente, *itens, **opcoes) que:
#
# cliente é o nome do cliente
# *itens são os produtos pedidos
# **opcoes podem incluir: entrega="sim", pagamento="cartão", cupom="DESC10"
#
# A função deve:
#
# Calcular o total (cada item custa R$ 10,00)
# Se tiver cupom "DESC10", dar 10% de desconto
# Se entrega="sim", adicionar R$ 5,00
# Retornar um dicionário com: cliente, itens, total, forma de pagamento
#
# Exemplo:
# fazer_pedido("João", "Pizza", "Refrigerante", "Sobremesa",
#              entrega="sim", pagamento="pix", cupom="DESC10")

def fazer_pedido(cliente, *itens, **opcoes):
    # Cada item custa R$10
    preco_item = 10

    # Calcula o total base multiplicando a quantidade de itens pelo preço de cada um
    total = len(itens) * preco_item



    # Verifica se há cupom e se é "DESC10" usando .get()
    # .get('cupom') busca a chave "cupom" em opcoes — se não existir, retorna None
    if opcoes.get('cupom') == "DESC10":
        total *= 0.9 # aplica 10% de desconto (multiplica por 0.9)
        # Cada item custa 10, o desconto que será aplicado será somente nos itens, a entrega não entra junto

    # Verifica se o cliente pediu entrega
    # .get('entrega') busca a chave "entrega" — se for "sim", adiciona R$5
    if opcoes.get('entrega') == "sim":
        total += 5

    # Arredonda o total para 2 casas decimais (ex: 27.333 → 27.33)
    total = round(total, 2)

    # Cria um dicionário com as informações do pedido
    pedido = {
        'Cliente': cliente,
        'Itens': list(itens),  # converte os itens em lista
        'Total': total,
        # Busca o tipo de pagamento com .get(), caso não tenha, mostra "não informado"
        'Pagamento': opcoes.get('pagamento', 'não informado')
    }

    return pedido

def mostrar_bonito(pedido):
    print("=" * 40)
    print(f"📦 Pedido de {pedido['Cliente']}") #Aqui irá pegar o valor que está dentro da chave CLIENTE
    print("=" * 40)

    # Itens
    if pedido['Itens']:
        print("🛒 Itens:", ", ".join(pedido['Itens'])) #O join irá unir as strings, devido que é uma lista
    else:
        print("🛒 Nenhum item informado")

    # Total
    print(f"💰 Total: R$ {pedido['Total']:.2f}") #Irá imprimir o total que foi registrado acima

    # Pagamento
    print(f"💳 Pagamento: {pedido['Pagamento']}") #Irá informar a forma de pagamento




# ==============================
# Testando a função
# ==============================

pedido1 = fazer_pedido(
    "João",
    "Pizza", "Refrigerante", "Sobremesa", "Pao com mortadela",
    entrega="sim",
    pagamento="pix",
    cupom="DESC10"
)

mostrar_bonito(pedido1)
