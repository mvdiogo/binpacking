'''serializing'''
from random import randint


def serializing(bolsa, lista_bolsa, capacidade, interacoes, processos_paralelo):
    '''serializing'''
    pl = 1
    while pl < interacoes * processos_paralelo:
        j = randint(0, len(bolsa) - 1)  # bolsa inicio
        y = randint(0, len(bolsa) - 1)  # bolsa fim ver ordenar o tirar o min
        z = randint(0, len(lista_bolsa[j]) - 1)  # item inicio
        w = randint(0, len(lista_bolsa[y]) - 1)  # item fim
        if bolsa[j] == capacidade:
            j += 1
        else:
            if (
                lista_bolsa[y][w] <= capacidade - bolsa[j]
            ):  # inserssão ulti -item>cap-bolsa
                bolsa[j] += lista_bolsa[y][w]
                bolsa[y] -= lista_bolsa[y][w]
                lista_bolsa[j].append(lista_bolsa[y][w])
                lista_bolsa[y].remove(lista_bolsa[y][w])
                if 0 in bolsa:
                    # print(bolsa)
                    # print(lista_bolsa)
                    print(f"Diminuiu o tamanho da bolsa: {len(lista_bolsa)} ")
                    bolsa = [x for x in bolsa if x != 0]
                    lista_bolsa = [x for x in lista_bolsa if x != []]
            elif (
                lista_bolsa[y][w] - lista_bolsa[j][z] <= capacidade - bolsa[j]
            ):  # substituição ulti -item>cap-bolsa
                if lista_bolsa[j][z] - lista_bolsa[y][w] <= capacidade - bolsa[y]:
                    bolsa[j] += lista_bolsa[y][w]
                    bolsa[y] -= lista_bolsa[y][w]
                    bolsa[j] -= lista_bolsa[j][z]
                    bolsa[y] += lista_bolsa[j][z]
                    lista_bolsa[j].append(lista_bolsa[y][w])
                    lista_bolsa[y].remove(lista_bolsa[y][w])
                    lista_bolsa[y].append(lista_bolsa[j][z])
                    lista_bolsa[j].remove(lista_bolsa[j][z])
        pl += 1
    print("fim - serializing")
    return bolsa, lista_bolsa
