# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 16:24:51 2020

@author: Joana
"""

from PIL import Image
import time


"""SUMA DE GRISES EN LA IMAGEN A GRISES"""
def suma(im,alpha):
    im = Image.open(im)
    im.show()
    im11 = im
    i = 0
    while i < im11.size[0]:
        j = 0
        while j < im11.size[1]:
            valor = im11.getpixel((i, j))
            valor = valor + alpha 
            if valor >= 255:
                valor = 255
            im11.putpixel((i, j),(valor))
            j+=1
        i+=1
    im11.show()


"""SUMA DE 2 GRISES"""
def suma2(ima1,ima2):
    im1 = Image.open(ima1)
    im1.show()
    im2 = Image.open(ima2)
    im2.show()
    im11 = im1
    im22 = im2
    i = 0
    while i < im11.size[0]:
        j = 0
        while j < im11.size[1]:
            valor1 = im11.getpixel((i,j))
            valor2 = im22.getpixel((i,j))
            valor1 = valor1 + valor2
            if valor1 >= 255:
                valor1 = 255
            im11.putpixel((i, j),(valor1))
            j+=1
        i+=1
    im11.show()

"""RESTA DE GRISES EN LA IMAGEN A GRISES"""
def resta(im,alpha):
    im = Image.open(im)
    im.show()
    im11 = im
    i = 0
    while i < im11.size[0]:
        j = 0
        while j < im11.size[1]:
            valor = im11.getpixel((i, j))
            valor = valor - alpha
            if valor < 0:
                valor = 0
            im11.putpixel((i, j),(valor))
            j+=1
        i+=1
    im11.show()
    
    
"""RESTA DE 2 GRISES"""
def resta2(ima1,ima2):
    im1 = Image.open(ima1)
    im1.show()
    im2 = Image.open(ima2)
    im2.show()
    im11 = im1
    im22 = im2
    i = 0
    while i < im11.size[0]:
        j = 0
        while j < im11.size[1]:
            valor1 = im11.getpixel((i,j))
            valor2 = im22.getpixel((i,j))
            valor1 = valor1 - valor2
            if valor1 < 0:
                valor1 = 0
            im11.putpixel((i, j),(valor1))
            j+=1
        i+=1
    im11.show()
    

"""MUTIPLICACIÓN DE GRISES EN LA IMAGEN A GRISES"""
def mul(im,alpha):
    im = Image.open(im)
    im.show()
    im11 = im
    i = 0
    while i < im11.size[0]:
        j = 0
        while j < im11.size[1]:
            valor = im11.getpixel((i, j))
            valor = valor * alpha
            if valor > 255:
                valor = 255
            im11.putpixel((i, j),(valor))
            j+=1
        i+=1
    im11.show()
    

"""MULTIPLICACIÓN DE 2 GRISES"""
def mul2(ima1,ima2):
    im1 = Image.open(ima1)
    im1.show()
    im2 = Image.open(ima2)
    im2.show()
    im11 = im1
    im22 = im2
    i = 0
    while i < im11.size[0]:
        j = 0
        while j < im11.size[1]:
            valor1 = im11.getpixel((i,j))
            valor2 = im22.getpixel((i,j))
            valor1 = valor1 * valor2
            if valor1 >= 255:
                valor1 = 255
            im11.putpixel((i, j),(valor1))
            j+=1
        i+=1
    im11.show()


"""DIVISIÓN DE GRISES EN LA IMAGEN A GRISES"""
def div(im,alpha):
    im = Image.open(im)
    im.show()
    im11 = im
    i = 0
    while i < im11.size[0]:
        j = 0
        while j < im11.size[1]:
            valor = im11.getpixel((i, j))
            valor = round(valor / alpha)
            if valor < 0:
                valor = 0
            im11.putpixel((i, j),(valor))
            j+=1
        i+=1
    im11.show()
    
    
"""DIVISIÓN DE 2 GRISES"""
def div2(ima1,ima2):
    im1 = Image.open(ima1)
    im1.show()
    im2 = Image.open(ima2)
    im2.show()
    im11 = im1
    im22 = im2
    i = 0
    while i < im11.size[0]:
        j = 0
        while j < im11.size[1]:
            valor1 = im11.getpixel((i,j))
            valor2 = im22.getpixel((i,j))
            if valor2 == 0:
                valor2 = 1
            valor1 = round(valor1 / valor2)
            if valor1 < 0:
                valor1 = 0
            im11.putpixel((i, j),(valor1))
            j+=1
        i+=1
    im11.show()