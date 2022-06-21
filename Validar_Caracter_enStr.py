
''' Comprobar si un caracter dado existe
en una cadena de caracteres'''


lenguaje= "Python es tremendo"

print(lenguaje.count('y')>0)

print(any(c == 'y' for c in lenguaje))

##carcater tanto mayuscula como minuscula
print(any(c.lower() == 'y' for c in lenguaje))



''' Obtener los caracteres que se repiten en una cadena

from collections import defaultdict
texto="Python es un lenguaje de programacion"
contador = defaultdict(int)
for c in texto:
    contador[c] +=1

for c in sorted(contador, key=contador.get, reverse=True):
    if contador[c]>1:
        print('El caracter %s se repite %i' % (c,contador[c]))


'''

