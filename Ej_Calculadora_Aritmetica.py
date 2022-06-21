''' Construir un programa que simule el funcionamiento
de una calculadora que puede realizar las cuatro
operaciones aritmeticas basicas (suma,resta,multiplicacion y division).
El usuario debe especificar la operacion con el primer
caracter del nombre de la operacion.

    -> S,s-Suma
    -> R,r-Resta
    -> P,p,M,m-Multiplicacion
    -> D,d-Division
'''

saldo = 1000
print("\t.:MENU:.")
print("1. Depositar")
print("2. Retirar")
print("3. Consultar saldo")
print("4. Salir")
opcion = int(input("Digitar opcion de menu: "))

print()

if opcion==1:
    depositar= float(input("Digite el valor a depositar: "))
    saldo +=depositar
    print(f"Dinero en la cuenta: {saldo}")
elif opcion==2:
    retirar = float(input("Digite el valor a retirar: "))
    if retirar>saldo:
        print("Saldo insuficiente")
    else:
        saldo -= retirar
    print(f"Dinero en la cuenta: {saldo}")
elif opcion==3:
    print(f"Dinero en la cuenta: {saldo}")
elif opcion==4:
    print("Gracias por utilizar nuetro servicio")
else:
    print("Error")
