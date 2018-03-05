#!/usr/bin/env python
# -*- coding: utf-8 -*-
menu_del_dia_file = open("menu_del_dia.txt", "w+")

print 'Bienvenido al programa'

menu = {}

while True:
    plato_principal = raw_input("Escriba el plato: ")
    precio = float(raw_input("Escriba el precio: "))
    menu[plato_principal] = {"Precio": precio}
    print menu

    new = raw_input("¿Quieres añadir algún plato más? (yes/no) ")

    if new.lower() == "no":
        break

print "Menú del día: %s" % menu
menu_del_dia_file.write("Menú del día: \n")
for k,v in menu.items():
    print "- " + k + " = " + str(v["Precio"]) + "€"
    menu_del_dia_file.write(k + " = " + str(v["Precio"]) + " €" "\n")
print "Gracias por usar el programa"

menu_del_dia_file.close()