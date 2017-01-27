import random
p = random.randrange(1, 102, 2)
q = random.randrange(1, 102, 2)
n = p * q
print(n)

if p%2==0 and q%2==0:
    print("los numeros son pares")
else:
    print("Son primos")

if n%2==0:
    print("n es par")
else:
    print("n es primo")
