# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 00:28:59 2020

@author: ACER
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

def plotear(im,nombre):
    (m,n) = im.shape                            #Filas y columnas
    for k in range(m):
        for l in range(n):
            if im[k,l] == 1:
                im[k][l] = 255
            else:
                im[k][l] = 0
    plt.imshow(im.astype(np.uint8),cmap='gray') 
    plt.title(nombre)
    plt.axis('off')
    plt.figure()
    #return im

def dilation(im,nombre="Dilatación"):
    (m,n) = im.shape                            #Filas y columnas
    h = np.array([[0,1,0],[1,0,1],[0,1,0]])     #Máscara
    imf = np.zeros((m,n))                       #Crea la nueva imagen
    t = 3                   
    ima = np.zeros((t,t))
    o = np.zeros((t,t))
    #Mapeo
    for i in range (1,m-1):
        for j in range (1,n-1):
            for p in range (-1*round((t-1)/2),round((t-1)/2)+1):
                for q in range (-1*round((t-1)/2),round((t-1)/2)+1):
                    ima[p+1][q+1] = im[i+p][j+q]
            o = np.logical_and(ima,h,casting='same_kind')
            imf[i][j] = o.any()
    fin = plotear(imf,nombre)
    #a=np.asarray(fin,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("dilatación.png")
    return imf

def erosion(im,nombre="Erosión",h=np.array([[0,1,0],[1,0,1],[0,1,0]])):
    (m,n) = im.shape                            #Filas y columnas
    imf = np.zeros((m,n))                       #Crea la nueva imagen
    t = 3
    ima = np.zeros((t,t))
    o = np.zeros((t,t))
    #Mapeo
    for i in range (1,m-1):
        for j in range (1,n-1):
            for p in range (-1*round((t-1)/2),round((t-1)/2)+1):
                for q in range (-1*round((t-1)/2),round((t-1)/2)+1):
                    ima[p+1][q+1] = im[i+p][j+q]
            o = np.logical_and(ima,h,casting='same_kind')
            p = np.equal(o,h)
            imf[i][j] = p.all()
    fin = plotear(imf,nombre)
    #a=np.asarray(fin,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("erosion.png")
    return imf

def opening(imagen,nombre="Opening"):
    im1 = erosion(imagen)
    im2 = dilation(im1,nombre)
    #a=np.asarray(im2,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("opening.png")
    
def closing(imagen,nombre="Closing"):
    im1 = dilation(imagen)
    im2 = erosion(im1,nombre)
    #a=np.asarray(im2,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("closing.png")
    
def complemento(imagen,nombre="Complemento"):
    (m,n) = imagen.shape        #Filas y columnas
    com = np.zeros((m,n))       #Crea complemento
    for k in range(m):
        for l in range(n):
            if imagen[k,l]==0:
                com[k][l] = 1
            else:
                com[k][l] = 0
    plotear(com,nombre)
    return com

def ht(imagen,com,m,n,hh,hm,nombre):    
    hitt = erosion(imagen,"hit",hh)
    miss = erosion(com,"miss",hm)
    ff = np.zeros((m,n)) 
    ff = np.logical_and(hitt,miss,casting='same_kind')
    plotear(ff,nombre)
    return ff

def hit(imagen,nombre="Hit and Miss"):
    (m,n) = imagen.shape                        #Filas y columnas
    com = complemento(imagen)
    hh1 = np.array([[0,1,0],[0,1,1],[0,0,0]])   #Máscara hit
    hh2 = np.array([[0,1,0],[1,1,0],[0,0,0]])   #Máscara hit
    hh3 = np.array([[0,0,0],[1,1,0],[0,1,0]])   #Máscara hit
    hh4 = np.array([[0,0,0],[0,1,1],[0,1,0]])   #Máscara hit
    hm1 = np.array([[0,0,0],[1,0,0],[1,1,0]])   #Máscara miss
    hm2 = np.array([[0,0,0],[0,0,1],[0,1,1]])   #Máscara miss
    hm3 = np.array([[0,1,1],[0,0,1],[0,0,0]])   #Máscara miss
    hm4 = np.array([[1,1,0],[1,0,0],[0,0,0]])   #Máscara miss
    #4 esquinas
    f1 = ht(imagen,com,m,n,hh1,hm1,"final 1")
    f2 = ht(imagen,com,m,n,hh2,hm2,"final 2")
    f3 = ht(imagen,com,m,n,hh3,hm3,"final 3")
    f4 = ht(imagen,com,m,n,hh4,hm4,"final 4")
    ff1 = np.logical_or(f1,f2,casting='same_kind')
    ff2 = np.logical_or(f3,f4,casting='same_kind')
    ff = np.logical_or(ff1,ff2,casting='same_kind')
    plotear(ff1,"or 1 y 2")
    plotear(ff2,"or 3 y 4")
    plotear(ff,nombre)
    return ff

def parte1(w):
    p = 1
    b1 = 0
    b2 = 0
    b3 = 0
    b4 = 0
    if w[1,2]==0 and (w[0,2]==1 or w[0,1]==1):
        b1 = 1
    if w[0,1]==0 and (w[0,0]==1 or w[1,0]==1):
        b2 = 1
    if w[1,0]==0 and (w[2,0]==1 or w[2,1]==1):
        b3 = 1
    if w[2,1]==0 and (w[2,2]==1 or w[1,2]==1):
        b4 = 1
    c1 = b1 + b2 + b3 + b4
    s1 = (w[1,2] or w[0,2]) + (w[0,1] or w[0,0]) + (w[1,0] or w[2,0]) + (w[2,1] or w[2,2])
    s2 = (w[0,2] or w[0,1]) + (w[0,0] or w[1,0]) + (w[2,0] or w[2,1]) + (w[2,2] or w[1,2])
    c2 = min(s1,s2)
    c3 = ((w[0,2] or w[0,1]) or (not w[2,2])) and w[1,2]
    if (c3==0 and c2>=2) and (c2<=3 and c1==1):
        p = 0
    return p

def parte2(w,c1,c2):
    p = 1
    c3 = ((w[2,0] or w[2,1]) or (not w[0,0])) and w[1,0]
    if (c3==0 and c2>=2) and (c2<=3 and c1==1):
        p = 0
    return p
    
def thin(imagen,nombre="Thinning"):
    (m,n) = imagen.shape                        #Filas y columnas
    imf = np.zeros((m,n))                       #Crea la nueva imagen
    msc = np.zeros((3,3))
    c1 = 10
    c2 = 10
    #Mapeo
    for i in range (0,m-1):
        for j in range (0,n-1):
            for p in range (-1,1):
                for q in range (-1,1):
                    if (i+p)<0 or (i+p)>=m:
                        msc[p+1][q+1] = 0
                    if (j+q)<0 or (j+q)>=n:
                        msc[p+1][q+1] = 0
                    else:
                        msc[p+1][q+1] = imagen[i+p][j+q]
            imf[i][j] = parte1(msc)
            if imf[i][j] == 1:
                imf[i][j] = parte2(msc,c1,c2)
                    
    fin = plotear(imf,nombre)
    #a=np.asarray(fin,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("erosion.png")
    return imf

def thick(imagen,nombre="Thickening"):
    c = complemento(imagen)
    y = thin(c)
    im = complemento(y)
    plotear(im,nombre)
    return im

def iterar(imagen,num):
    for i in range(0,num):
        imagen = dilation(imagen,f"Hit and Miss - Dilation - Iteración:{i+1}")
        print(i)
    print(f"Iteraciones: {num}")

"""IMAGEN"""
umbral = 80
ima = Image.open("C:/Users/Acer/Pictures/E4P.png")          #Imagen
img = ima.convert('L')              #Convertir a blanco y negro
[n,m] = img.size                    #Filas y columnas
imagen = np.array(img)              #Convertir a arreglo
#Original
plt.imshow(np.asarray(imagen),cmap='gray') 
plt.title("Original")
plt.figure()
#Binario
for k in range(m):
    for l in range(n):
        if imagen[k,l]>umbral:
            imagen[k][l] = 1
        else:
            imagen[k][l] = 0
plotear(imagen,f"Binario, umbral = {umbral}")

im1 = hit(imagen)
iterar(im1,3)

#a=np.asarray(imf,dtype=np.float32)
#Image.fromarray(a.astype(np.uint8)).save("original.png")

