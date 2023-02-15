import time


def binpack(peso, capacidade, inicio):
    w = 0
    bolsa = []
    lista_bolsa = []
    bolsa.append(0)
    lista_bolsa.append([])
    tamanho_bolsa = sum(peso) // capacidade
    itens = len(peso)
    i = 0
    tamanho_bolsa = tamanho_bolsa * 2  # flag para comparar antigo com novo

    laco = 0
    s = 0  #
    j = 0  # teto bolsa

    peso = sorted(peso, reverse=True)

    top = 1
    for w in range(0, top):  # top):
        s = 0
        bolsa = []
        bolsa.append(0)
        lista_bolsa = [[]]
        i = 0
        j = 0
        while capacidade < int(peso[i]):  # nao cabe
            i += 1

        while i < itens:

            while capacidade * 0.51 <= (int(peso[i])):  # enche a mochila
                bolsa[j] += peso[i]
                lista_bolsa[j].append(peso[i])
                j += 1
                bolsa.append(0)
                lista_bolsa.append([])
                i += 1
            laco = 0
            while laco == 0:
                for s in range(0, j + 1):  # procura bolsa
                    if peso[i] == (capacidade - bolsa[s]) and laco == 0:
                        bolsa[s] += peso[i]
                        lista_bolsa[s].append(peso[i])
                        # print("best fit")
                        laco = 1
                    elif peso[i] < (capacidade - bolsa[s]) and laco == 0:
                        bolsa[s] += peso[i]
                        lista_bolsa[s].append(peso[i])
                        # print("tem vaga bolsa")
                        laco = 1
                    elif peso[i] > (capacidade - bolsa[s]) and laco == 0:
                        if j == s:
                            # print("add bolsa")
                            j += 1
                            s += 1
                            bolsa.append(peso[i])
                            lista_bolsa.append([])
                            lista_bolsa[s].append(peso[i])
                            laco = 1
            i += 1
        if len(lista_bolsa) < tamanho_bolsa:
            bolsa_otima = bolsa
            bolsa_otima_guloso = bolsa
            lista_bolsa_otima_guloso = lista_bolsa
            lista_bolsa_otima = lista_bolsa
            tamanho_bolsa = len(lista_bolsa_otima)
            print("Tamanho bolsa Best Fit= {}".format(len(lista_bolsa_otima)))
            print("Teto minimo= {}".format(tamanho_bolsa))
            fim = time.time()
            print("Tempo total em segundos= {}".format(fim - inicio))
    return (
        tamanho_bolsa,
        bolsa_otima_guloso,
        lista_bolsa_otima_guloso,
        bolsa_otima,
        lista_bolsa_otima,
    )
