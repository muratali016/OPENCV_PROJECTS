import cv2
import numpy as np
import matplotlib.pyplot as plt


img1=cv2.imread("test1.png")
img=cv2.imread("test.png")
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img1,cmap="gray")
plt.axis("off")
plt.show()


_,eşikimg=cv2.threshold(img1,thresh=60,maxval=255,type=cv2.THRESH_BINARY)
#BINARY_INV dersen tam tersi olur
plt.figure()
plt.imshow(eşikimg,cmap="gray")
plt.axis("off")
plt.show()

#adaptive yöntemi ile nesneler daha belirgin ayrışıyor !!!!
threshold2=cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)

plt.figure()
plt.imshow(threshold2,cmap="gray")
plt.axis("off")
