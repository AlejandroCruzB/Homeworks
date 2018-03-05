#!/usr/bin/env python
# -*- coding: utf-8 -*-
vehiculos_file = open("vehiculos.txt", "w+")
class Vehiculo:
    def __init__(self, marca, modelo, km, date):
        self.marca = marca
        self.modelo = modelo
        self.km = km
        self.date = date


    def get_full_name(self):
        return self.marca + " " + self.modelo


def list_all_vehiculos(vehiculos):
    for index, coches in enumerate(vehiculos):
        print "ID: " + str(index+1)  # index
        print coches.get_full_name()
        print coches.date
        print coches.km
        print ""  # empty line

    if not vehiculos:
        print "You don't have any vehicle in your list."


def add_new_vehiculo(vehiculos):
    marca = raw_input("Please enter marca: ")
    modelo = raw_input("Please enter model: ")
    km = raw_input("Please enter km: ")
    date = raw_input("Please enter date: ")


    new = Vehiculo(marca=marca, modelo=modelo, km=km, date=date)
    vehiculos.append(new)

    print ""  # empty line
    print new.get_full_name() + " was successfully added to your list."


def edit_vehiculo(vehiculos):
    print "Select the number of the vehicle you'd like to edit:"

    for index, coches in enumerate(vehiculos):
        print str(index) + ") " + coches.get_full_name()

    print ""  # empty line
    selected_id = raw_input("What vehicle would you like to edit? (enter ID number): ")
    selected_vehiculo = vehiculos[int(selected_id)]

    new_date = raw_input("Please enter a new date for %s: " % selected_vehiculo.get_full_name())
    selected_vehiculo.date = new_date

    new_km = raw_input("Please enter a new km for %s: " % selected_vehiculo.get_full_name())
    selected_vehiculo.km = new_km

    print ""  # empty line
    print "Updated."





def main():



    print "Welcome to your List"


    Coche_A = Vehiculo(marca="Seat", modelo="Leon", km="39.429 km", date="05-02-2010")
    Coche_B = Vehiculo(marca="Mercedes", modelo="Clase C", km="89.429 km", date="2009")
    Coche_C = Vehiculo(marca="Audi", modelo="A5", km="109.429 km", date="2008")
    vehiculos = [Coche_A, Coche_B, Coche_C]



    while True:
        print ""  # empty line
        print "Please choose one of these options:"
        print "a) See all your list"
        print "b) Add a new vehicle"
        print "c) Edit a vehicle"
        print "d) Quit the program."
        print ""  # empty line

        selection = raw_input("Enter your selection (a, b, c, or d): ")
        print ""  # empty line

        if selection.lower() == "a":
            list_all_vehiculos(vehiculos)
        elif selection.lower() == "b":
            add_new_vehiculo(vehiculos)
        elif selection.lower() == "c":
            edit_vehiculo(vehiculos)
        elif selection.lower() == "d":
            print "Thank you for using List. Goodbye!"
            vehiculos_file.write("Lista: \n")
            for k in list_all_vehiculos(vehiculos):
                vehiculos_file.write("list_all_vehiculos(vehiculos) /n")
            break
        else:
            print "Sorry, I didn't understand your selection. Please try again."
            continue

vehiculos_file.close()

if __name__ == "__main__":
    main()