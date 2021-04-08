import cv2
import numpy as np
from matplotlib import pyplot as plt
import speech_recognition as konus
from os import system as komut
import os
import random
from playsound import playsound
from gtts import gTTS 
def speak(string):
    tts=gTTS(string )
    rand =random.randint(1,10000)
    file='audio-'+str (rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)
r = konus.Recognizer()
with konus.Microphone() as source:
    
    audio = r.listen(source)



mouth=cv2.CascadeClassifier('nose.xml')
face=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#mouth=cv2.CascadeClassifier('Mouth.xml')
video=cv2.VideoCapture(0)

a=0
while True:
	_,kare=video.read()
	gray=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
	#Mouth=mouth.detectMultiScale(gray,1.1,4)

	faces=face.detectMultiScale(gray,1.1,4)
	mouth1=mouth.detectMultiScale(gray,1.1,4)
	
	
	for (x,y,w,h) in faces:
		cv2.rectangle(kare,(x,y), (x+w,y+h),(0,255,0),3)
		cv2.putText(kare,"person",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
		
		
	
			

	for(x,y,w,h) in mouth1:
		a=a+1
		b="put your mask up"	
		cv2.rectangle(kare,(x,y), (x+w,y+h),(0,255,0),3)
		cv2.putText(kare,b,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),2)
		if a==2:
			speak("close your nose")
			print("put it over your nose")
		for (x,y,w,h) in faces:
			cv2.rectangle(kare,(x,y), (x+w,y+h),(0,0,255),3)
			cv2.putText(kare,"__NO MASK",(x,y-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),3)
		
			#for (ex,ey,ew,eh) in Mouth:
				#cv2.rectangle(kare,(ex,ey), (ex+ew,ey+eh),(0,255,0),3)
				#cv2.putText(kare,"ağız açıkta",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),2)	


		








	#cv2.imshow("ben",kare)

	
	cv2.imshow("kare",kare)
	if cv2.waitKey(1) & 0xFF ==ord("k"):
		 break

video.release()
cv2.destroyAllWindows()		
