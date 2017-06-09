a = int(input("Escribe un numero: "))
b = int(input("Escribe otro numero: "))
c = a + b

if(c < 10):
    print("Come caca {} veces".format(c))
else:
    print("Eres bieeeeen vergas. Vales {} veces tu peso en oro ue".format(c))

nombre = input("Escribe tu nombre: ")
longitudString = print("El nombre que escribiste tiene {} letras (Incluyendo espacios si los pusiste.)".format(len(nombre)))# noqa
letra = int(input("Escribe el numero de la letra que quieres obtener: "))

if(letra <= 0):
    print("No mames ue, no puedes hacer eso")
else:
    print("Esta es la letra que elegiste ue: \"{}\"".format(nombre[letra - 1]))
