def calcular_viagem(destino,dias,*acompanhantes,**custos):

    total_pessoas = 1 + len(acompanhantes)

    custo_total= sum(custos.values())
    custo_pessoa = custo_total/total_pessoas
    custo_dia = custo_total/dias

    viagem = {
        'Destino': destino,
        'Dias': dias,
        'Acompanhantes': ["Humberto"] + list(acompanhantes),
        'Custo Total': custo_total,
        'Custo Pessoa': custo_pessoa,
        'Custo Dia': custo_dia,

    }
    return viagem


def mostrar_bonito(viagem):
    print("Viagem: ", viagem['Destino'])
    print("Dias: ", viagem['Dias'])
    print("Acompanhantes: ",", ".join(viagem['Acompanhantes']))
    for chave,valor in viagem.items():
        if 'Custo' in chave:
            print(f"Gasto de {chave} de R$ {valor}")


Viagem = calcular_viagem(
    "Paris",
    7,
    "Maria", "João",
    hospedagem=1400,
    alimentacao=700,
    passagem=2400,
    passeios=500
)

mostrar_bonito(Viagem)