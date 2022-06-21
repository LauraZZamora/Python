import numpy as np
##Arreglo de una sola dimension
a=np.array(list(range(1,5)))
print(type(a))
print(a)
print(a.shape)
print(a[0],a[1],a[2])
a[0]=-4
print(a)


b=np.array([[1,2,3,5,6],[4,5,6,7,8]])
print(b.shape)
print(b)
b[0,0]=1590
print(b)
print(b[0,1])
print(b[1,0])

a=np.zeros((2,3,4))

b =np.ones((2,3)) ## Dos filas,tres columnas
print(b)
print(b.shape)


a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
## de la fila 0 y 1 las columnas 1 y 2
print(a)
b=a[0:2,1:3]
print(b)


b[0,0]=-11
print(b)
print(a)
print(a[0,1])

x=np.array([5,-4],dtype=np.int32)
print(x.dtype)
x=np.array([1.0,2.0])
print(x.dtype)


x=np.array([[1,2,5],[3,4,6]],dtype=np.float128)
x=np.array([[5,6,-1],[7,4,6]],dtype=np.float128)
print(x+y)
print(np.add(x,y))
