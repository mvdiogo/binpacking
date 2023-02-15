''' multithreating not working'''
import os
import concurrent.futures
import threading

from threading import Lock, excepthook, Barrier

from metaheuristic.binpackage import BinPackage

def custom_hook(args):
    # report the failure
    # lock.release()
    print(f'Thread failed: {args.exc_value}')
    pass


def multiThread(
    best_bin, bolsa, lista_bolsa, capacidade, interacoes, processosParalelo
):
    ''' multithreating not working'''
    lock = Lock()
    barrier = Barrier(interacoes, timeout=1)
    threading.excepthook = custom_hook
    worst_bin = best_bin
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = [
            executor.submit(
                BinPackage, bolsa, lista_bolsa, capacidade, interacoes, lock
            )
            for _ in range(processosParalelo)
        ]
        for f in concurrent.futures.as_completed(results):
            if best_bin < len(f.result().__dict__["lista_bolsa"]):
                worst_bin = len(f.result().__dict__["lista_bolsa"])
            else:
                best_bin = len(f.result().__dict__["lista_bolsa"])
                lista_bolsa = f.result().__dict__["lista_bolsa"]
                bolsa = f.result().__dict__["bolsa"]
        else:
            print("terminou for")
            print(f"best_bin:{best_bin}")
            print(f"worst_bin:{worst_bin}")
            if best_bin != worst_bin:
                bolsa, lista_bolsa = multiThread(
                    best_bin,
                    bolsa,
                    lista_bolsa,
                    capacidade,
                    interacoes,
                    processosParalelo,
                )
            else:
                print("fim - ThreadPoolExecutor")
                print(best_bin)
    return bolsa, lista_bolsa
