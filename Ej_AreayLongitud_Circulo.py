
''' Hacer un programa para ingresar el radio
de un circulo y se reporte su area y la
longitud de la circunferencia:
    entrada: r
    salida :
     area = pi * r^2
     longitud = 2 * pi * r
'''
import math ##importando modulo math para poder acceder al valor de pi
radio=float(input("Ingrese el radio: "))
area= math.pi * radio**2
longitud = 2*math.pi * radio

## area:.2f es para que solo me imprima dos numeros despues del punto del decimal
print(f"El area es: {area:.2f} y la longitud es {longitud:.3f}")

