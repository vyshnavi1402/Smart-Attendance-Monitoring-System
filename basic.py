import cv2
import numpy as np
import face_recognition
#convert image from bgr to rgb
imgElon=face_recognition.load_image_file("C:\\Users\\vyshg\\Downloads\\attendance system\\photos\\Vyshnavi.jpg")
imgElon=cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest=face_recognition.load_image_file("C:\\Users\\vyshg\\Downloads\\attendance system\\photos\\Vyshnavi Test.jpg")
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

#Finding faces and finding encodings
facLoc=face_recognition.face_locations(imgElon)[0]
encodeElon=face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(facLoc[3],facLoc[0]),(facLoc[1],facLoc[2]),(255,0,255),2)

facLocTest=face_recognition.face_locations(imgTest)[0]
encodeTest=face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(facLocTest[3],facLocTest[0]),(facLocTest[1],facLocTest[2]),(255,0,255),2)

#comparing the faces and  finding the distance
results=face_recognition.compare_faces([encodeElon],encodeTest)
faceDis=face_recognition.face_distance([encodeElon],encodeTest)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
print(results,faceDis)

cv2.imshow('Vyshnavi',imgElon)
cv2.imshow('Vyshnavi Test',imgTest)
cv2.waitKey(0)
