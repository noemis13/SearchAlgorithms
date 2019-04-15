#Fonte: https://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python

from random import randint
import time

def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more
 
lista = []
tamanho = 50000
for i in range(tamanho):
    lista.append(randint(1,100000))

ini = time.time()
lista = quickSort(lista)
fim = time.time()

print("Tamanha da entrada: ", tamanho)
print("Tempo de Execução: ", fim-ini)
# print(lista)





