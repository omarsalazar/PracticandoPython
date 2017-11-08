# creo que este codigo está kk, estoy seguro que se puede hacer de una manera más "elegante".
a = 0
b = 1
# fibo pa' los cuates uwu.
num = int(input("cuantos numeros quieres de fibo? uwu"))
if num < 2:
	print(a)
else:
	print("{}\n{}".format(a, b))
	for x in range(0, num - 2):
		c = a + b
		a = b
		b = c
		print("{} ".format(c))