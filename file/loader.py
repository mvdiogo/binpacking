''' loader'''
import sys
import itertools
from file.create_file import createFile  # pylint: disable=import-error


def loader():
    ''' loader'''
    try:
        nome_arquivo = sys.argv[1]
        with open(sys.argv[1],"r", encoding="utf-8") as file:
            i = 0
            peso = []
            lines = file.read().splitlines()
            capacidade = int(lines[0].split(" ")[1].rstrip())
            lines = lines[1:]
            for _ in lines:
                peso.append((lines[i].split(" ")))
                i += 1
            peso = list(itertools.chain(*peso))
            peso = filter(None, peso)  # eliminar os vazios
            peso = list(map(int, peso))  # converter para inteiro
    except Exception:
        x = input("Você quer criar um novo arquivo?(s/n)")
        if x == "s":
            print("Create file")
            createFile()
        else:
            print("** To run the algorithm correctly please type: **")
            print("** python3 bl.py ./file/name_of_file.txt **")
            sys.exit()
    else:
        file.close()
    return peso, capacidade, nome_arquivo
