
palabra = input("Ingresa la palabra a adivinar uwu: ")
fallo = 0
i = 0
turno = 1

def pista(palabra):
    """Te da una pista"""
    espacios = palabra.count(' ')
    letras = len(palabra) - espacios
    print("La palabra tiene {} letras y {} espacios".format(letras, espacios))

def tiras(palabra):
    """Verifica que lo que escribiste esté en la palabra"""
    if letra in palabra:
        if letra == palabra:
            if (turno % 2 == 0):
                print("¡Haz ganado Usuario 2, felicidades!")
                i = 1
            else:
                print("¡Haz ganado Usuario 1, felicidades!")
                i = 1

        else:
            print("Hay {} \"{}\" en la palabra".format(palabra.count(letra), letra))
            #Aquí va a estar la función "acertaste()"
    else:
        print("No hay \"{}\" en la palabra".format(letra))
        global fallo
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
            print("\"Ahorcado\"")
            print("    o")
            print("   /|\ ")
            print("   / \  ")
            print("Haz perdido :C")
            i = 1
        

def acertaste(palabra):
    """Imprime las letras que acertaste"""
    #Esta wea esta incompleta :C
    for x in range(len(palabra)):
        espacio = " "

while (i != 1):
    """
    Habrá dos usuarios y dependiendo de el valor 
    del modulo de turno tirará el usuario 1 o 2.
    """
    if (turno % 2 == 0):
        letra = input("Usuario 2: ")
        tiras(palabra)
        turno += 1
    else:
        letra = input("Usuario 1: ")
        tiras(palabra)
        turno += 1

pista(palabra)


