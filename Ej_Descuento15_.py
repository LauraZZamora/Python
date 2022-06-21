
'''
Una tienda ofrece un descuento del 15% sobre el total de la compra
y un cliente desea saber cuando debera pagar finalmente por su compra
'''

precio = float(input("Digite el precio: "))
descuento = (precio*15)/(100)
precio_final = precio-descuento

print(f"El precio es de : {precio_final:.2f}")
