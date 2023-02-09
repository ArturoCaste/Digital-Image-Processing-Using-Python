import numpy as np
import cv2
import math as mt
import matplotlib.pyplot as plt


def ideal(im):
    img1=cv2.imread(im,0)                  #Lee la imagen a tratar 
    fuv=np.fft.fft2(img1)                  #Hace la transformada de fourier
    fuv=np.fft.fftshift(fuv)               #Cambia los componentes del centro de frecuencia
    M=img1.shape[0]                        #obtenemos el numero de columnas
    N=img1.shape[1]                        #Obtenemos el numero de las filas
    Do=np.zeros(2)                         #creamos un arreglo de ceros
    Do[0]=round(0.5*M)                     #Creamos los cuadrantes
    Do[1]=round(0.5*N)
    Dc=10                                  #Elegimos el tamaño del radio
    Huv=np.array(img1)                     #creamos un arreglo del tamaño de la imagen 
    for k in range(M):
        for m in range(N):                 #Creamos el arreglo 
           Huv[k,m]=0
    for k in range(M):
        for m in range(N):                 #le otrogamos al arreglo los valor requeridos
           d=mt.sqrt(((m-Do[0])**2)+((k-Do[1])**2))
           if(d>Dc):                       #poner uno a valores mayores del radio
               Huv[k,m]=1                 


    cv2.imshow("Pb", np.uint8(255*Huv))
    Guv=(1/255)*Huv*fuv
    Guv=np.fft.fftshift(Guv)
    Guv_abs=np.abs(Guv)
    Guv_abs=np.uint8(255*Guv_abs/np.max(Guv_abs))
    cv2.imshow("espectro G", Guv_abs)
    gxy=np.fft.ifft2(Guv)
    gxy=gxy.real
    Ip_min=(np.amin(np.amin(gxy)))
    Ip_max=(np.amax(np.amax(gxy)))
    gxy=255*(gxy-Ip_min)/(Ip_max-Ip_min)
    gxy=np.uint8(gxy)
    cv2.imwrite("FiltradaIdealPA.png", gxy)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
