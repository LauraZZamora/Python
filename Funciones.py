
''' Primero se escribe la palabra reservada def y Posteriormente se escribe el nombre
de la funcion .'''




def funcion(x):
    ## Se le esta pasando una variable por parametro
    return x*x ## Retornar la multiplicacion
print(funcion(3)) ## y en print se le paso el valor de x


def informacion(nombre, puesto = 'Paramtro por defecto -> Desconocido'):
    print(f'Soy {nombre} y soy {puesto}')
    return nombre
informacion('Laura','Desarrolladora')
informacion('Tatiana','Ingeniera')
informacion('Juan')

empleado = informacion('Pablo')
print (empleado)


def datos(nombre):
    return nombre

empleado2 = datos('Lola')
print(empleado2)


nombre2 = 'Pedro'
def mostrar_nombre(nombre2):
    print(f'Hola {nombre2}')

mostrar_nombre(nombre2.upper())
print( nombre2.upper() ) ### Mayusculas
print( nombre2.title() ) ### Primera mayuscula



##  RADIO CIRCULO ##################


def Area_Circulo(radio):
    pi= 3.1416
    area= pi*radio**2
    return area
print(Area_Circulo(3))

'''Si queremos importar el valor de pi, debemos de agregar
import math'''

import math
def Area_Circulo2(radio2):
    area2= math.pi*radio2**2
    return area2
print(Area_Circulo2(3))

''' Tambien se puede importar pi de la siguiente manera'''

from math import pi

def Area_Circulo3(radio3):
    area3= pi*radio3**2
    return area3
print(Area_Circulo3(3))


##### FUNCIONES CON MAS DE UN PARAMETRO DE ENTRADA

''' Area rectangulo 
Para el c´alculo del ´area de un rect´angulo es necesario conocer el largo y el
ancho del rect´angulo, a partir de los cuales el ´area del rect´angulo est´a
dada por la expresi´on Ar = l ∗ a'''

largo= float(input("Largo del rectangulo: "))
ancho= float(input("Ancho del rectangulo: "))

def Area_Rectangulo(l,a):
    area=l*a
    return area
print("El area del rectangulo es:", end =" ") ## Para que el resultado me quede al lado y no de para abajo
print(Area_Rectangulo(largo,ancho))


