#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def quicksort(lista):
    if len(lista) > 1:
        pivote = lista[0] # Escogemos el pivote, por defecto será el primer elemento de la lista
        menores = [x for x in lista[1:] if x < pivote] # Una sublista con los elementos menores o iguales al pivote
        mayores = [x for x in lista[1:] if x >= pivote]  # Una sublista con los elementos mayores o iguales al pivote
        return quicksort(menores) + [pivote] + quicksort(mayores) # Llamada recursiva al algoritmo sobre las sublistas
    else:
        return lista # Ya ordenada


if __name__ == '__main__':
    l = random.sample(xrange(100), 10) # Toma 10 números aleatorios, desde el 0 al 100
    print "Lista aleatoria:", l
    print "Lista ordenada :", quicksort(l)
