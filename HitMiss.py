import cv2
import math as m
from matplotlib import pyplot as plt
import numpy as np
#Dilatación con umbral binario
#UMBRAL BINARIO
I1=cv2.imread('C:/Users/Acer/Pictures/Pruebas/negat.png',0)
Ib=np.array(I1)
#T=int(input("Ingrese el valor del umbral T:\n"))
T=150 #valor del umbral
M=I1.shape[0]
N=I1.shape[1]
for i in range(M):
    for j in range(N):
        if(I1[i,j]<=T):
            Ib[i,j]=0
        if(I1[i,j]>T):
            Ib[i,j]=255
cv2.imshow('Original',I1)
cv2.imshow('umbral binario',Ib)
I=np.ones((M+2,N+2))
Mb=I.shape[0]
Nb=I.shape[1]
for i in range(1,Mb-1):
    for j in range(1,Nb-1):
        I[i,j]=Ib[i-1,j-1]
Ic=np.array(I1)
for i in range(M):
    for j in range(N):
        if(Ib[i,j]==255):
            Ic[i,j]=0
        if(Ib[i,j]==0):
            Ic[i,j]=255
cv2.imshow('umbral binario reves',Ic)
II=np.ones((M+2,N+2))
Mc=II.shape[0]
Nc=II.shape[1]
for i in range(1,Mc-1):
    for j in range(1,Nc-1):
        II[i,j]=Ic[i-1,j-1]
hh=np.array([[1,1,0],[1,0,0],[0,0,0]])
hms=np.array([[0,0,0],[0,0,1],[0,1,1]])
sumahh=0
sumahms=0
for i in range(3):
    for j in range(3):
        if(hh[i,j]==1):
            sumahh=sumahh+1
for i in range(3):
    for j in range(3):
        if(hms[i,j]==1):
            sumahms=sumahms+1
print(sumahh,sumahms)
Ib_out=np.array(I)
Ib_out=Ib_out*0
Ic_out=np.array(I)
Ic_out=Ic_out*0
ite=1
for t in range(ite):
    for i in range(1,M+1):
        for j in range(1,N+1):
            suma1=0
            for m in range(-1,2):
                for n in range(-1,2):
                    if(I[i+m,j+n]==255):
                        if(I[i+m,j+n]*hh[m+1,n+1]==255*hh[m+1,n+1]):
                            suma1=suma1+1
                    if(suma1>=sumahh):
                        Ib_out[i-1,j-1]=255
for t in range(ite):
    for i in range(1,M+1):
        for j in range(1,N+1):
            suma1=0
            for m in range(-1,2):
                for n in range(-1,2):
                    if(II[i+m,j+n]==255):
                        if(II[i+m,j+n]*hms[m+1,n+1]==255*hms[m+1,n+1]):
                            suma1=suma1+1
                    if(suma1>=sumahms):
                        Ic_out[i-1,j-1]=255
If=np.array(I)
If=If*0
for i in range(M):
    for j in range(N):
        if(Ib_out[i,j] and Ic_out[i,j] ==255):
            If[i,j]=255
cv2.imshow("Thinning", If)
cv2.imwrite("ThinHM.png", If)
gxy=np.uint8(If)
plt.imshow(np.uint8(If),cmap='gray')  #Mostramos el arreglo original en una grafica 
plt.title("Thin")   
plt.figure() 
cv2.waitKey(0)
cv2.destroyAllWindows()