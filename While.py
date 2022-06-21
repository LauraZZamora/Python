
''' Se va a repetir mientras se cumpla una condicion'''

'''
i = 0
while(i <= 6):
    print(i)
    i = i + 1

'''


i = 2                   # inicializa a i en 2
j = 25                  # inicializa a j en 25
while i < j:            # mientras i sea menor a j
    print(i, j, sep = ", ") # imprime los valores de i y j , y con sep los separa con coma ,
    i *= 2                  # i = i * 2; i se mult´ıplica por 2 en cada paso
    j += 10                 # j = j + 10; se incrementa de 10 en 10
print("the end.")       # se ejecuta al terminar el ciclo
print(i, j, sep = ", ") # valores finales de i y j, y con sep los separa con coma


''' La codificaci´on en Python de una funci´on constante
 para hallar el m´ınimo n´umero positivo representable 
 en la m´aquina y un programa principal es '''
def min_maquina():
    Xo = 1.0
    Xi = Xo / 2.0
    while Xi > 0.0:
        Xo = Xi
        Xi = Xo / 2.0
    return Xo
print("El mınimo numero positivo", end = " ")
print("en esta maquina es:", min_maquina())


'''Disene un algoritmo que involucre un ciclo y que nunca ingrese al
ciclo.'''
a=3
b=4
while a>b:
    print("Nunca va a entrar al bucle juemama")

'''Disene un algoritmo que involucre un ciclo y que se ejecute
indefinidamente'''
c=5
d=3
while c>d:
    print(f"{c},{d}")
    print("Bucle infinito juemama")
    c -=1
print("The end")
print(f"{c},{d}")


''' Disene un algoritmo que pida un valor entero, y que siga leyendo
valores enteros mientras que alguno de esos valores no represente el
c´odigo ASCII de una letra may´uscula en el abc del ingl´es.
'''
n=int(input("Digite el numero entero: "))
while  n>=65 and n<=90:
    n = int(input("Digite otro numero entero, este no sirve, representa letra mayuscula en ASCII: "))
print(f"El numero {n} no representa letras mayusculas en ASCII, BIEN")