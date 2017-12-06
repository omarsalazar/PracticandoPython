a = ''
listakk = []
while a != '1':
    a = input("Ingresa algo a la lista. (\"1\" para detener el loop)")
    if a == '1':
        break
    listakk.append(a)

print("Esto es lo que hay en la lista: ", listakk)
