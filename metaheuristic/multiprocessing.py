'''Multiprocessing'''
import concurrent.futures

from metaheuristic.binpackage import BinPackage


def paralelismo(
    best_bin, bolsa, lista_bolsa, capacidade, interacoes, processosParalelo
):
    '''paralelismo'''
    worst_bin = best_bin
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [
            executor.submit(
                BinPackage, bolsa, lista_bolsa, capacidade, interacoes
            )
            for _ in range(processosParalelo)
        ]
        for f in concurrent.futures.as_completed(results, timeout=None):
            if best_bin < len(f.result().__dict__["lista_bolsa"]):
                worst_bin = len(f.result().__dict__["lista_bolsa"])
            else:
                best_bin = len(f.result().__dict__["lista_bolsa"])
                lista_bolsa = f.result().__dict__["lista_bolsa"]
                bolsa = f.result().__dict__["bolsa"]
        else:
            print(f"Diminuiu o tamanho da bolsa: {best_bin}")
            if best_bin != worst_bin:
                bolsa, lista_bolsa = paralelismo(
                    best_bin,
                    bolsa,
                    lista_bolsa,
                    capacidade,
                    interacoes,
                    processosParalelo,
                )
            else:
                print("fim - Multiprocessing")
                print(best_bin)
    return bolsa, lista_bolsa
