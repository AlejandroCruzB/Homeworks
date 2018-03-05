import random

tablero = []

for x in range(0,5):
  tablero.append(["O"] * 5)

def print_tablero(tablero):
  for fila in tablero:
    print " ".join(fila)

print "Juguemos a la batalla naval!"
print_tablero(tablero)

def fila_aleatoria(tablero):
  return random.randint(0,len(tablero)-1)

def columna_aleatoria(tablero):
	return random.randint(0,len(tablero[0])-1)

barco_fila = fila_aleatoria(tablero)
barco_columna = columna_aleatoria(tablero)

for turno in range(4):
    print "Ronda", turno + 1
    adivina_fila = int(raw_input("Adivina fila:"))
    adivina_columna = int(raw_input("Adivina columna:"))

    print barco_fila
    print barco_columna


    if adivina_fila == barco_fila and adivina_columna == barco_columna:
        print "Felicitaciones, Hundiste mi barco!"
        break
    else:

        if adivina_fila not in range(5) or adivina_columna not in range(5):
            print "Huy, eso ni siquiera esta en el oceano"
        elif tablero[adivina_fila][adivina_columna] == "X":
            print "Ya dijiste esa."
        else:
            print "Agua, no tocaste mi barco"
            tablero[adivina_fila][adivina_columna] = "X"
            print_tablero(tablero)
        if turno == 3:
            print "Fin del juego"
            break
