num = int(input("Que numero quieres convertir a binario?"))
print("NOTA: el numero en binario esta al reves xD")
while num != 0:
	coci = int(num % 2)
	num = int(num / 2)
	print("{}".format(coci))