
# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox

master = Tkinter.Tk()

menu_del_dia_file = open("menu_del_dia.txt", "w+")

label_bienvenida = Tkinter.Label(master, text='Bienvenido al programa')
label_bienvenida.pack()
plato_principal = Tkinter.Entry(master)
plato_principal.pack()
precio = Tkinter.Entry(master)
precio.pack()

menu = {}

label_menu = Tkinter.Label(master, menu)
label_menu.pack()
new = Tkinter.Entry(master)
new.pack()

while True:
    plato_principal = raw_input("Escriba el plato: ")
    precio = float(raw_input("Escriba el precio: "))
    menu[plato_principal] = {"Precio": precio}
    print menu

    new = raw_input("¿Quieres añadir algún plato más? (yes/no) ")

    if new.lower() == "no" or new.lower() == "n":
        break

print "Menú del día: %s" % menu
menu_del_dia_file.write("Menú del día: \n")
def final():
    for k,v in menu.items():
        print "- " + k + " = " + str(v["Precio"]) + "€"
        menu_del_dia_file.write(k + " = " + str(v["Precio"]) + " €" "\n")

tkMessageBox.showinfo("Menú del día: ", menu)
label_despedida = Tkinter.Label(master, text= "Gracias por usar el programa")
label_despedida.pack()
submit = Tkinter.Button(master, text="Enviar", command=final)
submit.pack()
menu_del_dia_file.close()

master.mainloop()