from collections import defaultdict

Can=0
P = str(input("Digitar las letras de los caditados de grupo 10-P(P) sin espacios,puntos(.) o comas (,): ")).upper()

contadorp = defaultdict(int)
for cp in P:
    contadorp[cp] +=1

for cp in sorted(contadorp, key=contadorp.get, reverse=True):
    if contadorp[cp]>1:
        print("No puedes ingresar dos letras iguales")
        P = str(input("Digitar las letras de los caditados de grupo 10-P(P) sin espacios,puntos(.) ni comas (,): ")).upper()

N = str(input("Digitar las letras de los caditados de grupo 10-N(N) sin espacios,puntos(.) o comas (,): ")).upper()

contan = defaultdict(int)
for cn in N:
    contan[cn] +=1
for cn in sorted(contan, key=contan.get, reverse=True):
    if contan[cn]>1:
        print("No puedes ingresar dos letras iguales")
        N = str(input("Digitar las letras de los caditados de grupo 10-N(N) sin espacios,puntos(.) o comas (,): ")).upper()

V=str(input("Digite los votos: "))


for i in range(0,len(V)):
    if V[i] in P and V[i] in N:
        Can +=0
    elif V[i] in P:
        Can +=1
    elif V[i] in N:
        Can -=1
    else:
        Can +=0

    if Can>0:
        print("P", end="")
    elif Can<0:
        print("N", end="")
    else:
        print("I",end="")