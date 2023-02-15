'''Class thread and process'''
from typing import List, Any
from random import randint


class BinPackage:
    '''BinPackage'''
    def __init__(
        self,
        bolsa: List[int],
        lista_bolsa: List[int],
        capacidade: int,
        interacoes: int,
    ):
        self.bolsa = bolsa
        self.lista_bolsa = lista_bolsa
        self.interacoes = interacoes
        self.erros: List[Any] = []
        self.capacidade = capacidade
        self.run()

    def run(self):
        '''chose process or thread to run'''
        self.process()
        # self.thread() not working need fix

    def thread(self):
        '''thread need to fix'''
        j = 0
        pl = 1
        while pl < self.interacoes:
            try:
                j = randint(0, len(self.bolsa) - 1)  # bolsa inicio
                y = randint(
                    0, len(self.bolsa) - 1
                )  # bolsa fim ver ordenar o tirar o min
                z = randint(0, len(self.lista_bolsa[j]) - 1)  # item inicio
                w = randint(0, len(self.lista_bolsa[y]) - 1)  # item fim
                tmp = self.lista_bolsa[y][w]  # pylynch: disable=unused-variable
                tmp = self.lista_bolsa[j][z]  # pylynch: disable=unused-variable
                tmp = self.bolsa[j]  # pylynch: disable=unused-variable
                if self.bolsa[j] == self.capacidade:
                    j += 1
                else:
                    if (
                        self.lista_bolsa[y][w] <= self.capacidade - self.bolsa[j]
                    ):  # inserssão ulti -item>cap-bolsa
                        self.bolsa[j] += self.lista_bolsa[y][w]
                        self.bolsa[y] -= self.lista_bolsa[y][w]
                        self.lista_bolsa[j].append(self.lista_bolsa[y][w])
                        self.lista_bolsa[y].remove(self.lista_bolsa[y][w])
                        if 0 in self.bolsa:
                            pl = self.interacoes
                            # print(f"*Diminuiu o tamanho da bolsa - {len(self.lista_bolsa)}")
                            self.bolsa = [x for x in self.bolsa if x != 0]
                            self.lista_bolsa = [x for x in self.lista_bolsa if x != []]
                            break
                    elif (
                        self.lista_bolsa[y][w] - self.lista_bolsa[j][z]
                        <= self.capacidade - self.bolsa[j]
                    ):  # substituição ulti -item>cap-bolsa
                        if (
                            self.lista_bolsa[j][z] - self.lista_bolsa[y][w]
                            <= self.capacidade - self.bolsa[y]
                        ):
                            #self.lock.acquire(blocking=True, timeout=1)
                            self.bolsa[j] += self.lista_bolsa[y][w]
                            self.bolsa[y] -= self.lista_bolsa[y][w]
                            self.bolsa[j] -= self.lista_bolsa[j][z]
                            self.bolsa[y] += self.lista_bolsa[j][z]
                            self.lista_bolsa[j].append(self.lista_bolsa[y][w])
                            self.lista_bolsa[y].remove(self.lista_bolsa[y][w])
                            self.lista_bolsa[y].append(self.lista_bolsa[j][z])
                            self.lista_bolsa[j].remove(self.lista_bolsa[j][z])
                            #self.lock.release()
                pl += 1
            except Exception as err:
                print(f"Exception:{err.args}")
            finally:
                pass
        return self.bolsa, self.lista_bolsa, self.interacoes

    def process(self):
        '''process'''
        j = 0
        pl = 1
        while pl < self.interacoes:
            try:
                j = randint(0, len(self.bolsa) - 1)  # bolsa inicio
                y = randint(
                    0, len(self.bolsa) - 1
                )  # bolsa fim ver ordenar o tirar o min
                z = randint(0, len(self.lista_bolsa[j]) - 1)  # item inicio
                w = randint(0, len(self.lista_bolsa[y]) - 1)  # item fim
            except Exception as err:
                print(f"Exception:{err.args}")
                break
            if self.bolsa[j] == self.capacidade:
                j += 1
            else:
                if (
                    self.lista_bolsa[y][w] <= self.capacidade - self.bolsa[j]
                ):  # inserssão ulti -item>cap-bolsa
                    self.bolsa[j] += self.lista_bolsa[y][w]
                    self.bolsa[y] -= self.lista_bolsa[y][w]
                    self.lista_bolsa[j].append(self.lista_bolsa[y][w])
                    self.lista_bolsa[y].remove(self.lista_bolsa[y][w])
                    if 0 in self.bolsa:
                        pl = self.interacoes
                        # print(f"*Diminuiu o tamanho da bolsa - {len(self.lista_bolsa)}")
                        self.bolsa = [x for x in self.bolsa if x != 0]
                        self.lista_bolsa = [x for x in self.lista_bolsa if x != []]
                        break
                elif (
                    self.lista_bolsa[y][w] - self.lista_bolsa[j][z]
                    <= self.capacidade - self.bolsa[j]
                ):  # substituição ulti -item>cap-bolsa
                    if (
                        self.lista_bolsa[j][z] - self.lista_bolsa[y][w]
                        <= self.capacidade - self.bolsa[y]
                    ):
                        self.bolsa[j] += self.lista_bolsa[y][w]
                        self.bolsa[y] -= self.lista_bolsa[y][w]
                        self.bolsa[j] -= self.lista_bolsa[j][z]
                        self.bolsa[y] += self.lista_bolsa[j][z]
                        self.lista_bolsa[j].append(self.lista_bolsa[y][w])
                        self.lista_bolsa[y].remove(self.lista_bolsa[y][w])
                        self.lista_bolsa[y].append(self.lista_bolsa[j][z])
                        self.lista_bolsa[j].remove(self.lista_bolsa[j][z])
            pl += 1
        return self.bolsa, self.lista_bolsa, self.interacoes
