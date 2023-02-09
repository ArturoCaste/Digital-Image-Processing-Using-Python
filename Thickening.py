import cv2
import math as m
from matplotlib import pyplot as plt
import numpy as np
X=cv2.imread("C:/Users/ACER/Pictures/Pruebas/negat.png", 0)
M=X.shape[0]
N=X.shape[1]
print(M,N)
T=150
for i in range(M):
    for j in range(N):
        if(X[i,j]<=T):
            X[i,j]=0
        if(X[i,j]>T):
            X[i,j]=255
Xn=np.array(X)
for i in range(M):
    for j in range(N):
        if(X[i,j]==255):
            Xn[i,j]=0
        if(X[i,j]==0):
            Xn[i,j]=255
Xb=np.zeros((M+2,N+2))
Mb=Xb.shape[0]
Nb=Xb.shape[1]
for i in range(1,Mb-1):
    for j in range(1,Nb-1):
        Xb[i,j]=(1/255)*Xn[i-1,j-1]
h=np.zeros((3,3))
y=np.array(X)
b1=0
b2=0
b3=0
b4=0
s1=0
s2=0
c1=0
c2=0
c3=0
for i in range(1,M+1):
    for j in range(1,N+1):
        for m in range(-1,2):
            for n in range(-1,2):
                b1=0
                b2=0
                b3=0
                b4=0
                s1=0
                s2=0
                h[1+m,1+n]=Xb[i+m,n+j]
                y[i-1,j-1]=h[1,1]
                if(h[1,2]==0 and (h[0,2]==1 or h[0,1]==1)):
                    b1=1
                if(h[0,1]==0 and (h[0,0]==1 or h[1,0]==1)):
                    b2=1
                if(h[1,0]==0 and (h[2,0]==1 or h[2,1]==1)):
                    b3=1
                if(h[2,1]==0 and (h[2,2]==1 or h[1,2]==1)):
                    b4=1
                c1=b1+b2+b3+b4
                if(h[1,2]==1 or h[0,2]==1):
                    s1=s1+1
                if(h[0,1]==1 or h[0,0]==1):
                    s1=s1+1
                if(h[1,0]==1 or h[2,0]==1):
                    s1=s1+1
                if(h[2,1]==1 or h[2,2]==1):
                    s1=s1+1
                if(h[0,2]==1 or h[0,1]==1):
                    s2=s2+1
                if(h[0,0]==1 or h[1,0]==1):
                    s2=s2+1
                if(h[2,0]==1 or h[2,1]==1):
                    s2=s2+1
                if(h[2,2]==1 or h[1,2]==1):
                    s2=s2+1
                c2=min(s1,s2)
                if(h[1,2]==0):
                    c3=0
                    if(c3==0 and c2>=2 and c2<=3 and c1==1):
                        y[i-1,j-1]=0        
                if(h[1,2]==1):
                    if(h[0,2]==1 or h[0,1]==1 or (1-h[2,2])==1):
                        if(h[1,0]==0):
                            c3=0
                            if(c3==0 and c2>=2 and c2<=3 and c1==1):
                                y[i-1,j-1]=0
                        if(h[1,0]==1):
                            if(h[2,0]==0 and h[2,1]==0 and (1-h[0,0])==0):
                                c3=0
                                if(c3==0 and c2>=2 and c2<=3 and c1==1):
                                    y[i-1,j-1]=0
                    if(h[0,2]==0 and h[0,1]==0 and (1-h[2,2])==0):
                        c3=0
                        if(c3==0 and c2>=2 and c2<=3 and c1==1):
                            y[i-1,j-1]=0
y=255*y
yn=np.array(y)
cv2.imshow("Thicke", y)
cv2.imwrite("Thicke_T_150.png", y)
M=y.shape[0]
N=y.shape[1]
print(M,N)
for i in range(M):
    for j in range(N):
        if(y[i,j]==255):
            yn[i,j]=0
        if(y[i,j]==0):
            yn[i,j]=255

cv2.imshow("Thickening", yn)
cv2.imwrite("Thickening_T_150.png", yn)
        
cv2.waitKey(0)
cv2.destroyAllWindows()
