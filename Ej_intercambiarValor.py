''' Hacer un programa para intercambiar
el valor de 2 variables, por ejemplo:

a=10  ->  a=5
b=5   ->  b=10
'''

a = input("a -> ")
b = input("b -> ")
### intercambio
a,b = b,a

print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")
