import numpy as np
import cv2
import math as ma
import matplotlib.pyplot as plt
from PIL import Image


img1=cv2.imread("C:/Users/ACER/Pictures/Pruebas/negat.png",0)

fuv=np.fft.fft2(img1)
fuv=np.fft.fftshift(fuv)
fuv_abs=np.abs(fuv)
fuv_log=20*np.log10(fuv_abs)
cv2.imshow("Original", img1)
cv2.imshow("Espectro de fourier", np.uint8(255*fuv_log/np.max(fuv_log)))

M=img1.shape[0]
N=img1.shape[1]
Do=np.zeros(2)
Do[0]=round(0.5*M)
Do[1]=round(0.5*N)
print(Do)
Dc=10
Huv=np.array(img1)
for k in range(M):
    for m in range(N):
        Huv[k,m]=0
for k in range(M):
    for m in range(N):
        d=ma.sqrt(((m-Do[0])**2)+((k-Do[1])**2))
        Huv[k,m]=255*ma.exp(-(d**2)/(2*Dc**2))


cv2.imshow("Pb", np.uint8(Huv))
Guv=(1/255)*Huv*fuv
Guv_abs=np.abs(Guv)
Guv_abs=np.uint8(255*Guv_abs/np.max(Guv_abs))
cv2.imshow("espectro G", Guv_abs)
gxy=np.fft.ifft2(Guv)
gxy=np.abs(gxy)
gxy=np.uint8(gxy)
cv2.imwrite("FiltradaGaussianPB.png", gxy)

cv2.waitKey(0)
cv2.destroyAllWindows()
