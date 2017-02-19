palabra = input("Ingresa la palabra a adivinar uwu: ")

"""Te da una pista"""
def pista(palabra):
    espacios = palabra.count(' ')
    letras = len(palabra) - espacios
    print("La palabra tiene {} letras y {} espacios".format(letras, espacios))

pista(palabra)

""" Habrá dos usuarios y dependiendo de el valor 
 del modulo de turno tirará el usuario 1 o 2."""
i = 1
turno = 1
while (i == 1):
    if (turno % 2 == 0):
        letra = input("Usuario 2: ")
        eleccion(palabra, letra, opcion)
    else:
        letra = input("Usuario 1: ")
        eleccion(palabra, letra, opcion)
turno = turno + 1
