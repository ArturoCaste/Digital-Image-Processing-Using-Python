# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 19:08:18 2020

@author: ACER
"""
from skimage import io
from PIL import Image
from skimage import io

def abrir_imagen(im):
    ruta = ("C:/Users/Acer/Pictures/" + im)
    im = Image.open(ruta)
    im.show()
    print("- Dimensiones de la imagen:")
    print(Image.shape)
    
    