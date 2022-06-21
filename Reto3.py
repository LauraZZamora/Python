
'''
Todos los codigos repetidos sin ten ren cuenta si son o no consecutivos:

codigos=str(input("Digite los sellos de los productos sin comas(,) ni puntos: "))
lista=list(codigos.split(" "))
sin_repetirCodigo=[]



for i in lista:
    if i not in sin_repetirCodigo:
        sin_repetirCodigo.append(i)

print(' '.join(sin_repetirCodigo))


for c in range(0, len(sin_repetirCodigo)):
    print(f"{lista.count(sin_repetirCodigo[c])}", end=" ")
'''
codigos=input().split(" ")
codigoAnterior=codigos[0]
cantidadAnterior=0
resultadoCodigos=""
resultadoCantidades=""
contador=0

for codigo in codigos:
    if codigo==codigoAnterior:
        cantidadAnterior+=1
    else:
        resultadoCodigos +=codigoAnterior+" "
        resultadoCantidades +=str(cantidadAnterior)+" "
        codigoAnterior=codigo
        cantidadAnterior =1
    if contador==len(codigos)-1:
        resultadoCodigos += codigoAnterior + " "
        resultadoCantidades += str(cantidadAnterior)
    contador +=1
print(resultadoCodigos)
print(resultadoCantidades)