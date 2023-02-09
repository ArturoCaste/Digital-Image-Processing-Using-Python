# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 22:01:14 2020

@author: ACER
"""


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

def plotear(imagen,nombre):
    plt.imshow(np.asarray(imagen),cmap='gray') 
    plt.title(nombre)
    plt.figure()
    
def guardar(imagen,nombre):
    imf = imagen*255
    a=np.asarray(imf,dtype=np.float32)
    Image.fromarray(a.astype(np.uint8)).save(f"{nombre}.png")

def mascara(imagen,m,n,i,j,v=0):
    msc = np.zeros((3,3))
    for p in range (-1,2):
        for q in range (-1,2):
            x = i+p
            y = j+q
            if (x > m-1) or (x<0) or (y > n-1) or (y < 0):
                msc[p+1][q+1] = v
            else:
                msc[p+1][q+1] = imagen[x][y]
    return msc

def dilation(imagen,nombre="Dilatación",h = np.array([[1,1,1],[1,1,1],[1,1,1]])):
    #h = np.array([[0,0,1],[0,1,0],[0,1,1]])
    (m,n) = imagen.shape
    imf = np.zeros((m,n))
    for i in range (m):
        for j in range (n):
            msc = mascara(imagen, m, n, i, j)
            #print(f"{i},{j} \n {msc}")
            o = np.logical_and(msc,h,casting='same_kind')
            imf[i][j] = o.any()
    #plotear(imf,nombre)
    #guardar(imf,nombre)
    return imf

def erosion(imagen,nombre="Erosión",h = np.array([[1,1,1],[1,1,1],[1,1,1]])):
    #h = np.array([[1,1,0],[0,1,0],[1,0,0]])
    (m,n) = imagen.shape
    imf = np.zeros((m,n))
    for i in range (m):
        for j in range (n):
            msc = mascara(imagen, m, n, i, j, 1)
            o = np.logical_and(msc,h,casting='same_kind')
            p = np.equal(o,h)
            imf[i][j] = p.all()
    #plotear(imf,nombre)
    #guardar(imf,nombre)
    return imf

def opening(imagen,nombre="Opening"):
    im = erosion(imagen)
    imf = dilation(im)
    plotear(imf,nombre)
    guardar(imf,nombre)
    return imf
    
def closing(imagen,nombre="Closing"):
    im = dilation(imagen)
    imf = erosion(im)
    plotear(imf, nombre)
    guardar(imf,nombre)
    return imf
    
def ht(imagen,com,m,n,hh,hm):    
    hitt = erosion(imagen,"hit",hh)
    miss = erosion(com,"miss",hm)
    ff = np.logical_and(hitt,miss,casting='same_kind')
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
    f1 = ht(imagen,com,m,n,hh1,hm1)
    f2 = ht(imagen,com,m,n,hh2,hm2)
    f3 = ht(imagen,com,m,n,hh3,hm3)
    f4 = ht(imagen,com,m,n,hh4,hm4)
    ff1 = np.logical_or(f1,f2,casting='same_kind')
    ff2 = np.logical_or(f3,f4,casting='same_kind')
    imf = np.logical_or(ff1,ff2,casting='same_kind')
    plotear(imf,nombre)
    #guardar(imf,nombre)
    return imf

def parte1(w):
    p = w[1,1]
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

def parte2(w):
    p = w[1,1]
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
    c3 = ((w[2,0] or w[2,1]) or (not w[0,0])) and w[1,0]
    if (c3==0 and c2>=2) and (c2<=3 and c1==1):
        p = 0
    return p
    
def thin(imagen,nombre="Thinning"):
    (m,n) = imagen.shape
    im = np.zeros((m,n))
    imf = np.zeros((m,n))
    msc = np.zeros((3,3))
    for i in range (m):         #Mapeo parte 1
        for j in range (n):
            msc = mascara(imagen, m, n, i, j,1)
            im[i][j] = parte1(msc)
    for i in range (m):         #Mapeo parte 2
        for j in range (m):
            if im[i,j]==1:
                msc = mascara(im, m, n, i, j,1)
                imf[i][j] = parte2(msc)
            else:
                imf[i][j] = im[i,j]
    plotear(imf,nombre)
    guardar(imf,nombre)
    return imf

def thick(imagen,nombre="Thickening"): #v=1
    c = complemento(imagen)
    y = thin(c)
    imf = complemento(y)
    plotear(imf, nombre)
    guardar(imf,nombre)
    return imf

def sk(imagen,nombre="Skeleton"):
    (m,n) = imagen.shape
    imf = np.zeros((m,n))
    D = ndimage.distance_transform_edt(imagen)
    for i in range (m):
        for j in range (n):
            msc = mascara(D, m, n, i, j)
            a = msc[0,1]
            b = msc[1,2]  
            c = msc[2,1]
            d = msc[1,0] 
            E = max(a,b,c,d)
            F = msc[1,1]
            if(E!=0):
                if F>=E:
                    imf[i,j]=1
    plotear(D,"Distancia")
    plotear(imf,nombre) 
    guardar(imf,nombre)      

def fill(imagen,nombre="Fill",h = np.array([[1,1,1],[1,0,1],[1,1,1]])):
    (m,n) = imagen.shape
    imf = np.zeros((m,n))
    for i in range (m):
        for j in range (n):
            msc = mascara(imagen, m, n, i, j, 1)
            if msc[1,1]==1:
                imf[i][j] = 1
            else:
                o = np.logical_and(msc,h,casting='same_kind')
                p = np.equal(o,h)
                imf[i][j] = p.all()
    plotear(imf,nombre)
    guardar(imf,nombre)
    return imf

def bd(imagen,nombre="Boundary Extraction"):
    h = np.ones((3,3))
    im = erosion(imagen,nombre,h)
    imf = imagen - im
    plotear(imf, nombre)
    guardar(imf,nombre)
    return imf

def refill(imagen,a,b,nombre="Region Filling"):
    com = complemento(imagen)
    (m,n) = imagen.shape 
    h = np.array([[0,1,0],[1,1,1],[0,1,0]])
    im = np.zeros((m,n))
    im[a,b] = 1
    s = 0
    c = 0
    while c==0:
        imf = im
        im = dilation(im,nombre,h)
        im = np.logical_and(com,im)
        p = np.equal(imf,im)
        c = p.all()
        s = s+1
        print(s)
    imf = np.logical_or(im,imagen)
    plotear(imf,nombre)
    guardar(imf,nombre)
    return imf

def ext(imagen,a,b,nombre="Extraction"):
    (m,n) = imagen.shape 
    h = np.array([[0,1,0],[1,1,1],[0,1,0]])
    im = np.zeros((m,n))
    im[a,b] = 1
    s = 0
    c = 0
    while c==0:
        imf = im
        im = dilation(im,nombre,h)
        im = np.logical_and(imagen,im)
        p = np.equal(imf,im)
        c = p.all()
        s = s+1
        print(s)
    imf = np.logical_and(im,imagen)
    plotear(imf,nombre)
    guardar(imf,nombre)
    return imf

def binario(imagen,umbral=0):
    (m,n) = imagen.shape
    im = np.zeros((m,n))
    for k in range(m):
        for l in range(n):
            if imagen[k,l]>umbral:
                im[k][l] = 1
            else:
                im[k][l] = 0
    return im

def complemento(imagen,nombre="Complemento"):
    (m,n) = imagen.shape 
    com = np.zeros((m,n))       #Crea complemento
    for k in range(m):
        for l in range(n):
            if imagen[k,l]==0:
                com[k][l] = 1
            else:
                com[k][l] = 0
    #plotear(com,nombre)
    #guardar(com,nombre)
    return com

def iterar(imagen,num,nombre):
    for i in range(0,num):
        imagen = thick(imagen)
        plotear(imagen,f"{nombre} - Iteración:{i+1}")

"""Convierte la imagen a arreglo"""
umbral = 105
im = "C:/Users/ACER/Pictures/Pruebas/negat.png"
imagen = np.array((Image.open(im)).convert('L'))
plotear(imagen, "Original")
imagen = binario(imagen,umbral)
plotear(imagen, f"Binario - Umbral={umbral}")

#imagen = np.array([[0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,1,0,1,1,0,0],[0,1,1,1,1,1,1,0],[0,0,1,1,1,1,1,0],[0,0,0,1,1,1,1,0],[0,0,0,0,1,1,0,0],[0,0,0,0,0,1,0,0]])   
#imagen = np.array([[0,0,1,1,1,0,0,0],[0,0,0,1,1,1,0,0],[0,0,0,0,1,1,1,0],[0,0,0,0,0,1,1,1],[0,0,0,0,1,1,0,0],[0,0,0,1,1,0,0,0],[0,0,1,1,0,0,0,0],[0,1,1,0,0,0,0,0]])
#imagen = np.array([[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,1],[1,1,1,1,0,1,0,1],[1,1,1,1,0,0,0,1],[0,0,1,1,0,0,0,1],[1,0,1,1,1,1,1,1],[0,0,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]])
#imagen = np.array([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])

#print(imagen)
#thin(imagen)
#fill(imagen)
#opening(imagen)
#closing(imagen)
#thin(imagen)
#iterar(imagen,6, "thick")
#complemento(imagen)
#im = closing(imagen)
#im = hit(imagen)
#thick(imagen) #v=1 en thinning
#ext(imagen, 223, 183)
#bd(imagen)
thick(imagen)

#sk(imagen)
