print "Bienvenido a Pig traductor"

pyg = 'ei'

original = raw_input('Escribe una palabra: ') #pedirle al usuario que inserte una palabra

if len(original) > 0 and original.isalpha():
    palabra = original.lower() #nueva variable para poner en minusculas lo que sea que escriba el usuario
    prim = palabra[0] #Variable que almacena la primera letra de la palabra que puso el usuario
    if prim == "a" or prim == "e" or prim == "i" or prim == "o" or prim == "u": #decirle al programa que vaya y revise si la primera palabra es una vocal
        nueva_palabra = palabra + pyg #variable que hace la traduccion
        print nueva_palabra
    else:
        nueva_palabra = palabra[1:] + prim + pyg #'palabra[1:]' significa: de la segunda letra en adelante + primera letra + 'ei'
        print nueva_palabra
else:
	print "Escriba una palabra valida"

pyg = 'ay'
nueva_palabra = palabra + primera + pyg
nueva_palabra = "[1:len(nueva_palabra)]"
original = raw_input('Escribi una palabra:')

if len(original) > 0 and original.isalpha():
    palabra = original.lower()
    primera = palabra[0]
    print nueva_palabra
else:
    print 'vacio'