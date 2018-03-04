#!/usr/bin/env python
# -*- coding: utf-8 -*-

menu = {}

print "Bienvenido al menú del día"
while True:
    nombre = raw_input('Nombre del menú: ')
    precio = float(raw_input("Precio del plato: "))

    # menu[nombre] = precio
    menu[nombre] = {"nombre": nombre, "precio": precio, }

    print menu

    salir = raw_input("¿Quieres salir del menú? (y/n)")
    if salir.lower() == "y":
        break
print menu
print menu["paella"][
    "precio"]# esta función lo que hace es print el precio de un plato que hemos mencionado antes, si no se ha mencionado antes dará error
print "Hasta la próxima."