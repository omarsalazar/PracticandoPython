#Ésta es la palabra que se va a adivinar
palabra = input("Ingresa la palabra a adivinar uwu")
#Mientras i sea igual a 1 los turnos van a continuar.
i= 1
turno = 1
while (i == 1):
 # Abrá dos usuarios y dependiendo de el valor-
 # -del modulo de turno tirará el usuario 1 o 2.
	if (turno % 2 == 0):
		letra = input("Usuario 2: ")
        eleccion(palabra, letra, opcion)
	else:
		letra = input("Usuario 1: ")
        eleccion(palabra, letra, opcion)

	turno = turno + 1

#Esta parte es en donde se elige que quiere poner, letra o numero.
#Lo que se escribe se compara con la palabra a adivinar-
#-y te dice si acertaste o fallaste
def eleccion(palabra, letra, opcion):
	opcion = input("Deseas ingresar una letra(L) o la palabra(P)")
	if (opcion == "P" || opcion == "p"):
		#Llamar a la funcion palabra
        palabra()
	elif(opcion == "L" || opcion == "l"):
		if (palabra == letra):
		#Llamar a la funcion letra
        letra()
	else:
		print("Ingresa una letra valida")

def palabra():
	if (palabra == letra):
        #i se iguala a 0 para terminar el juego.
		i = 0
		print("¡Has ganado la partida!")
	else:
		print("Fallaste.")

def letra():
	if (palabra == letra):
		print("¡Has acertado!")
	else:
		print("Fallaste.")
