'''
!/usr/bin/env python
-*- coding: utf-8 -*-
Disciplina de Projeto e Análise de Algoritmos

Professor: Valdisio

Autores: Marcus

Metaheurística Busca Local - bin packing

Objetivo: menor quantidade de cestos possível

exemplo: python bl.py nomedoarquivoaimportar.txt
'''

import time
import os

from file.loader import loader
from greedy.serializing import binpack
from metaheuristic.multiprocessing import paralelismo
# from metaheuristic.multithreading import multiThread
from metaheuristic.serializing import serializing
from log.report import report
from file.create_file import createFile


def main() -> None:
    ''' Greedy and metaheuristic'''
    peso, capacidade, nome_arquivo = loader()

    inicio = time.time()
    print("Greedy")
    (
        tamanho_bolsa,
        bolsa_otima_guloso,
        lista_bolsa_otima_guloso,
        bolsa_otima,
        lista_bolsa_otima,
    ) = binpack(peso, capacidade, inicio)

    bolsa = bolsa_otima

    lista_bolsa = lista_bolsa_otima

    processos_paralelo = os.cpu_count() // 2

    interacoes = 1000000

    best_bin = len(lista_bolsa_otima_guloso)

    # metaheuristic
    x = input("1. Serial, 2. Processor, 3. Thread (not working), 4. Create file:")
    inicio = time.time()
    if x == "1":
        # -- serializing --
        print("Serializing")
        bolsa, lista_bolsa = serializing(
            bolsa, lista_bolsa, capacidade, interacoes, processos_paralelo
        )
    elif x == "2":
        # -- multiprocessing --
        print("Multiprocessing")
        bolsa, lista_bolsa = paralelismo(
            best_bin, bolsa, lista_bolsa, capacidade, interacoes, processos_paralelo
        )
    elif x == "3":
        # multithreading
        # bolsa, lista_bolsa = multiThread(
        #    best_bin, bolsa, lista_bolsa, capacidade, interacoes, processos_paralelo
        # )
        print("not working")
    elif x == "4":
        print("Create file")
        createFile()
    else:
        print("By!!")

    fim = time.time()
    interacoes_total = int(processos_paralelo) * int(interacoes)
    report(
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
    )
    print(f"Tempo em segundos= {fim - inicio}")


if __name__ == "__main__":
    main()
