'''create_file'''
from random import randint


def createFile():
    '''createFile'''
    qtd_objetos = 0
    size_bin = 0
    bolsa_itens = ""

    while True:
        qtd_objetos = int(input("Qual quantidade de objetos(ex:100):"))
        size_bin = int(input("Qual capacidade de cada pacote(ex:100):"))

        if qtd_objetos < 50:
            print("Por favor digite um valor maior que 50")
            continue
        else:
            if size_bin < 50:
                print("Por favor digite um valor maior que 50")
                continue
            else:
                break

    with open(f"./file/n{qtd_objetos}C{size_bin}.txt", "w", encoding="utf-8") as arq:
        variacao = randint(3, 6)
        for _ in range(qtd_objetos):
            bolsa_itens += " " + str(
                randint(int(size_bin / variacao), int(size_bin / variacao) * 2)
            )
        arq.write(f"{qtd_objetos} {size_bin}\n")
        arq.write(f"{bolsa_itens}")
    arq.close()
    print(bolsa_itens)
    print(f"Nome do arquivo: n{qtd_objetos}C{size_bin}.txt")
