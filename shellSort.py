#Fonte: https://rosettacode.org/wiki/Sorting_algorithms/Shell_sort

from random import randint
import time

def shell(seq):
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
 
lista = []
tamanho = 50000
for i in range(tamanho):
    lista.append(randint(1,100000))

ini = time.time()
shell(lista)
fim = time.time()

print("Tamanha da entrada: ", tamanho)
print("Tempo de Execução: ", fim-ini)
# print(lista)