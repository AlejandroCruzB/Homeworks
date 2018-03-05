#!/usr/bin/env python
# -*- coding: utf-8 -*-

archivoadn = open('dna.txt')

aux = archivoadn.readline()
adn_autor = aux.split()

Caracteristicas_humanas = {}

Caracteristicas_humanas["Color_pelo"] = { "Negro" : "CCAGCAATCGC", "Marron": "GCCAGTGCCG", "Rubio" : "TTAGCTATCGC"},
Caracteristicas_humanas["Forma_facial"] = {"Cuadrada": "GCCACGG", "Redonda": "ACCACAA", "Ovalada" : "AGGCCTCA"},
Caracteristicas_humanas["Color_ojos"] = {"Azul" : "TTGTGGTGGC", "Verde" : "GGGAGGTGGC", "Marron": "AAGTAGTGAC"},
Caracteristicas_humanas["Genero"] = {"Mujer" : "TGAAGGACCTTC", "Hombre": "TGCAGGAACTTC"},
Caracteristicas_humanas["Raza"] = {"Blanco" : "AAAACCTCA", "Negro": "CGACTACAG", "Asiatico": "CGCGGGCCG"}

Sospechosos = {}

Sospechosos["Eva"] = {"Genero" : "Mujer", "Raza": "Blanco", "Color_pelo": "Rubio", "Color_ojos": "Azul", "Forma_facial": "Ovalada"},
Sospechosos["Larisa"] = {"Genero" : "Mujer", "Raza": "Blanco", "Color_pelo": "Marron", "Color_ojos": "Marron", "Forma_facial": "Ovalada"},
Sospechosos["Matej"] = {"Genero" : "Hombre", "Raza": "Blanco", "Color_pelo" : "Negro", "Color_ojos": "Azul", "Forma_facial": "Ovalada"},
Sospechosos["Miha"] = {"Genero" : "Hombre", "Raza": "Blanco", "Color_pelo": "Marron", "Color_ojos": "Verde", "Forma_facial": "Cuadrada"},

def caract():
    for k,v in Caracteristicas_humanas.items():
        print "%s -> %s" %(k,v)
def sosp():
    for k,v in Sospechosos.items():
        print "%s -> %s" %(k,v)

print adn_autor
print caract()
print sosp()