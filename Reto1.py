Num1 = int(input("Digite el primer numero del billete: "))
Num2 = Num1*2+4
Num3 = int ((Num1+Num2)/5)
print(Num1,Num2,Num3)
if Num3>=0 and Num3 <=20:
    print("uno")
elif Num3 >= 21 and Num3 <=30:
    print("dos")
elif Num3 >= 31 and Num3 <=50:
    print("tres")
else:
    print("cuatro")