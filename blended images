import cv2
import numpy as np
import matplotlib.pyplot as plt

#hor=np.hstack((img,img1))
#ver=np.vstack((img,img1))
img1=cv2.imread("test1.png")
img=cv2.imread("test.png")
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
nimg1=cv2.resize(img1,(250,250))
nimg=cv2.resize(img,(250,250))
#çizgili=cv2.line(nimg1,(0,0),(250,250),(255,0,0),4)
#hor=np.hstack((img,img))
#ver=np.vstack((img,img))
#cv2.imshow("img",hor)

#karıştırma
blended=cv2.addWeighted(src1=nimg,alpha=4,src2=nimg1,beta=0.5,gamma=0)

