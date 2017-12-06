
centinela = 1
fallo = 0
turno = 1


def instrucciones():
    print("Este es un clásico juego de ahorcado. Ingresa una palabra y los otros intentarán adivinarla.\nCreado por Omar Salazar Paz.\n") #noqa


def pista(palabra):
    espacios = palabra.count(' ')
    letras = len(palabra) - espacios
    print("La palabra tiene {} letras y {} espacios".format(letras, espacios))


def palabraoculta(palabra):
    secreto = len(palabra) * "-"
    print("{}".format(secreto))


def tiras(palabra):
    """
    Verifica que lo que escribiste esté en la palabra 
    y realiza una acción dependiento de lo que escribiste
    """
    if letra in palabra:
        global fallo

        if letra == palabra:
            global centinela
            if (turno % 2 == 0):
                centinela = 0
                print("¡Haz ganado Usuario 2, felicidades!")
            else:
                centinela = 0
                print("¡Haz ganado Usuario 1, felicidades!")

        elif letra == "":
            print("¡No ingreses espacios en blanco, solo letras!\nEsto cuenta como fallar.")
            fallo += 1

        else:
            print("Hay {} \"{}\" en la palabra".format(palabra.count(letra), letra))

    else:
        print("No hay \"{}\" en la palabra".format(letra))
        
        fallo = fallo + 1

        if fallo == 1:
            print("\"Ahorcado\"")
            print("    o")
        elif fallo == 2:
            print("\"Ahorcado\"")
            print("    o")
            print("    |  ")
        elif fallo == 3:
            print("\"Ahorcado\"")
            print("    o")
            print("   /|  ")
        elif fallo == 4:
            print("\"Ahorcado\"")
            print("    o")
            print("   /|\ ")
        elif fallo == 5:
            print("\"Ahorcado\"")
            print("    o")
            print("   /|\ ")
            print("   /    ")
        elif fallo == 6:
            centinela = 0
            print("\"Ahorcado\"")
            print("    o")
            print("   /|\ ")
            print("   / \  ")
            print("Haz perdido :C")


def acertaste(palabra):
    """
    Imprime las letras que acertaste
    """
    #Esta wea esta incompleta :C
    for x in range(len(palabra)):
        espacio = " "



palabra = input("Ingresa la palabra a adivinar uwu: ")

for x in range(1,10):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")

instrucciones()
pista(palabra)

while (centinela > 0):
    if (centinela == 0 or fallo == 6):
        print("Juego terminado")
        break
    else:    
        palabraoculta(palabra)
        if (turno % 2 == 0):
            letra = input("Usuario 2: ")
            tiras(palabra) 
            turno += 1
        else:
            letra = input("Usuario 1: ")
            tiras(palabra)
            turno += 1
