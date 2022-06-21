from collections import defaultdict
from collections import Counter

def CandidatosP():
    P = str(input("Digitar las letras de los caditados de grupo 10-P(P) sin espacios,puntos(.) o comas (,): ")).upper()

    contadorp = defaultdict(int)
    for cp in P:
        contadorp[cp] += 1

    for cp in sorted(contadorp, key=contadorp.get, reverse=True):
        if contadorp[cp] > 1:
            print("No puedes ingresar dos letras iguales")
            P = str(input("Digitar las letras de los caditados de grupo 10-P(P) sin espacios,puntos(.) o comas (,): ")).upper()
        else:
            CandidatosN(P)

def CandidatosN(P):
    N = str(input("Digitar las letras de los caditados de grupo 10-N(N) sin espacios,puntos(.) o comas (,): ")).upper()
    contan = defaultdict(int)
    for cn in N:
        contan[cn] += 1
    for cn in sorted(contan, key=contan.get, reverse=True):
        if contan[cn] > 1:
            print("No puedes ingresar dos letras iguales")
            N = str(input("Digitar las letras de los caditados de grupo 10-N(N) sin espacios,puntos(.) o comas (,): ")).upper()
        else:
            V = str(input("Digite los votos: "))
            Caracteres_ComunesP(P,V)


def Caracteres_ComunesP(P,V):
    contador_1 = Counter(P)
    contador_2 = Counter(V)

    comunes= contador_1 & contador_2

    if len(comunes)==0:
        return None
    comunes = list(comunes.elements())
    comunes = sorted(comunes)
    return comunes

print(CandidatosP())