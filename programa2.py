# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 21:21:56 2020

@author: ACER
"""

import numpy as np
from PIL import Image

import math as mas
from matplotlib import pyplot as plt

"""SUMA DE GRISES de dos imagenes"""

def grafica(vec,Titulo): #Definimod la función, pedimos el 
    #vector numpy  y el titulo de la grafica
    v = vec #definimos la nueva variable 
    plt.plot(v)#ploteamos el vector
    plt.title(Titulo) # le damos titulo, indices y mostramos 
    #la grafica
    plt.xlabel("Entrada de la escala de grises")
    plt.ylabel("Salida de la escala de grises")
    plt.legend()
    plt.show()
    

def identidad(imagen1): #Definimos la función y pedimos
    #la imagen a tratar
    Im = Image.open(imagen1)#Abrimos la imagen
    im = Im # Redefinimos la imagen
    im.show() #mostramos la imagen
    m = im.size[0] #redefinimos las filas 
    n = im.size[1] #redefinimos las columnas 
    l = 256
    z = np.zeros(l) #creamos un vector de ceros
    i = 0 #Hacemos un barrido 
    while i < m:
       j = 0 #Les pasamos los pixeles de la imagen al vector de ceros 
       while j < n:
           z[im.getpixel((i, j))] = z[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(z) #ploteamos el histograma sin procesar
    plt.show() #lo mostramos en pantalla
    im =  Image.open(imagen1) #Abrimos de nuevo la imagen 
    i = 0 #aplicamos la funcion identidad asignando el mismo valor 
    # de pixel a cada pixel 
    while i < im.size[0]:
        j = 0
        while j < im.size[1]:
            valor = im.getpixel((i,j))
            im.putpixel((i, j),(valor))
            j+=1
        i+=1
    im.show() # Mostramos la imagen
    im.save("imagen1_iden.jpeg") #salvamos la imagen
    ima = Image.open("imagen1_iden.jpeg")#abrimos la imagen
    m = ima.size[0] #redefinimos las filas
    n = ima.size[1] #redefinimos las columnas
    l = 256 # redifinimos a l
    z = np.zeros(l) #creamos un arreglo numpy de ceros 
    i = 0 #hacemos un barrido y le damos el valor pixel por pixel
    # de la nueva imagen al arreglo de ceros
    while i < m:
       j = 0
       while j < n:
           z[im.getpixel((i, j))] = z[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(z) #ploteamos el histograma
    plt.show() #mostramos el histograma
    z = np.zeros(l) #creamos un arreglo numpy de ceros y ploteamos
    #la función identidad utilizando la funcion grafica
    for i in range (0,l):
        z[i] = i
    grafica(z,"Identidad")
    

def negativo(imagen1):#Definimos la función y pedimos
    #la imagen a tratar
    Im = Image.open(imagen1)  #Abrimos la imagen
    im = Im # Redefinimos la imagen
    im.show() #mostramos la imagen
    m = im.size[0] #redefinimos las filas 
    n = im.size[1] #redefinimos las columnas 
    l = 256
    h = np.zeros(l)  #creamos un vector de ceros
    i = 0 #Hacemos un barrido
    while i < m:
       j = 0
       while j < n:#Les pasamos los pixeles de la imagen
       #al vector de ceros 
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1  
    plt.plot(h)  #ploteamos el histograma sin procesar
    plt.show() #lo mostramos en pantalla
    im =  Image.open(imagen1) #Abrimos de nuevo la imagen 
    i = 0 #aplicamos la funcion negativo asignando el valor de
    #pixel por pixel de la resta de L con el valor de
    #entrada
    while i < im.size[0]:
        j = 0
        while j < im.size[1]:
            gris = im.getpixel((i,j))
            valor = 255 - gris
            im.putpixel((i, j),valor)
            j+=1
        i+=1
    im.show() # Mostramos la imagen
    im.save("imagen1_neg.jpeg") #salvamos la imagen
    ima = Image.open("imagen1_neg.jpeg")#abrimos la imagen
    im = ima # redifinimos la variable
    m = im.size[0] #redefinimos las filas
    n = im.size[1] #redefinimos las columnas   
    l = 256
    h = np.zeros(l) #creamos un arreglo numpy de ceros 
    i = 0
    #hacemos un barrido y le damos el valor pixel por pixel
    # de la nueva imagen al arreglo de ceros
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)   #ploteamos el histograma
    plt.show()   #mostramos el histograma
    neg = np.zeros(l)     #creamos un arreglo numpy de 
    #ceros y ploteamos la función identidad
    #utilizando la funcion grafica
    for i in range (0,l):
        neg[i] = l-1-i
    grafica(neg,"Negativo de una imagen")
 

   
def gamma(imagen1): #Definimos la función y pedimos
#la imagen a tratar
    Im = Image.open(imagen1)#Abrimos la imagen
    im = Im  # Redefinimos la imagen
    im.show()  #mostramos la imagen
    m = im.size[0]  #redefinimos las filas 
    n = im.size[1] #redefinimos las columnas     
    l = 256
    h = np.zeros(l) #creamos un vector de ceros
    i = 0 #Hacemos un barrido 
    while i < m:
       j = 0
       while j < n:#Les pasamos los pixeles de la 
       #imagen al vector de ceros
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h) #ploteamos el histograma sin procesar
    plt.show() #lo mostramos en pantalla
    im = Image.open(imagen1)  #Abrimos de nuevo la imagen 
    g = 0.4 #definimos la variable gamma
    i = 0 #aplicamos la funcion gamma utilizando la función
    #dada en el ejemplo asignando el valor de pixel
    #siguiendo esta formula
    while i < im.size[0]:
        j = 0
        while j < im.size[1]:
            valor = round(255*((im.getpixel((i,j))/255)**g))
            im.putpixel((i, j),(valor))
            j+=1
        i+=1
    im.show()  # Mostramos la imagen
    im.save("imagen1_gam.jpeg")  #salvamos la imagen
    Im = Image.open("imagen1_gam.jpeg")  #abrimos la imagen
    im = Im
    m = im.size[0]  #redefinimos las filas
    n = im.size[1]  #redefinimos las columnas  
    l = 256
    h = np.zeros(l)  #creamos un arreglo numpy de ceros 
    i = 0    #hacemos un barrido y le damos 
    #el valor pixel por pixel 
    # de la nueva imagen al arreglo de ceros
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h) #ploteamos el histograma
    plt.show()   #mostramos el histograma
    gam = np.zeros(l) #creamos un arreglo numpy de ceros 
    #y ploteamos la función exponencial utilizando 
    #la funcion grafica
    for i in range (0,l):
        gam[i] = round((l-1)*((i/(l-1))**g))
    grafica(gam,"Corrección Gamma")
    


def logar(imagen1): #Definimos la función y pedimos
    #la imagen a tratar
    Im = Image.open(imagen1) #Abrimos la imagen
    im = Im # Redefinimos la imagen
    im.show() #mostramos la imagen
    m = im.size[0] #redefinimos las filas 
    n = im.size[1] #redefinimos las columnas    
    l = 256
    h = np.zeros(l) #creamos un arreglo numpy de ceros
    i = 0 #Hacemos un barrido 
    while i < m:
       j = 0
       while j < n:
           #Les pasamos los pixeles de la imagen al vector de ceros 
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)  #ploteamos el histograma sin procesar
    plt.show()  #lo mostramos en pantalla
    im =  Image.open(imagen1) #Abrimos de nuevo la imagen 
    i = 0 
    while i < im.size[0]:
        j = 0
        while j < im.size[1]:#aplicamos la funcion logaritmica
 #asignando el valor dada la ecuación (usamos round para lograr un
 #mejor resultado al plotearla)
            valor = im.getpixel((i,j))
            valor = valor + 1
            valor =  int(round((255/mas.log10(256))*mas.log(valor, 10)))
            if valor >= 255:
                valor = 255
            im.putpixel((i, j),valor)
            j+=1
        i+=1
    im.show()  # Mostramos la imagen
    im.save("imagen1_log.jpeg") #salvamos la imagen
    ima = Image.open("imagen1_log.jpeg") #abrimos la imagen
    im = ima
    m = im.size[0]  #redefinimos las filas
    n = im.size[1]   #redefinimos las columnas    
    l = 256
    h = np.zeros(l) #creamos un arreglo numpy de ceros 
    i = 0
    while i < m:
       j = 0
       while j < n:#hacemos un barrido y le damos
#el valor pixel por pixel  de la nueva imagen al arreglo de ceros
    
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h) #ploteamos el histograma
    plt.show()   #mostramos el histograma
    loga = np.zeros(l)  #creamos un arreglo numpy de ceros y
#ploteamos función logaritmo utilizando la funcion grafica
    for i in range (0,l):
        loga[i] = round(((l-1)/mas.log(l))*mas.log(i+1))
    grafica(loga,"Corrección Logarítmica")


def seno(imagen1): #Definimos la función y pedimos
#la imagen a tratar
    Im = Image.open(imagen1) #Abrimos la imagen
    im = Im # Redefinimos la imagen
    im.show() #mostramos la imagen
    k = im.size[0]    #redefinimos las filas 
    n = im.size[1]  #redefinimos las columnas 
    l = 256
    h = np.zeros(l)   #creamos un vector de ceros
    i = 0 #Hacemos un barrido 
    while i < k:
       j = 0
       while j < n:#Les pasamos los pixeles 
#de la imagen al vector de ceros 
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h) #ploteamos el histograma sin procesar
    plt.show() #lo mostramos en pantalla
    im =  Image.open(imagen1) #Abrimos de nuevo la imagen
    r = (3.1416/2)*(1/255) #redefinimos una nueva variable
    i = 0 
    while i < im.size[0]:
        j = 0
        while j < im.size[1]: #aplicamos la funcion 
 #seno utilizando la math y redondeando el valor al final 
            valor = im.getpixel((i,j))
            valor =round(255*mas.sin(r*valor))
            im.putpixel((i, j),(valor))
            j+=1
        i+=1
    im.show()  # Mostramos la imagen
    im.save("imagen1_sen.jpeg") #salvamos la imagen
    ima = Image.open("imagen1_sen.jpeg") #abrimos la imagen
    im = ima
    m = im.size[0] #redefinimos las filas    
    n = im.size[1] #redefinimos las columnas   
    l = 256
    h = np.zeros(l) #creamos un arreglo numpy de ceros 
    i = 0
    #hacemos un barrido y le damos el valor pixel por pixel
    # de la nueva imagen al arreglo de ceros
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h) #ploteamos el histograma
    plt.show() #mostramos el histograma
    se = np.zeros(l)  #creamos un arreglo numpy de ceros 
#y ploteamos la función seno utilizando la funcion grafica
    for i in range (0,l):
        se[i] = round(((l-1)*mas.sin((i*mas.pi)/(2*(l-1)))))
    grafica(se,"Corrección seno")


def coseno(imagen1): #Definimos la función y pedimos
#la imagen a tratar
    Im = Image.open(imagen1) #Abrimos la imagen
    im = Im # Redefinimos la imagen
    im.show()  #mostramos la imagen
    m = im.size[0] #redefinimos las filas   
    n = im.size[1] #redefinimos las columnas 
    l = 256
    h = np.zeros(l)  #creamos un vector de ceros
    i = 0 #Hacemos un barrido
    while i < m:
       j = 0
       while j < n: #Les pasamos los pixeles de 
#la imagen al vector de ceros 
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)  #ploteamos el histograma sin procesar
    plt.show()  #lo mostramos en pantalla
    im = Image.open(imagen1) #Abrimos de nuevo la imagen 
    r = (3.1416/2)*(1/255) #redefinimos una nueva variable
    i = 0 
    while i < im.size[0]:
        j = 0
        while j < im.size[1]: #aplicamos la funcion 
# coseno, utilizando math, la función round y utilizando
# la formula dada
            valor = im.getpixel((i,j))
            valor= round(255*(1 - mas.cos(r*valor)))
            im.putpixel((i, j),(valor))
            j+=1
        i+=1
    im.show()  # Mostramos la imagen
    im.save("imagen1_cos.jpeg") #salvamos la imagen
    ima = Image.open("imagen1_cos.jpeg") #abrimos la imagen
    im = ima
    m = im.size[0]  #redefinimos las filas    
    n = im.size[1] #redefinimos las columnas   
    l = 256
    h = np.zeros(l) #creamos un arreglo numpy de ceros
    i = 0
    #hacemos un barrido y le damos el valor pixel por pixel
    # de la nueva imagen al arreglo de ceros
    while i < m:
       j = 0
       while j < n:
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)  #ploteamos el histograma
    plt.show()   #mostramos el histograma
    co = np.zeros(l)   #creamos un arreglo numpy de ceros 
#y ploteamos la función coseno utilizando la funcion grafica
    for i in range (0,l):
        co[i] = round((l-1)*(1-mas.cos((i*mas.pi)/(2*(l-1)))))
    grafica(co,"Corrección cosenoidal")
 



def exponencial(imagen1):#Definimos la función y pedimos
    #la imagen a tratar
    Im = Image.open(imagen1) #Abrimos la imagen
    im = Im # Redefinimos la imagen
    im.show() 
    m = im.size[0]  #redefinimos las filas 
    n = im.size[1]   #redefinimos las filas     
    l = 256
    h = np.zeros(l) #creamos un vector de ceros
    i = 0 #Hacemos un barrido 
    while i < m:
       j = 0
       while j < n:
    #Les pasamos los pixeles de la imagen al vector de ceros
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h) #ploteamos el histograma sin procesar
    plt.show() #lo mostramos en pantalla
    im =  Image.open(imagen1) #Abrimos de nuevo la imagen 
    g = (255)/(1-mas.exp(-1)) #redefinimos una nueva variable
    i = 0 
    while i < im.size[0]:
        j = 0
        while j < im.size[1]: #aplicamos la funcion
#exponencial utilizando round y math y asigando el valor final
#al arreglo de nuestra imagen incial
            valor = im.getpixel((i,j))
            u=(-1)*(valor/255)
            u=1-mas.exp(u)
            u=g*u
            valor = int(round(u))
            im.putpixel((i, j),(valor))
            j+=1
        i+=1
    im.show()#mostramos la imagen
    im.save("imagen1_exp.jpeg") #salvamos la imagen
    ima = Image.open("imagen1_exp.jpeg") #abrimos la imagen
    im = ima
    m = im.size[0]  #redefinimos las filas     
    n = im.size[1]    #redefinimos las columnas  
    l = 256
    h = np.zeros(l)  #creamos un arreglo numpy de ceros 
    i = 0 
    while i < m:
       j = 0
       while j < n:
    #hacemos un barrido y le damos el valor pixel por pixel
    # de la nueva imagen al arreglo de ceros
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)      #ploteamos el histograma
    plt.show() #mostramos el histograma
    ex = np.zeros(l)   #creamos un arreglo numpy de ceros
#y ploteamos la función exponencial utilizando la funcion grafica
    for i in range (0,l):
        ex[i] = round(((l-1)/(1-mas.exp(-1)))*(1-(mas.exp(-(i/(l-1))))))
    grafica(ex,"Corrección exponencial")
    

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
    
   
  
def umbral(im): #Definimos la función y pedimos
 #la imagen a tratar
    im = Image.open(im) #Abrimos la imagen
    im.show() #mostramos la imagen
    m = im.size[0] #redefinimos las filas         
    n = im.size[1] #redefinimos las columnas 
    t = 50 # metemos el umbral
    im2 = Image.new('1', (m, n), "white")  #creamos un
#una imagen de l mismo tamaño que la imagen incial  
    i = 0 #Hacemos un barrido 
    while i < m:
        j = 0
        while j < n:
            if (im.getpixel((i,j))) <= t:
 #si cumple que el valor del pixel incial es menor al umbral
 #asignamos un cero a la matriz creada y si no un 1
                im2.putpixel((i,j),0)
            else:
                im2.putpixel((i,j),1)
            j+=1
        i+=1
    im2.show() # Mostramos la imagen
    im2.save("imu.jpeg")  #salvamos la imagen
    ima = Image.open("imu.jpeg")#abrimos la imagen
    im = ima
    m = im.size[0]   #redefinimos las filas   
    n = im.size[1] #redefinimos las columnas     
    l = 256
    h = np.zeros(l) #creamos un arreglo numpy de ceros 
    i = 0
    while i < m:
       j = 0
       while j < n: 
 # hacemos un barrido y le damos el valor pixel por pixel 
 # de la nueva imagen al arreglo de ceros
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)     #ploteamos el histograma
    plt.show()  #mostramos el histograma



def umbralf(im): #Definimos la función y pedimos
#la imagen a tratar
    im = Image.open(im)  #Abrimos la imagen
    im.show() #mostramos la imagen
    imbra = im
    T = 90   # metemos el umbral
    i = 0 #hacemos un barrido 
    while i < imbra.size[0]:
        j = 0
        while j < imbra.size[1]:
 #si cumple que el valor absoluto del pixel inicial esigual al umbral
 #asignamos un cero a la matriz creada y si el mismo valor 
 #del pixel
            valor = imbra.getpixel((i, j))
            if  -T <= valor <= T:
                valor = 0
            else:
                valor = imbra.getpixel((i, j))
            imbra.putpixel((i, j),(valor))
            j+=1
        i+=1
    imbra.show() # Mostramos la imagen
    imbra.save("imf.jpeg") #Guardamos la imagen
    Im = Image.open("imf.jpeg") #Llamamos a la imagen  
    im = Im
    m = im.size[0]       #redefinimos las filas   
    n = im.size[1]       #redefinimos las columnas 
    l = 256
    h = np.zeros(l)   #creamos un arreglo numpy de ceros 
    i = 0
    while i < m:
       j = 0
       while j < n:
# hacemos un barrido y le damos el valor pixel por pixel
 # de la nueva imagen al arreglo de ceros
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)    #ploteamos el histograma
    plt.show()    #mostramos el histograma
    

def umbrals(im):
    #Definimos la función y pedimos
    #la imagen a tratar
    im = Image.open(im)  #Abrimos la imagen
    im.show() #mostramos la imagen
    imbra = im  # metemos el umbral
    T = 90 
    i = 0
     #Hacemos un barrido 
    while i < imbra.size[0]:
        j = 0
        while j < imbra.size[1]:
            valor = imbra.getpixel((i, j))
  #si cumple que el valor absoluto del pixel inicial es
 #menor  o igual al umbral  asignamos un cero a la matriz 
 # si es mayor a  t, el valor del pixe  es igual a 
 # el original menos t y, si es menor a -T, entonces 
#sumamos T al valor inicial del pixel
            if  -T <= valor <= T:
                valor = 0
            if   valor > T:
                valor =  imbra.getpixel((i, j)) - T
            if   valor < -T:
                valor =  imbra.getpixel((i, j)) + T
            imbra.putpixel((i, j),(valor))
            j+=1
        i+=1
    imbra.show()   # Mostramos la imagen
    imbra.save("imb.jpeg")  #salvamos la imagen
    ima = Image.open("imb.jpeg")  #abrimos la imagen
    im = ima
    m = im.size[0]     #redefinimos las filas   
    n = im.size[1]  #redefinimos las columnas    
    l = 256
    h = np.zeros(l) #creamos un arreglo numpy de ceros 
    i = 0
    while i < m:
       j = 0
       while j < n:
 # hacemos un barrido y le damos el valor pixel por pixel 
 # de la nueva imagen al arreglo de ceros
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)   #ploteamos el histograma
    plt.show()    #mostramos el histograma


def Histo(imagen1): #Definimos la función y pedimos
 #la imagen a tratar
    im = Image.open(imagen1) #Abrimos la imagen
    im.show() #mostramos la imagen
    m = im.size[0] #redefinimos las filas 
    n = im.size[1] #redefinimos las columnas    
    l = 256
    h = np.zeros(l) #creamos un arreglo numpy de ceros
    i = 0 #Hacemos un barrido 
    while i < m:
       j = 0
       while j < n:
           #Les pasamos los pixeles de la imagen al vector de ceros 
           h[im.getpixel((i, j))] = h[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    plt.plot(h)  #ploteamos el histograma sin procesar
    plt.show()  #lo mostramos en pantalla
    im = Image.open(imagen1)  #Abrimos la imagen
    m = im.size[0]   #redefinimos las filas       
    n = im.size[1]    #redefinimos las filas       
    h1 = np.zeros(256) #creamos dos arreglos numpy con limite de
    #256 pixeles 
    h2 = np.zeros(256)
    i = 0  #Hacemos un barrido 
    while i < m:
       j = 0
       while j < n:
           h1[im.getpixel((i, j))] = h1[im.getpixel((i, j))] + 1
           j+=1
       i+=1
    H = h1/(m*n) #normalizamos el histograma  
    p = np.zeros(256) #creamos otro arreglo de zeros
    for i in range(0,256,1):
       p[i]=p[i-1] + H[i] #obtenemos la probabilidad acumulada
    v = np.zeros(256) #creamos otro arreglo de ceros
    for i in range(0,256,1):
       v[i]=round((255)*p[i]) #redefinimos los nuevos niveles de
       #gris
    i = 0 #hacemos un barrido 
    while i < m:
        j = 0
        while j < n:
 #para cada valor del nuevo nivel de gris,se manda a la imagen
 #original
            valor = v[im.getpixel((i, j))]
            im.putpixel((i, j),(int(valor)))
            j+=1
        i+=1
    im.save("equaliz.jpg")  #salvamos l imagen 
    im.show() #mostramos la imagen 
    i = 0 #hacemos un barrido 
    while i < m:
       j = 0
       while j < n:
# hacemos un barrido y le damos el valor pixel por pixel 
 # de la nueva imagen al arreglo de ceros
            h2[im.getpixel((i, j))] = h2[im.getpixel((i, j))] + 1
            j+=1
       i+=1
    H2 = h2/(m*n) #normalizamos el histograma
    p2 = np.zeros(256)  #creamos un arreglo numpy de ceros  
#y asignamos su valor de acuerdo a la probabilidad acumulada 
    for i in range(0,256,1): 
        p2[i]=p2[i-1] + H2[i]
    plt.plot(p)  #ploteamos el histograma
    plt.show()    #mostramos el histograma
    
    
    

def constras(im): #Definimos la función y pedimos
 #la imagen a tratar
    im = Image.open(im) #Abrimos la imagen
    im.show()
    img = np.array(im)    #Obtenemos el arreglo de la imagen
    L = np.min(img)     #Obtenemos el Valor mínimo del rango
    M = np.max(img)     #Obtenemos el Valor máximo del rango
    g=(253)/(M-L) #redefinimos una nueva variable
    i = 0 #Hacemos un barrido 
    while i < im.size[0]:
        j = 0
        while j < im.size[1]:
 #si cumple que el valor del pixel incial es menor a M y mayor a
 #L aplicamos la función del contraste, si es mayor a M se manda 
 # a 255 y si es menor a L a 0
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
    im.show()#mostramos la imagen
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
    plt.show() #mostramos el histograma
    
    
def escale(im):
    im = Image.open(im) #Abrimos la imagen
    im.show()
    im2 = im
    i = 0
    while i < im2.size[0]:
        j = 0
        while j < im2.size[1]:
            r, g, b = im2.getpixel((i,j))
            g = (r + g + b) / 3
            gris = int(g)
            pixel = tuple([gris, gris, gris])
            im2.putpixel((i,j), pixel)
            j+=1
        i+=1
    im2.show()
    im2 = im.convert('L')
    im2.save("C:/Users/Acer/Pictures/nueva.jpg")


