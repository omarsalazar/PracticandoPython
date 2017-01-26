a = ''
nombres = {
    'nombre': [],
    'apellido':[]
}
while a != '1':
    a = input("Ingresa un nombre. ")
    if a == '1': break
    nombres['nombre'].append( a )
    a = input("Ingresa un apellido. ")
    nombres['apellido'].append( a )

for x, (y, z) in enumerate(zip(nombres['nombre'], nombres['apellido'])):
    print (x, y, z)
