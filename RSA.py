import random

p = random.randrange(1, 102, 2)
q = random.randrange(1, 102, 2)
n = p * q
fin = (p-1)*(q-1)
e = 1%fin
d = (e**(-1))%fin

m = input("ingresa un mensaje")
c = (m**e)%n

print("Este es el mensaje encriptado: ", c)
