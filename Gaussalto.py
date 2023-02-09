import numpy as np
import cv2
import math as mt
import matplotlib.pyplot as plt
from PIL import Image



def bajo(im): 
    img1=cv2.imread(im,0)                   #Lee la imagen a tratar 
    fuv=np.fft.fft2(img1)                   #Hace la transformada de fourier
    fuv=np.fft.fftshift(fuv)                #Cambia los componentes del centro de frecuencia
    M=img1.shape[0]                         #obtenemos el numero de columnas
    N=img1.shape[1]                         #Obtenemos el numero de las filas
    Do=np.zeros(2)                          #creamos un arreglo de ceros
    Do[0]=round(0.5*M)                      #Creamos los cuadrantes
    Do[1]=round(0.5*N)
    Dc=50                             #Elegimos el tamaño del radio
    Huv=np.array(img1)                      #creamos un arreglo del tamaño de la imagen 
    for k in range(M):     
        for m in range(N):                  #Creamos el arreglo 
            Huv[k,m]=0
    for k in range(M): 
        for m in range(N):                  #le otrogamos al arreglo los valor requeridos
            d=mt.sqrt(((m-Do[0])**2)+((k-Do[1])**2))
            Huv[k,m]=255*mt.exp(-(d**2)/(2*Dc**2))
            
            
    plt.imshow(np.uint8(img1),cmap='gray')  #Mostramos el arreglo original en una grafica 
    plt.title("Original")                   #como se vería el filtro 
    plt.figure() 
    cv2.imshow("Imagen Filtrada",img1)        #Mostramos la imagen generada
    Guv=(1/255)*Huv*fuv                     #normalizamos para su espectro gaussiano
    Guv_abs=np.abs(Guv)                     #Obtenemos la norma  
    Guv_abs=np.uint8(255*Guv_abs/np.max(Guv_abs))
    gxy=np.fft.ifft2(Guv)
    gxy=np.abs(gxy)
    gxy=np.uint8(gxy)
    plt.imshow(np.uint8(gxy),cmap='gray')   #Mostramos la imagen modificada  
    plt.title("Imagen filtrada")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
