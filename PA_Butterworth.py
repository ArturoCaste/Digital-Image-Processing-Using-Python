import numpy as np
import cv2
import math as ma
img1=cv2.imread("C:/Users/ACER/Pictures/Pruebas/negat.png",0)

fuv=np.fft.fft2(img1)
fuv=np.fft.fftshift(fuv)
M=img1.shape[0]
N=img1.shape[1]
Do=np.zeros(2)
Do[0]=round(0.5*M)
Do[1]=round(0.5*N)
print(Do)
Dc=50
n=3
Huv=np.array(img1)
for k in range(M):
    for m in range(N):
        Huv[k,m]=0
for k in range(M):
    for m in range(N):
        d=ma.sqrt(((m-Do[0])**2)+((k-Do[1])**2))
        Huv[k,m]=255-(255/(1+(d/Dc)**(2*n)))


cv2.imshow("Pb", np.uint8(Huv))
Guv=(1/255)*Huv*fuv
Guv=np.fft.fftshift(Guv)
gxy=np.fft.ifft2(Guv)
gxy=gxy.real
Ip_min=(np.amin(np.amin(gxy)))
Ip_max=(np.amax(np.amax(gxy)))
gxy=255*(gxy-Ip_min)/(Ip_max-Ip_min)


gxy=np.uint8(gxy)
cv2.imshow("Truncada",gxy)
cv2.imwrite("FiltradaButterPA.png", gxy)
cv2.waitKey(0)
cv2.destroyAllWindows()
