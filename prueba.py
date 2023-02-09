# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:53:54 2020

@author: ACER
"""


import pylab as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image


def image(imagen1):
    ima = Image.open(imagen1)
    ime = ima
    [ren, col] = ime.size
    total = ren * col
    a = np.asarray(ime, dtype = np.float32)
    a = a.reshape(1, total)
    a = a.astype(int)
    c = max(a)
    b = min(a)
    im = Image.open(imagen1)
    i = 0 
    while i < im.size[0]:
        j = 0
        while j < im.size[1]:
            valor = (253*(im.getpixel((i,j)))/(c - b) - b) + 1
            im.putpixel((i, j),(valor))
            j+=1
        i+=1
    im.show()

    