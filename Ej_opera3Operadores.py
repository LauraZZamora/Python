''' Determinar la solucion logica
de la siguiente operacion:

    ((3+5x8)<3 and ((-6/3 x 4)+2<2)) or (a>b)
'''

a = float(input("a-> "))
b = float(input("b-> "))

operacion = ((3+5*8)<3 and (((-6*4)/(3))+2<2)) or (a>b)
print(f"El resultado de la operacion es {operacion}")

