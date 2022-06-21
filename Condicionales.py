
### Valor absoluto de numero
x = float(input("Ingrese un numero real x: "))
def valor_absoluto(x):
    if x >= 0:
        valor = x
    else:
        valor = -x
    return valor

valor_abs = valor_absoluto(x)
print("El valor absoluto de " + str(x), end = " ")
print("es " + str(valor_abs))

#### El mayor de dos numeros

n1=int(input("Digite el primer numero: "))
n2=int(input("Digite el segundo numero: "))
if n1>n2:
    print(f"El numero mayor es {n1}")
elif n1==n2:
    print(f"El numero {n1} es igual a {n2}")
else:
    print(f"El numero mayor es {n2}")

### Operador condicional ternario

y=float(input("Digite el numero: "))
def valor_absoluto(y):
    valor = y if y >= 0 else -y
    ##me va a retornar el valor de y si se cumple la condicion
    return valor
print("El valor absoluto de " + str(y), end = " ")
print("es " + str(valor_absoluto(y)))


### Impresion de numeros con signo / utiliza solo un condiciona


def imprimir_signo(f):
    if f>=0:
        print("+",end="")
    print(f)
    return f
f=float(input("Digite el numero para agregar signo: "))
print(imprimir_signo(f))


## Condicional con true y false

def condicional(p,q):
    if p==True and q==False:
        return False
    else:
        return True

## Tambien se puede asi sin ele

def condicional2(p,q):
    if p: ##Si p es verdadera retornar q
        return q
    return True ## De lo contrario retornar True


##Condicionales anidados
''' Si un cliente lleva mas de 5 productos del mismo tipo le realizan
un descuento del 5%. Si lleva mas de 10 productos del mismo tipo
le realizan un descuento del 10%. Si lleva mas de 20 productos
del mismo tipo le realizan un descuento del 20%. Construya un
programa que dado el numero de productos y el precio de cada
producto determine el valor a pagar por el cliente.
 '''

def Precio_Producto(precio,cantidad):

  if cantidad<=5:
      valor = (precio * cantidad)
      print(f"No hay descuento, precio a pagar {valor}")
  elif 5<cantidad<=10:
      valor = (((precio * cantidad)*5)/100)
      print(f"El precio a pagar es de: {valor}")
  elif 10<cantidad<=20:
      valor = (((precio * cantidad)*10)/100)
      print(f"El precio a pagar es de: {valor}")
  else:
      valor = (((precio * cantidad)*20)/100)
      print(f"El precio a pagar es de: {valor}")

precio=float(input("Digite el precio del prodicto: "))
cantidad=float(input("Digite la cantidad de producto: "))
print(Precio_Producto(precio,cantidad))