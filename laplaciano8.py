import cv2
import math as m
import numpy as np
from matplotlib import pyplot as plt
img1=cv2.imread("C:/Users/ACER/Pictures/Pruebas/negat.png",0)

cv2.imshow("Original",img1)
print(img1)
tf=3
M=img1.shape[0]
N=img1.shape[1]
print("M:",M,"N:",N)
Is=np.zeros((M,N))
print(Is)
fil=np.ones((tf,tf))
masc=np.array(fil)
masc=0*masc
fil=np.array([[1,1,1],[1,-8,1],[1,1,1]])
print(fil)
x=fil.shape[0]
y=fil.shape[1]
print(x,y)
a=(-1*((tf-1)/2))
b=(tf+1)/2
print(a,b)
for i in range(1,M+1): 
    for j in range(1,N+1): 
        for m in range(-1,2): 
            for n in range(-1,2):
                index_i=i+m
                if (index_i<1):
                    index_i=abs(index_i)+i
                elif (index_i>M):
                    index_i=index_i-m
                index_j=j+n
                if (index_j<1):
                    index_j=abs(index_j)+j
                elif (index_j>N):
                    index_j=index_j-n
                masc[m+1,n+1]=img1[index_i-1,index_j-1]
                Is[i-1,j-1]=Is[i-1,j-1]+img1[index_i-1,index_j-1]*fil[m+1,n+1]

suma=0
print(i,i)
print(Is[i-1,j-1])
print(masc)
print(Is)
maximo=Is[0,0]
minimo=Is[0,0]
for i in range(M):
    for j in range(N):
        if(Is[i,j]>maximo):
            maximo=Is[i,j]
        if(Is[i,j]<minimo):
            minimo=Is[i,j]
print(maximo,minimo)
for i in range(M):
    for j in range(N):
        Is[i,j]=255*((Is[i,j]-minimo)/(maximo-minimo))
print(Is)
print("Imagen filtrada")
imgfil=np.array(img1)
for i in range(M):
    for j in range(N):
        imgfil[i,j]=Is[i,j]
cv2.imshow("Imagen con Laplaciano8",imgfil)
cv2.imwrite("Laplaciano8.png", imgfil)

plt.hist(img1.ravel(),256,[0,255])
plt.xlabel('Valores de escala de grises')
plt.ylabel('Numero de veces que se repiten')
plt.title('Histograma imagen original')
plt.show()

plt.hist(imgfil.ravel(),256,[0,255])
plt.xlabel('Valores de escala de grises')
plt.ylabel('Numero de veces que se repiten')
plt.title('Histograma imagen filtro Laplaciano8')
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
