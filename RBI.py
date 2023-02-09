# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:59:03 2020

@author: ACER
"""


import numpy as np
import cv2
import math as ma
import matplotlib.pyplot as plt



def recha(im,Dch,Dcl):
    img1=cv2.imread(im,0)
    fuv=np.fft.fft2(img1)
    fuv=np.fft.fftshift(fuv)
    M=img1.shape[0]
    N=img1.shape[1]
    Do=np.zeros(2)
    Do[0]=round(0.5*M)
    Do[1]=round(0.5*N)
    H1=np.array(img1)
    H2=np.array(img1)
    Huv=np.array(img1)
    for k in range(M):
        for m in range(N):
            H1[k,m]=0
    for k in range(M):
        for m in range(N):
            d=ma.sqrt(((m-Do[0])**2)+((k-Do[1])**2))
            if(d<=Dch):
                H1[k,m]=1
    for k in range(M):
        for m in range(N):
            H2[k,m]=0
    for k in range(M):
        for m in range(N):
            d=ma.sqrt(((m-Do[0])**2)+((k-Do[1])**2))
            if(d<=Dcl):
                H2[k,m]=1
    plt.imshow(np.uint8(img1),cmap='gray') #Mostramos el arreglo original en una grafica 
    plt.title("Original")                  #como se vería el filtro 
    plt.figure() 
    Huv=H1-H2
    Huv=1-Huv
    Guv=Huv*fuv
    Guv=np.fft.fftshift(Guv)
    gxy=np.fft.ifft2(Guv)
    gxy=gxy.real
    Ip_min=(np.amin(np.amin(gxy)))
    Ip_max=(np.amax(np.amax(gxy)))
    gxy=255*(gxy-Ip_min)/(Ip_max-Ip_min)
    gxy=np.uint8(gxy)
    plt.imshow(np.uint8(gxy),cmap='gray')  #Mostramos el arreglo original en una grafica 
    plt.title("Imagen RBI")                #como se vería el filtro 
    plt.figure() 
 
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
    
    
    
    