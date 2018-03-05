from random import randint
opcion = int(raw_input('Tu opcion: '))
opciones_restantes = 3
while opciones_restantes > 0:
    numero_aleatorio = randint(1, 10)
    print numero_aleatorio
    opciones_restantes -= 1
    if opcion == numero_aleatorio:
        print 'Ganaste'
        break
else: #ponemos en else en esta sangria porque si le ponemos la misma sangria que if, despues de cada numero hara el print
    print 'Perdiste'