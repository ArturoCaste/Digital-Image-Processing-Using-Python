# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 22:05:40 2020

@author: ACER
"""
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def negativo(imagen1):
    Im = Image.open(imagen1)
    im = Im
    im = im.convert('L') 
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
    plt.imshow(np.asarray(im),cmap='gray') 

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
    plt.imshow(np.asarray(imesc),cmap='gray') 
