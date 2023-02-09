# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 22:01:14 2020

@author: ACER
"""


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def plotear(im,nombre):
    (m,n) = im.shape                            #Filas y columnas
    maximo = im.max()
    for i in range(m):
        for j in range(n):
            im[i,j] = round(im[i,j]*255/maximo)
    plt.imshow(im.astype(np.uint8),cmap='gray') 
    plt.title(nombre)
    plt.axis('off')
    plt.figure()
    return im

def dilation(imagen,nombre="Dilatación",h = np.array([[0,1,0],[1,0,1],[0,1,0]])):
    (mo,no) = imagen.shape                              #Filas y columnas
    imf = np.zeros((mo,no))
    img = binario(imagen)
    im = borde(img)
    (m,n) = im.shape
    ima = np.zeros((3,3))
    o = np.zeros((3,3))
    #Mapeo
    for i in range (1,m-1):
        for j in range (1,n-1):
            for p in range (-1,2):
                for q in range (-1,2):
                    ima[p+1][q+1] = im[i+p][j+q]
            o = np.logical_and(ima,h,casting='same_kind')
            imf[i-1][j-1] = o.any()
    #fin = plotear(imf,nombre)
    #a=np.asarray(fin,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("dilatación.png")
    return imf

def erosion(imagen,nombre="Erosión",h=np.array([[0,1,0],[1,0,1],[0,1,0]])):
    (mo,no) = imagen.shape      
    imf = np.zeros((mo,no))
    img = binario(imagen)
    im = bordee(img)
    (m,n) = im.shape
    ima = np.zeros((3,3))
    o = np.zeros((3,3))
    #Mapeo
    for i in range (1,m-1):
        for j in range (1,n-1):
            for p in range (-1,2):
                for q in range (-1,2):
                    ima[p+1][q+1] = im[i+p][j+q]
            o = np.logical_and(ima,h,casting='same_kind')
            p = np.equal(o,h)
            imf[i-1][j-1] = p.all()
    fin = plotear(imf,nombre)
    #a=np.asarray(fin,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("erosion.png")
    return imf

def opening(imagen,nombre="Opening"):
    print(imagen)
    im1 = erosion(imagen)
    print(im1)
    im2 = dilation(im1,nombre)
    #a=np.asarray(im2,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("opening.png")
    
def closing(imagen,nombre="Closing"):
    im1 = dilation(imagen)
    im2 = erosion(im1,nombre)
    #a=np.asarray(im2,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("closing.png")
    


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
    imf1 = np.ones((m,n))
    imf2 = ff*imf1
    fin = plotear(imf2,nombre)
    #a=np.asarray(fin,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("hm.png")
    return ff

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
    print(imagen.shape)
    (mo,no) = imagen.shape
    imf1 = np.zeros((mo,no))
    imf2 = np.zeros((mo,no))
    img = borde(imagen)
    im = binario(img)
    (m,n) = im.shape
    print(im.shape)
    msc = np.zeros((3,3))
    #Mapeo parte 1
    for i in range (1,m-1):
        for j in range (1,n-1):
            for p in range (-1,2):
                for q in range (-1,2):
                    msc[p+1][q+1] = im[i+p][j+q]
            imf1[i-1][j-1] = parte1(msc)
    #Mapeo parte 2
    imf3 = borde(imf1)
    for i in range (1,m-1):
        for j in range (1,n-1):
            if imf1[i-1,j-1]==1:
                for p in range (-1,2):
                    for q in range (-1,2):
                        msc[p+1][q+1] = imf3[i+p][j+q]
                imf2[i-1][j-1] = parte2(msc)
            else:
                imf2[i-1][j-1] = imf1[i-1,j-1]
    print(imf2.shape)
    fin = plotear(imf2,nombre)
    #a=np.asarray(fin,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("thin.png")
    return imf2

def thick(imagen,nombre="Thickening"):
    c = complemento(imagen)
    y = thin(c)
    imf = complemento(y,nombre)
    #a=np.asarray(imf,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("thick.png")
    return imf

def distancia(com,nombre="Distancia"):
    (m,n) = com.shape
    mx = max(m,n)
    D = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if(com[i,j]==255):
                D[i,j]=0
            if(com[i,j]==0):
                su=0
                sd=0
                sr=0
                sl=0
                #sd
                for k in range(i,m-1):
                    sd=sd+1
                    if(k+1==m-1):
                        if(com[k+1,j]==255):
                            break;
                        if(com[k+1,j]==0):
                            sd=mx
                            break;
                    if(com[k+1,j]==255):
                        break;
                #su
                for k in range(i):
                    l=i-k
                    su=su+1
                    if(l-1==0):
                        if(com[l-1,j]==255):
                            break;
                        if(com[l-1,j]==0):
                            su=mx
                            break;
                    if(com[l-1,j]==255):
                        break;
                #sr
                for x in range(j,n-1):
                    sr=sr+1
                    if(x+1==n-1):
                        if(com[i,x+1]==255):
                            break;
                        if(com[i,x+1]==0):
                            sr=mx
                            break;
                    if(com[i,x+1]==255):
                        break;
                #sl
                for x in range(j):
                    y=j-x
                    sl=sl+1
                    if(y-1==0):
                        if(com[i,y-1]==255):
                            break;
                        if(com[i,y-1]==0):
                            sl=mx
                            break;
                    if(com[i,y-1]==255):
                        break;
                if(su==0):
                    su=mx
                if(sd==0):
                    sd=mx
                if(sr==0):
                    sr=mx
                if(sl==0):
                    sl=mx
                
                c1=min(su,sd,sr,sl)
                #print("i:",i,"j:",j)
                #print("su:", su,"sd:", sd, "sr:", sr, "sl:", sl,"c1:",c1)
                D[i,j]=c1
    d = D*5
    maximo = d.max()
    p = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            p[i,j] = round(d[i,j]*255/maximo)
    plt.imshow(p.astype(np.uint8),cmap='gray') 
    plt.title(nombre)
    plt.axis('off')
    plt.figure()
    return d

def ske(imagen,nombre="Skeleton"):
    (m,n) = imagen.shape
    skel = np.zeros((m,n))
    msc = np.zeros((3,3))
    mp = np.array([[0,1,0],[1,1,1],[0,1,0]])
    s = np.zeros((3,3))
    com = complemento(imagen)
    D = distancia(com)
    d = borde(D)
    #Mapeo
    for i in range (1,m+1):
        for j in range (1,n+1):
            for p in range (-1,2):
                for q in range (-1,2):
                    msc[p+1][q+1] = d[i+p][j+q]
            c1 = mp*msc
            c2 = mp*msc[1,1]
            #print(f"({i},{j}):{d[i,j]}\n {c1} \n {c2}")
            c = np.greater_equal(c2,c1)
            e = np.equal(c1,s)
            if e.all() == 1:
                skel[i-1][j-1] = 0
            else:
                skel[i-1][j-1] = c.all()
    print(skel.shape)
    plotear(skel,nombre)
    #a=np.asarray(skel,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("Ske.png")

def sk(imagen,nombre="Skeleton"):
    im = binario(imagen)
    (m,n) = im.shape
    r = np.zeros((m,n))
    s = 0
    c = 0
    while c==0:
        ima = im
        im = erosion(im)
        p = np.equal(im,r)
        c = p.all()
        s = s+1
        print(s)  
    print(ima)
    plotear(ima,nombre+"-erosiones")
    im1 = opening(ima,nombre+"-openning")
    print(im1)
    imf = np.subtract(ima,im1)
    plotear(imf,nombre)

def fill(imagen,nombre="Fill"):
    (mo,no) = imagen.shape            
    imf = np.zeros((mo,no))
    img = binario(imagen)
    im = borde(img)
    (m,n) = im.shape
    h = np.array([[1,1,1],[1,0,1],[1,1,1]])
    ima = np.zeros((3,3))
    o = np.zeros((3,3))
    #Mapeo
    for i in range (1,m-1):
        for j in range (1,n-1):
            for p in range (-1,2):
                for q in range (-1,2):
                    ima[p+1][q+1] = im[i+p][j+q]
            if ima[1,1]==1:
                imf[i-1][j-1] = 1
            else:
                o = np.logical_and(ima,h,casting='same_kind')
                p = np.equal(o,h)
                imf[i-1][j-1] = p.all()
    fin = plotear(imf,nombre)
    #a=np.asarray(fin,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("fill.png")
    return imf

def bd(imagen,nombre="Boundary Extraction"):
    h = np.ones((3,3))
    im = erosion(imagen,nombre+" - Erosion")
    imf = np.subtract(imagen,im)
    fin = plotear(imf,nombre)
    #a=np.asarray(fin,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("bd.png")
    return imf

def ref(imagen,nombre="Region Filling"):
    com = complemento(imagen)
    (m,n) = imagen.shape 
    h = np.array([[0,1,0],[1,1,1],[0,1,0]])
    im = np.zeros((m,n))
    im[20,175] = 1
    s = 0
    c = 0
    while c==0:
        imf = im
        im = dilation(im,nombre+f" - Dilation - Iteración:{s}",h)
        im = np.logical_and(com,im)
        p = np.equal(imf,im)
        c = p.all()
        s = s+1
        print(s)
    imf = np.logical_or(im,imagen)
    fin = plotear(imf,nombre)
    #a=np.asarray(fin,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("RegionFilling.png")
    return imf

def ext(imagen,nombre="Extraction"):
    (m,n) = imagen.shape 
    h = np.array([[0,1,0],[1,1,1],[0,1,0]])
    im = np.zeros((m,n))
    im[20,175] = 1
    s = 0
    c = 0
    while c==0:
        imf = im
        im = dilation(im,nombre+f" - Dilation - Iteración:{s}",h)
        im = np.logical_and(imagen,im)
        p = np.equal(imf,im)
        c = p.all()
        s = s+1
        print(s)
    imf = np.logical_and(im,imagen)
    fin = plotear(imf,nombre)
    #a=np.asarray(fin,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("Extraction.png")
    return imf

def complemento(imagen,nombre="Complemento"):
    im = binario(imagen)
    print(im.shape)
    (m,n) = im.shape                        #Filas y columnas
    """
    for k in range(m):
        for l in range(n):
            print(im[k,l]) #"""
    com = np.zeros((m,n))       #Crea complemento
    for k in range(m):
        for l in range(n):
            if im[k,l]==0:
                com[k][l] = 1
            else:
                com[k][l] = 0
    plotear(com,nombre)
    #a=np.asarray(com,dtype=np.float32)
    #Image.fromarray(a.astype(np.uint8)).save("com.png")
    return com

def borde(im):
    (m,n) = im.shape
    imagen = np.zeros((m+2,n+2))
    for k in range(m):
        for l in range(n):
            imagen[k+1][l+1] = im[k][l]
    return imagen

def bordee(im):
    (m,n) = im.shape
    imagen = np.ones((m+2,n+2))
    for k in range(m):
        for l in range(n):
            imagen[k+1][l+1] = im[k][l]
    return imagen

def iterar(imagen,num,nombre):
    h = np.ones((3,3))
    for i in range(0,num):
            imagen = erosion(imagen,f"{nombre} - Iteración:{i+1}")
            print(i+1,imagen)
    return imagen 



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

"""IMAGEN"""
umbral = 110
ima = Image.open("C:/Users/ACER/Pictures/Pruebas/negat.png")          #Imagen
img = ima.convert('L')              #Convertir a blanco y negro
[n,m] = img.size                    #Filas y columnas
#print(img.size)
plt.imshow(np.asarray(img),cmap='gray') 
plt.title("Original")
plt.figure()
imagen = binario(np.array(img),umbral)
plotear(imagen,f"Binario, umbral = {umbral}")
            
#imagen = np.array([[0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,1,0,1,1,0,0],[0,1,1,1,1,1,1,0],[0,0,1,1,1,1,1,0],[0,0,0,1,1,1,1,0],[0,0,0,0,1,1,0,0],[0,0,0,0,0,1,0,0]])   
h = np.ones((3,3))
h1 = np.array([[0,0,1],[0,1,0],[0,1,1]])
h2 = np.array([[1,1,0],[0,1,0],[1,0,0]])
imagena = np.array([[1,0,1,0,1,0,1],[0,1,0,0,0,0,0],[1,0,1,0,1,0,1],[0,0,0,1,0,0,0],[1,0,1,0,1,0,1],[0,0,0,0,0,1,0],[1,0,1,0,1,0,1]])   
#im = np.array([[0,0,1,1,1,0,0,0],[0,0,0,1,1,1,0,0],[0,0,0,0,1,1,1,0],[0,0,0,0,0,1,1,1],[0,0,0,0,1,1,0,0],[0,0,0,1,1,0,0,0],[0,0,1,1,0,0,0,0],[0,1,1,0,0,0,0,0]])
#im = np.array([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])
imagenb = borde(np.ones((6,6)))
imagenc = np.array([[1,1,1,1,1,1,1,1],[1,0,1,1,1,1,1,1],[1,1,1,0,1,1,1,1],[1,1,1,1,1,1,1,1],[0,1,1,1,0,1,1,1],[1,1,1,1,1,0,1,1],[1,1,1,0,1,1,1,1],[1,1,1,1,1,1,1,1]])
imagend = np.array([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,1,1,1,1,1,0],[0,0,1,0,0,0,1,0],[0,0,1,0,0,1,1,0],[0,0,0,1,0,0,1,0],[0,0,0,0,1,1,1,0],[0,0,0,0,0,0,0,0]])
imagene = np.array([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0],[0,0,1,1,0,0,1,0],[0,0,1,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,0]])


#print(imagenb)
#(m,n) = im.shape

plotear(imagen,"Arreglo")
im = ext(imagen)
fill(imagen)
thin(imagen)
hit(imagen)
sk(imagen)
thick(imagen)
imf = iterar(imagen,4,"Erosión")
closing(imf)
imf = bd(imagen)
ref(imf)
ext(imagen)
iterar(imagen,3,erosion)

#a=np.asarray(imf,dtype=np.float32)
#Image.fromarray(a.astype(np.uint8)).save("original.png")



