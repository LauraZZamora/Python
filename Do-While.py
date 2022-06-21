
''' Hacer mientras.
Se ejecutara una vez, se actualiza y se se evalua la condicion para ver si
esa actualizacion entrea al while o no, con el do se asegura la primera ejecucion'''

def min_maquina():
    Xi = 1.0 # Valor inicial
    Xo = Xi
    Xi = Xo / 2.0
    while(Xi > 0.0):
        Xo = Xi
        Xi = Xo / 2.0
    return Xo
print("El m´ınimo n´umero positivo", end = " ")
print("en esta m´aquina es:", min_maquina())


## Uso de variable bandera
'''
<bloque_prev>
<inicia>
bandera = True
while(bandera or <cond>): ## mientras la bandera sea verdadera o se cumple la condicion
bandera = False
<bloque>
<actualiza>
<bloque_sigui>
'''

''' El algoritmo para el obtener el mınimo numero positivo de la maquina
usando la aproximacion de un ciclo hacer-mientras (do) con una bandera
como se muestra a continuacion.'''

def min_maquina2():
    Xi = 1.0 # Valor inicial
    bandera = True # Permite que se ejecute el ciclo al menos una vez
    while(bandera or Xi > 0.0):
        bandera = False # Indica que ya se entro al ciclo y que luego solo se debe evaluar la condicion
         ##Al convertir la bandera en falsa ahora solo depende del Xi para entrar o no al while
        Xo = Xi
        Xi = Xo / 2.0
    return Xo
print("El m´ınimo n´umero positivo", end = " ")
print("en esta m´aquina es:", min_maquina2())

bandera2=True
p=2
while bandera2 or p>0:
    print("Hello bitch")
    bandera2=False
    p -=1


## Forzando la terminacion de un ciclo con break

''' Desarrollar un programa que lea numeros enteros y los sume hasta que lea
un cero (0). Un algoritmo que soluciona este problema es el que se
muestra a continuacion'''

suma = 0
while True:
    dato = int(input("Ingrese un n´umero entero " +"a sumar o 0 para salir: "))
    if(dato == 0):
        break
    suma += dato
print("La suma es: " + str(suma))