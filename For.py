'''
Esta estructura de control tiene dos propositos
primordiales que no siempre son soportados portodo lenguaje de
programacion:

1 Como una forma compacta de escribir un ciclo mientras (while).
2 Para iterar sobre los elementos de una coleccion de elementos.

'''


''' permiten calcular la suma de los primeros n n´umeros naturales positivos, 
es decir, permiten calcular el valor de la expresi´on'''

'''
## CON WHILE
int suma(int n){
    int s = 0;
    int i = 1;
    while(i <= n){
        s = s + i;
        i++;
    }
    return s;
}

def suma(n):
    s = 0
    i = 1
    while(i <= n):
        s += i
        i += 1
    return s



## CON FOR
int suma(int n){
    int s = 0;
    for(int i = 1; i <= n; i++){
        s = s + i;
    }
    return s;
}

def suma(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


'''


## Iteracion de colecciones

'''
<bloque_prev>
for <elemento> in <coleccion>:
    <bloque>
<bloque_sigui>

'''

frutas =["Tomane de arbol","Maracuya","Guayaba"]
for f in frutas:  ## Para cada elemento f en la lista de frutas
    ## f va a recorrer cada elemento de la lista, tomara cada elemento para poderlo imprimir
    print(f)


''' imprimir elementos hasta encontrar el nombre "Carolina"'''
nombres=["Laura","Carolina","Zamora"]
for f2 in nombres:
    print(f2)
    if f2=="Carolina":
        break  ## Me va a imprimir hasta Carolina, incluyendo este
    ## si quiero que me imprima hasta Carolina pero sin incluir este, ponemos el print abajo
    ## print(f2)



## La coleccion Rango (range)

'''
El comando range(6) genera la secuencia [0, 1, 2, 3, 4, 5].

El comando range(10, 21) genera la secuencia ##(posicion de inicio, posicion final -1)
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].

El comando range(-7, 8) genera la secuencia   ##(posicion de inicio, posicion final -1)
[-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7].

El comando range(2,11,2) genera la secuencia ##(posicion de inicio, posicion final -1,incrementar de 2 en 2)
[2, 4, 6, 8, 10].

El comando range(11,20,2) genera la secuencia ##(posicion de inicio, posicion final -1,incrementar de 2 en 2)
[11, 13, 15, 17, 19].

El comando range(5,-1,-1) genera la secuencia ##(posicion de inicio, posicion final -1,disminuyendo de a 1 unidad)
[5, 4, 3, 2, 1, 0].

El comando range(-2) genera la secuencia [ ].

'''

for i in range(-5,6,1): ##(posicion de inicio, posicion final -1, aumnetando 1 unidad)
    print(i)

print()

for v in range(10,0,-1):
    print(v)

print()

for r in range (11):
    print(r)

n=int(input("Digite el primer numero: "))
def suma2(n):
    s = 0
    for t in range(1, n + 1):
        s += t
    return s
print(suma2(n))


def suma(l):
    k = 0
    for m in range(1, l + 1):
        k += m
    return k
def main():
    l = int(input("n? = "))
    print("La suma de los primeros n n´umeros es:", end=" ")
    print(suma(l))
main()

