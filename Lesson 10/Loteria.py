#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
import random

def main():
    print 'Welcome to the Lottery numbers generator.'
    opcion = int(raw_input('Please enter how many random numbers would you like to have: '))
    try:
        x = int(opcion)
        print numero_aleatorio(x)
    except ValueError:
        print "Por favor inserte un numero"

    print "Gracias por participar"


def numero_aleatorio(x):
    numero_aleatorio_lista = []
    while True:
        if len(numero_aleatorio_lista) == x:
            break

        numero_aleatorio = randint(0, 9)

        if numero_aleatorio not in numero_aleatorio_lista:
            numero_aleatorio_lista.append(numero_aleatorio)

    return numero_aleatorio_lista

if __name__ == "__main__":
    main()