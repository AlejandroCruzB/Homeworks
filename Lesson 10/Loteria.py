#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
print 'Welcome to the Lottery numbers generator.'
opcion = int(raw_input('Please enter how many random numbers would you like to have: '))
opciones_restantes = opcion
numero_aleatorio=[]
while opciones_restantes > 0:

    numero_aleatorio = randint(0, 50)
    print numero_aleatorio,
    opciones_restantes -= 1

print 'Gracias por participar'
