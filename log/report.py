'''Create report'''
def report(
    nome_arquivo,
    capacidade,
    interacoes_total,
    tamanho_bolsa,
    bolsa_otima_guloso,
    bolsa,
    peso,
    fim,
    inicio,
    lista_bolsa,
):
    '''
    Create report file
    >>> report()
    '''
    file_path = "./log/rep_bestfitcominteações"
    with open(file_path,"a", encoding="utf-8") as arq:
        arq.write(
            "Guloso best fit com interação de troca de itens para diminuir bolsa "
        )
        arq.write("\n")
        arq.write(f"Nome d arquivo ={nome_arquivo}\n")
        arq.write(f"Capacidade do bin = {capacidade}\n")
        arq.write(f"Quantidade de interações = {interacoes_total}\n")
        arq.write(f"Teto mínimo= {tamanho_bolsa}\n")
        arq.write(f"Quant bolsas ótimo guloso = {len(bolsa_otima_guloso)}\n")
        arq.write(f"Quant bolsas ótimo  = {len(bolsa)}\n")
        arq.write(f"Quantidade de itens = {len(peso)}\n")
        arq.write(f"Soma itens = {sum(peso)}\n")
        arq.write(f"Tempo total em segundos= {fim - inicio}\n")
        arq.write(f"Peso dos itens das bolsas= {bolsa}\n")

        arq.write(f"Lista itens bolsa= {lista_bolsa}\n")
        arq.write("----------------------------------")
    arq.close()
