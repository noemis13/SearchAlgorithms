#Fonte: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html

from random import randint
import time

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

lista = []
tamanho = 10000
for i in range(tamanho):
    lista.append(randint(1,10000))

ini = time.time()
selectionSort(lista)
fim = time.time()

print("Tamanha da entrada: ", tamanho)
print("Tempo de Execução: ", fim-ini)
# print(lista)