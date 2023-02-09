import cv2
import math as m
from matplotlib import pyplot as plt
import numpy as np
X=cv2.imread("C:/Users/ACER/Pictures/Pruebas/negat.png", 0) 
M=X.shape[0]
N=X.shape[1]

MN=max(M,N)
print(M,N,MN)
T=150
Xb=np.array(X)
for i in range(M):
    for j in range(N):
        if(X[i,j]<=T):
            Xb[i,j]=0
        if(X[i,j]>T):
            Xb[i,j]=255
Xn=np.array(X)
for i in range(M):
    for j in range(N):
        if(Xb[i,j]==255):
            Xn[i,j]=0
        if(Xb[i,j]==0):
            Xn[i,j]=255
cv2.imshow("Original", X)
cv2.imshow("Binaria", Xb)
cv2.imshow("Binaria reves", Xn)
skel=np.array(X)
skel=skel*0
D=np.zeros((M,N))
for i in range(M):
    for j in range(N):
        if(Xn[i,j]==255):
            D[i,j]=0
        if(Xn[i,j]==0):
            su=0
            sd=0
            sr=0
            sl=0
            #sd
            for m in range(i,M-1):
                sd=sd+1
                if(m+1==M-1):
                    if(Xn[m+1,j]==255):
                        break;
                    if(Xn[m+1,j]==0):
                        sd=MN
                        break;
                if(Xn[m+1,j]==255):
                    break;
            #su
            for m in range(i):
                n=i-m
                su=su+1
                if(n-1==0):
                    if(Xn[n-1,j]==255):
                        break;
                    if(Xn[n-1,j]==0):
                        su=MN
                        break;
                if(Xn[n-1,j]==255):
                    break;
            #sr
            for x in range(j,N-1):
                sr=sr+1
                if(x+1==N-1):
                    if(Xn[i,x+1]==255):
                        break;
                    if(Xn[i,x+1]==0):
                        sr=MN
                        break;
                if(Xn[i,x+1]==255):
                    break;
            #sl
            for x in range(j):
                y=j-x
                sl=sl+1
                if(y-1==0):
                    if(Xn[i,y-1]==255):
                        break;
                    if(Xn[i,y-1]==0):
                        sl=MN
                        break;
                if(Xn[i,y-1]==255):
                    break;
            if(su==0):
                su=MN
            if(sd==0):
                sd=MN
            if(sr==0):
                sr=MN
            if(sl==0):
                sl=MN
            
        
            c1=min(su,sd,sr,sl)
            #print("i:",i,"j:",j)
            #print("su:", su,"sd:", sd, "sr:", sr, "sl:", sl,"c1:",c1)
            D[i,j]=c1
        
D=D*5
for i in range(M):
    for j in range(N):
        mau=0
        mad=0
        mar=0
        mal=0
        if(i!=0):
            mau=D[i-1,j]
        if(i!=(M-1)):
            mad=D[i+1,j]
        if(j!=(N-1)):
            mar=D[i,j+1]
        if(j!=0):
            mal=D[i,j-1] 
        c2=max(mau,mad,mar,mal)
        if(D[i,j]>=c2):
            skel[i,j]=255
cv2.imshow("Skeleton", skel)
cv2.imwrite("Silueta hueca.png", skel)
cv2.waitKey(0)
cv2.destroyAllWindows()
        
