# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:10:27 2020

@author: ACER
"""
import numpy as np
import cv2
import math as mt
import matplotlib.pyplot as plt


def ideal(im,Dc):
    img1=cv2.imread(im,0)                  #Lee la imagen a tratar 
    fuv=np.fft.fft2(img1)                  #Hace la transformada de fourier
    fuv=np.fft.fftshift(fuv)               #Cambia los componentes del centro de frecuencia
    M=img1.shape[0]                        #obtenemos el numero de columnas
    N=img1.shape[1]                        #Obtenemos el numero de las filas
    Do=np.zeros(2)                         #creamos un arreglo de ceros
    Do[0]=round(0.5*M)                     #Creamos los cuadrantes
    Do[1]=round(0.5*N)                             #Elegimos el tamaño del radio
    Huv=np.array(img1)                     #creamos un arreglo del tamaño de la imagen 
    for k in range(M):
        for m in range(N):                 #Creamos el arreglo 
           Huv[k,m]=0
    for k in range(M):
        for m in range(N):                 #le otrogamos al arreglo los valor requeridos
           d=mt.sqrt(((m-Do[0])**2)+((k-Do[1])**2))
           if(d<=Dc):                       #poner uno a valores mayores del radio
               Huv[k,m]=1                 

    plt.imshow(np.uint8(img1),cmap='gray') #Mostramos el arreglo original en una grafica 
    plt.title("Original")                  #como se vería el filtro 
    plt.figure() 
    Guv= Huv*fuv                           #normalizamos para su espectro gaussiano
    Guv=np.fft.fftshift(Guv)               #Cambiamos los componentes de Frecuencia
    gxy=np.fft.ifft2(Guv)                  #Obtenemos la trandformada en 2D
    gxy=np.abs(gxy)
    gxy=np.uint8(gxy)
    plt.imshow(np.uint8(gxy),cmap='gray')  #Mostramos el arreglo original en una grafica 
    plt.title("Imagen truncada")           #como se vería el filtro 
    plt.figure() 


    cv2.waitKey(0)
    cv2.destroyAllWindows()
