
def verificar_posicion(listaNumero_Vitrina,lista_Productos,producto):
  posicionfinal=[]

  for f in listaNumero_Vitrina:
    if lista_Productos[f]==producto:
      posicionfinal.append(f)
  return posicionfinal
verificar_posicion([1, 3, 6, 8],['reloj','cadena','anillo','anillo','anillo','reloj','cadena','anillo','anillo','anillo'],'cadena')




def entrada_sin_exhibicion(listaLlegada,listaExhibicion):
    sinexhibicion = []
    for l in listaLlegada:
            if l not in listaExhibicion:
                sinexhibicion.append(l)
    return sinexhibicion
entrada_sin_exhibicion([3,5,7,10,15,16],[4,10,5,8])


def cantidad_exhibicion_sin_entrada(listallegaron,lista_Enexhibicion):
  contador_llegaron = 0
  contador_exhibicion = 0
  for v in listallegaron:
    if v not in lista_Enexhibicion:
      contador_llegaron += 1
  for b in lista_Enexhibicion:
    if b not in listallegaron:
      contador_exhibicion += 1
  if contador_llegaron < contador_exhibicion:
    return contador_llegaron
  else:
    return contador_exhibicion
cantidad_exhibicion_sin_entrada([3,5,7,10,15,16],[4,10,5,8])

def tipo_de_joyas(nombre):
  resultadoproductos=[]
  for producto_o in nombre:
    if producto_o not in resultadoproductos:
      resultadoproductos.append(producto_o)
  return resultadoproductos
tipo_de_joyas(['reloj','cadena','anillo','anillo','anillo','reloj','cadena','anillo','anillo','anillo'])