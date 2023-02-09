# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 10:56:09 2020

@author: ACER
"""


import numpy as np
from PIL import Image
from numpy import array
import math as mas
from matplotlib import pyplot as plt

"""SUMA DE GRISES de dos imagenes"""

def identidad(imagen1):
    Im = Image.open(imagen1)
    im = Im
    im.show()
    m = im.size[0] #redefinimos las filas 
    n = im.size[1] #redefinimos las columnas 
    l = 256
    h = np.zeros(l) #creamos un vector de ceros
    i = 0 #Hacemos un barrido 
    while i < m:
       j = 0 #Les pasamos los pixeles de la imagen al vector de ceros 
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h) #ploteamos el histograma sin procesar
    plt.show() #lo mostramos en pantalla
    im =  Image.open(imagen1)
    i = 0 
    while i < im.size[0]:
        j = 0
        while j < im.size[1]:
            valor = im.getpixel((i,j))
            im.putpixel((i, j),(valor))
            j+=1
        i+=1
    im.show()
    im.save("imagen1_iden.jpeg")
    ima = Image.open("imagen1_iden.jpeg")
    m = ima.size[0]      
    n = ima.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()


def negativo(imagen1):
    Im = Image.open(imagen1)
    im = Im
    im.show()
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()
    im =  Image.open(imagen1)
    i = 0 
    while i < im.size[0]:
        j = 0
        while j < im.size[1]:
            gris = im.getpixel((i,j))
            valor = 255 - gris
            im.putpixel((i, j),valor)
            j+=1
        i+=1
    im.show()
    im.save("imagen1_neg.jpeg")
    ima = Image.open("imagen1_neg.jpeg")
    im = ima
    m = im.size[0]      
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()

    

    
def gamma(imagen1):
    Im = Image.open(imagen1)
    im = Im
    im.show()
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()
    im = Image.open(imagen1)
    g = 0.8
    i = 0 
    while i < im.size[0]:
        j = 0
        while j < im.size[1]:
            valor = round(255*((im.getpixel((i,j))/255)**g))
            im.putpixel((i, j),(valor))
            j+=1
        i+=1
    im.show()
    im.save("imagen1_gam.jpeg")
    Im = Image.open("imagen1_gam.jpeg")
    im = Im
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()

def logar(imagen1):
    Im = Image.open(imagen1)
    im = Im
    im.show()
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()
    im =  Image.open(imagen1)
    i = 0 
    while i < im.size[0]:
        j = 0
        while j < im.size[1]:
            valor = im.getpixel((i,j))
            valor = valor + 1
            valor =  int(round((255/mas.log10(256))*mas.log(valor, 10)))
            if valor >= 255:
                valor = 255
            im.putpixel((i, j),valor)
            j+=1
        i+=1
    im.show()
    im.save("imagen1_log.jpeg")
    ima = Image.open("imagen1_log.jpeg")
    im = ima
    m = im.size[0]      
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()
    im =  Image.open(imagen1)


    
def seno(imagen1):
    Im = Image.open(imagen1)
    im = Im
    im.show()
    k = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < k:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()
    im =  Image.open(imagen1)
    r = (3.1416/2)*(1/255)
    i = 0 
    while i < im.size[0]:
        j = 0
        while j < im.size[1]:
            valor = im.getpixel((i,j))
            valor =round(255*mas.sin(r*valor))
            im.putpixel((i, j),(valor))
            j+=1
        i+=1
    im.show()
    im.save("imagen1_sen.jpeg")
    ima = Image.open("imagen1_sen.jpeg")
    im = ima
    m = im.size[0]      
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()

def coseno(imagen1):
    Im = Image.open(imagen1)
    im = Im
    im.show()
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()
    im = Image.open(imagen1)
    r = (3.1416/2)*(1/255)
    i = 0 
    while i < im.size[0]:
        j = 0
        while j < im.size[1]:
            valor = im.getpixel((i,j))
            valor= round(255*(1 - mas.cos(r*valor)))
            im.putpixel((i, j),(valor))
            j+=1
        i+=1
    im.show()
    im.save("imagen1_cos.jpeg")
    ima = Image.open("imagen1_cos.jpeg")
    im = ima
    m = im.size[0]      
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()

def exponencial(imagen1):
    Im = Image.open(imagen1)
    im = Im
    im.show()
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()
    im =  Image.open(imagen1)
    g = (255)/(1-mas.exp(-1))
    i = 0 
    while i < im.size[0]:
        j = 0
        while j < im.size[1]:
            valor = im.getpixel((i,j))
            u=(-1)*(valor/255)
            u=1-mas.exp(u)
            u=g*u
            valor = int(round(u))
            im.putpixel((i, j),(valor))
            j+=1
        i+=1
    im.show()
    im.save("imagen1_exp.jpeg")
    ima = Image.open("imagen1_exp.jpeg")
    im = ima
    m = im.size[0]      
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()
    
            

            

def suma(imagen1,imagen2):
    imagen1 = Image.open(imagen1)
    imagen2 = Image.open(imagen2)
    imagen1.show()
    imagen2.show()
    im = imagen1.convert('L') 
    imagen2 = imagen2.convert('L') 
    im = im
    i = 0
    while i < im.size[0]:
        j = 0
        while j < im.size[1]:
            valor1 = imagen2.getpixel((i, j))
            valor = im.getpixel((i, j))
            valornuevo = valor + valor1
            if valornuevo >= 255:
                valornuevo = 255
            im.putpixel((i, j),(valornuevo))
            j+=1
        i+=1
    im.show()
    im.save("imagen1_sum.jpeg")
    ima = Image.open("imagen1_sum.jpeg")
    im = ima
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()



"""Suma de grises en la misma imagen"""
def sumae(im,escala):
    im = Image.open(im)
    im.show()
    im = im.convert('L') 
    imesc = im
    i = 0
    while i < imesc.size[0]:
        j = 0
        while j < imesc.size[1]:
            valor = imesc.getpixel((i, j))
            valore = valor + escala 
            if valore >= 255:
                valore = 255
            imesc.putpixel((i, j),(valore))
            j+=1
        i+=1
    imesc.show()
    imesc.save("imagen1_esc.jpeg")
    ima = Image.open("imagen1_esc.jpeg")
    im = ima
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()

"""Resta de grises en la misma escala de grises """
def restae(im,restaesc):
    im = Image.open(im)
    im.show()
    im = im.convert('L') 
    imres = im
    i = 0
    while i < imres.size[0]:
        j = 0
        while j < imres.size[1]:
            valor = imres.getpixel((i, j))
            valorest = valor - restaesc
            if valorest < 0:
                valorest = 0
            imres.putpixel((i, j),(valorest))
            j+=1
        i+=1
    imres.show()
    imres.save("imagen1_grs.jpeg")
    ima = Image.open("imagen1_grs.jpeg")
    im = ima
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()


    
"""Resta de dos imagenes (escala de grises)"""
def resta(ima1,ima2):
    im1 = Image.open(ima1)
    im1.show()
    im2 = Image.open(ima2)
    im2.show()
    ima1 = im1.convert('L') 
    ima2 = im2.convert('L') 
    im1res = ima1
    im2res = ima2
    i = 0
    while i < im1res.size[0]:
        j = 0
        while j < im1res.size[1]:
            valor1 = im1res.getpixel((i,j))
            valor2 = im2res.getpixel((i,j))
            valor = valor1 - valor2
            if valor < 0:
                valor = 0
            im1res.putpixel((i, j),(valor))
            j+=1
        i+=1
    im1res.show()
    im1res.save("imagen1_resn.jpeg")
    ima = Image.open("imagen1_resn.jpeg")
    im = ima
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()

    
"""Multiplicación de grises en la misma escala"""
def multi(im,multiplicando):
    im = Image.open(im)
    im.show()
    im = im.convert('L') 
    imulti = im
    i = 0
    while i < imulti.size[0]:
        j = 0
        while j < imulti.size[1]:
            valor = imulti.getpixel((i, j))
            valorm = valor * multiplicando
            if valorm > 255:
                valorm = 255
                if valorm < 0:
                    valorm = 0 
            imulti.putpixel((i, j),(valorm))
            j+=1
        i+=1
    imulti.show()
    imulti.save("imagen1_multi.jpeg")
    ima = Image.open("imagen1_multi.jpeg")
    im = ima
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()
  
    
    
    
"""Multiplicación de 2 grises"""
def mul(imagen1,imagen2):
    im1 = Image.open(imagen1)
    im1.show()
    im2 = Image.open(imagen2)
    im2.show()
    ima1 = im1.convert('L') 
    ima2 = im2.convert('L') 
    imulti1 = ima1
    imulti2 = ima2
    i = 0
    while i < imulti1.size[0]:
        j = 0
        while j < imulti1.size[1]:
            valor1 = imulti1.getpixel((i,j))
            valor2 = imulti2.getpixel((i,j))
            valorf =int(round( valor1 * valor2))
            if valorf >= 255:
                valorf = 255
            imulti1.putpixel((i, j),(valorf))
            j+=1
        i+=1
    imulti1.show()
    imulti1.save("imagen1_exp.jpeg")
    ima = Image.open("imagen1_exp.jpeg")
    im = ima
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()

    
"""División de grises entre escalar"""
def dive(imagen,factor):
    im = Image.open(imagen)
    im.show()
    ima1 = im.convert('L') 
    imdiv = ima1
    i = 0
    while i < imdiv.size[0]:
        j = 0
        while j < imdiv.size[1]:
            valor = int(round(imdiv.getpixel((i, j))))
            if factor == 0:
                factor = 1
            valorf = int((round(valor / factor)))
            if valorf < 0:
                valorf = 0
            imdiv.putpixel((i, j),(valorf))
            j+=1
        i+=1
    imdiv.show()
    imdiv.save("imagen1_div.jpeg")
    ima = Image.open("imagen1_div.jpeg")
    im = ima
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()

    
"""División se dos grises"""
def div(ima1,ima2):
    im1 = Image.open(ima1)
    im1.show()
    im2 = Image.open(ima2)
    im2.show()
    im1 = im1.convert('L')
    im2 = im2.convert('L') 
    imdiv1 = im1
    imdiv2 = im2
    i = 0
    while i < imdiv1.size[0]:
        j = 0
        while j < imdiv1.size[1]:
            valor1 = int(round(imdiv1.getpixel((i,j))))
            valor2 = int(round(imdiv2.getpixel((i,j))))
            if valor2 == 0:
                valor2 = 1
            valor1 = round(valor1 / valor2)
            if valor1 < 0:
                valor1 = 0
            imdiv1.putpixel((i, j),(valor1))
            j+=1
        i+=1
    imdiv1.show()
    imdiv1.save("imagen1_div1.jpeg")
    ima = Image.open("imagen1_div1.jpeg")
    im = ima
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()
    
    
    
    
def umbral(im):
    im = Image.open(im)
    im.show()
    imbra = im
    T = 50
    i = 0
    while i < imbra.size[0]:
        j = 0
        while j < imbra.size[1]:
            valor = imbra.getpixel((i, j)) + 1
            if valor > T:
                valor = 1
            if  valor <= T:
                valor = 0
            imbra.putpixel((i, j),(valor))
            j+=1
        i+=1
    imbra.show()
    imbra.save("imagen1_grs.jpeg")
    ima = Image.open("imagen1_grs.jpeg")
    im = ima
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()

    
def umbralf(im):
    im = Image.open(im)
    im.show()
    imbra = im
    T = 90
    i = 0
    while i < imbra.size[0]:
        j = 0
        while j < imbra.size[1]:
            valor = imbra.getpixel((i, j))
            if  -T <= valor <= T:
                valor = 0
            else:
                valor = imbra.getpixel((i, j))
            imbra.putpixel((i, j),(valor))
            j+=1
        i+=1
    imbra.show()
    imbra.save("imagen1_grs.jpeg") #Guardamos la imagen
    Im = Image.open("imagen1_grs.jpeg") #Llamamos a la imagen  
    im = Im
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()
    

    
def umbrals(im):
    im = Image.open(im)
    im.show()
    imbra = im
    T = 90
    i = 0
    while i < imbra.size[0]:
        j = 0
        while j < imbra.size[1]:
            valor = imbra.getpixel((i, j))
            if  -T <= valor <= T:
                valor = 0
            if   valor > T:
                valor =  imbra.getpixel((i, j)) - T
            if   valor < -T:
                valor =  imbra.getpixel((i, j)) + T
            imbra.putpixel((i, j),(valor))
            j+=1
        i+=1
    imbra.show()
    imbra.save("imagen1_grs.jpeg")
    ima = Image.open("imagen1_grs.jpeg")
    im = ima
    m = im.size[0]     
    n = im.size[1]      
    l = 256
    h = np.zeros(l)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)
    plt.show()
    
    
def Histo(imagen1):
    im = Image.open(imagen1)
    m = im.size[0]      
    n = im.size[1]      
    h1 = np.zeros(256)   
    h2 = np.zeros(256)
    i = 0
    while i < m:
       j = 0
       while j < n:
           h1[im.getpixel((i, j))] = h1[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    H = h1/(m*n)      
    p = np.zeros(256)
    for i in range(0,256,1):
       p[i]=p[i-1] + H[i]
    v = np.zeros(256)
    for i in range(0,256,1):
       v[i]=round((255)*p[i])
    i = 0
    while i < m:
        j = 0
        while j < n:
            valor = v[im.getpixel((i, j))]
            im.putpixel((i, j),(int(valor)))
            j+=1
        i+=1
    im.save("equal.jpg")
    im.show()
    i = 0
    while i < m:
       j = 0
       while j < n:
            h2[im.getpixel((i, j))] = h2[im.getpixel((i, j))] + 1
            j+=1
       i+=1
    H2 = h2/(m*n)
    p2 = np.zeros(256)
    for i in range(0,256,1):
        p2[i]=p2[i-1] + H2[i]
    plt.plot(p)
    plt.show()

def constras(im):
    im = Image.open(im)
    im.show()
    M= 186
    L= 4
    g=(253)/(M-L)
    i = 0
    while i < im.size[0]:
        j = 0
        while j < im.size[1]:
            valor = im.getpixel((i, j))
            if   L <= valor <= M:
                valor = valor - L
                valor = (g*valor) + 1
                valor = int(round(valor))
            if   valor > M:
                valor =  255
            if   valor < L:
                valor = 0 
            im.putpixel((i, j),(valor))
            j+=1
        i+=1
    im.show()
    im.save("imagen1_cont.jpeg") # Se guarda la imagen creada 
    ima = Image.open("imagen1_cont.jpeg") # Se abre la imagen creada
    im = ima #renombramos la variable
    m = im.size[0] #renombramos las filas 
    n = im.size[1] # Renombramos las columnas 
    l = 256 
    h = np.zeros(l) #creamos un vector de ceros
    i = 0 #Hacemos un barrido de filas y columnas 
    while i < m:
       j = 0
       while j < n: #Les pasamos los pixeles de la imagen al vector de ceros 
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h) #ploteamos el histograma
    plt.show()
