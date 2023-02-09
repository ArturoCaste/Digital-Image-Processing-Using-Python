# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:56:56 2020

@author: ACER
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt



foto=Image.open("C:/Users/Acer/Pictures/Pruebas/negat.png")


umbral=65

datos=foto.getdata()
datos_binarios=[]

for x in datos:
    if x< umbral:
        datos_binarios.append(0)
        continue
    datos_binarios.append(1)
nueva_imagen=Image.new("L",[50,50], 0)
nueva_imagen.putdata(datos_binarios)


    
        
        
        

    

