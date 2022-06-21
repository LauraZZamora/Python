import json

menu=input()
lista=list(input().split(" "))
diccionario_menu=json.loads(menu)
resultado_suma=0
resultado_lista=""


for i in lista:
    for k,v in diccionario_menu.items():
      if i==k:
        resultado_suma += v
        resultado_lista +=str(i)+" "
print(resultado_suma)
print(resultado_lista)



