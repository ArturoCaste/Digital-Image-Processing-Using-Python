import cv2
import math as m
from matplotlib import pyplot as plt
import numpy as np
X=cv2.imread('C:/Users/Acer/Pictures/Pruebas/negat.png',0)
T=150
M=X.shape[0]
N=X.shape[1]
print(M,N)
Ib=np.array(X)
for i in range(M):
    for j in range(N):
        if(X[i,j]<=T):
            Ib[i,j]=0
        if(X[i,j]>T):
            Ib[i,j]=1
Xn=1-Ib
#print(Xn)
cv2.imshow("Binaria", 255*Ib)
cv2.imshow("Binaria reves", 255*Xn)
MUL=M*N
x1=np.array(X)
x1=x1*0
x1[200,600]=1
D=np.zeros((M+2,N+2))
Mb=D.shape[0]
Nb=D.shape[1]
H=np.array([[0,1,0],[1,1,1],[0,1,0]])
#print(H)
Ib_out=np.array(x1)
suma=0
x=x1
y=x
t=0
while(suma!=MUL):
    t=t+1
    for i in range(1,Mb-1):
        for j in range(1,Nb-1):
            D[i,j]=x1[i-1,j-1]
    Ib_out=x1
    for i in range(1,M+1):
        for j in range(1,N+1):
            for m in range(-1,2):
                for n in range(-1,2):
                    mul=D[i+m,j+n]*H[m+1,n+1]
                    if(mul==1):
                        Ib_out[i-1,j-1]=1
                        x1=Ib_out*Ib
    suma=0
    for i in range(M):
        for j in range(N):
            y[i,j]=D[i+1,j+1]
    for i in range(M):
        for j in range(N):
            if(y[i,j]==x1[i,j]):
                suma=suma+1
          
print("last")                                                       
print(x1)
print(suma)
print("X1")
print(X)
Y=np.array(X)
for i in range(M):
    for j in range(N):
        if(X[i,j]==1 or x1[i,j]==1):
            Y[i,j]=1
Y=Y*255
print("X2")
print(X)

cv2.imshow("Fill", Y)
cv2.imwrite("Extracción", Y)
cv2.waitKey(0)
cv2.destroyAllWindows()
