nume = 1
num = int(input("Escribe un numero"))
for i in range(num):
	print(num)

piramide = int(input("Escribe el numero de filas que quieres de la piramide"))
for i in range(piramide):
	print("*" * nume)
	nume += 1

palabra = input("ESscribe una palabra y la escribire letra por letra")
for letra in palabra:
	print( "\""+letra+"\"")

x = int(input("Escribe el numero que iniciará el conteo"))
y = int(input("Escribe el numero que finalizará el conteo"))
for i in range(x,y + 1):
	print(i)

facnum = int(input("Escribe el numero del que quieres un factorial"))
facto = 1
for i in range(1, facnum):
	facto += facto
	print(i)
