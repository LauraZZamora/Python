'''
Cuando se requieren caracteres especiales, de control o de Unicode, se
puede utilizar la secuencia de escape apropiada.
\n : Una nueva lınea
\t : Una tabulacion
\" : Una comilla doble
\’ : Una comilla simple
\\ : El caracter de diagonal invertida (backslash)
\u0105 : El caracter
\u01F4 : El caracter G

'''

str1='Ejemplo de cadena'
print(str1)

cadena="Cadena con un tabulado \t, y una nueva \n linea"
## el \t genera un espacio y \n salta de linea
print(cadena)

nombre="Minch yoda"
trabajo="Star Mar"
print(nombre+ " el maestro")
print(nombre+' '+trabajo)

Pnombre=str(input("Digite su primer nombre: "))
Papellido=str(input("Digite su primer apellido: "))
print(f"{Pnombre} {Papellido}")


'''
   En el orden
   lexicogr´afico, se comparan de izquierda a derecha uno a uno los caracteres,
   mientras sean iguales. En el caso que no sean iguales, si el car´acter de la
   primera cadena es menor que el de la segunda a la primer cadena se le
   considera menor, pero si es mayor, a la primer cadena se le considera
   mayor. Si todos los caracteres son iguales, las cadenas son iguales.
 '''

print('Rojas'<'Rosas') ## En el codigo ASCCI la j=106 esta antes de la s=115
print('Rotas'<'Rosas') ## t=116 s=115 , me dara True

a='Rojas'
b="Rojas"
c="Ro"+"jas"
d="Ro"
e="jas"
f=d+e
print(a==b)
print(a is b)
print(a==c)
print(a is c)
print(a==f)
print(a is f)
print(a==("Ro"+"jas"))

