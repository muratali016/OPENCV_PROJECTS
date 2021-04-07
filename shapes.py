import cv2
import numpy as np 
img=np.zeros((512,512,3),np.uint8)
cv2.imshow("img",img)

cv2.line(img,(0,0),(300,300),(0,255,0),4)
cv2.imshow("img",img)

cv2.rectangle(img,(0,0),(250,250),(255,0,0),cv2.FILLED)
cv2.imshow("img",img)

cv2.circle(img,(400,400),70,(200,225,154),cv2.FILLED)
cv2.imshow("img",img)

cv2.putText(img,"Merhaba",(200,200),
	cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255))
cv2.imshow("img",img)

cv2.waitKey(0)
