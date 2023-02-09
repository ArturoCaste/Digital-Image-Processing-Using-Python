import cv2
import math as m
from matplotlib import pyplot as plt
import numpy as np
#Dilatación con umbral binario
#UMBRAL BINARIO
X=cv2.imread("C:/Users/Acer/Pictures/Pruebas/negat.png", 0)
M=X.shape[0]
N=X.shape[1]
Xb=np.array(X)
T=150
for i in range(M):
    for j in range(N):
        if(X[i,j]<=T):
            Xb[i,j]=0
        if(X[i,j]>T):
            Xb[i,j]=1
print(M,N)
cv2.imshow("Binaria", 255*Xb)
Y=np.array(Xb)

I=np.zeros((M+2,N+2))
Mb=I.shape[0]
Nb=I.shape[1]
print(Mb,Nb)
for i in range(1,Mb-1):
    for j in range(1,Nb-1):
        I[i,j]=Xb[i-1,j-1]
for i in range(1,M+1):
    for j in range(1,N+1):
        suma=0
        if(I[i,j]==0):
             for m in range(-1,2):
                 for n in range(-1,2):
                     if(I[i+m,j+n]==1):
                         suma=suma+1
                         if(suma==8):
                             Y[i-1,j-1]=1
Y=255*Y
cv2.imshow("Fill", Y)
cv2.imwrite("Fill.png", Y);
cv2.waitKey(0)
cv2.destroyAllWindows()
