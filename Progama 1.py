# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:31:44 2020

@author: ACER
"""
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PIL.ImageChops import add, subtract, multiply, difference, screen
import PIL.ImageStat as stat
from numpy import array
from skimage.io import imread, imsave, imshow, show, imread_collection,imshow_collection
from skimage import color, viewer, exposure, img_as_float, data
from skimage.transform import SimilarityTransform, warp, swirl
from skimage.util import invert, random_noise, montage
import matplotlib.image as mpimg
import matplotlib.image as img
import matplotlib.pylab as plt
from scipy.ndimage import affine_transform, zoom
from scipy import misc
from scipy import misc

im = imread("C:/Users/Acer/Pictures/imagen1.jpg")
im = Image.open("C:/Users/Acer/Pictures/imagen1.jpg") 
print(im.width, im.height, im.mode, im.format, type(im))
image = img.imread("C:/Users/Acer/Pictures/imagen1.jpg")
im.show()
image_sequence = im.getdata()
image_array = np.array(image_sequence)
print(image_array)
dato_pixel=im.getpixel((200,250)) 
print(f"pixel={dato_pixel}")
im_g = im.convert('L') 
im_g.save('C:/Users/Acer/Pictures/imagen1.jpg') 
plt.figure(figsize=(20,30))
plt.imshow(im) 
plt.axis('off')
plt.show()
im.load
Image.open("C:/Users/Acer/Pictures/imagen1.jpg").show() 
