''' Los bucles o ciclos while se va a repetir
 un numero indeterminado de veces y se
  necesita que se cumpla una condicion para que
  se ejecute n veces
'''

import math

numero=int(input("Digite un numero: "))

#Mientras se cumpla la condicion, el bucle se ejecutara n veces
while numero<0:
    print("Error -> Deberia ser un numero positivo")
    numero = int(input("Digite un numero: "))

print(f"\nSu raiz cuadrada es: {(math.sqrt(numero))}")

i=0
while i<10:
    print(f"{i}. Hola mundo")
    i +=1







