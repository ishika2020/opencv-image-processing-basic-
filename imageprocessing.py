#creating 1st image using rectangle
import numpy
import cv2

img1 = numpy.ones((600,600,3),numpy.uint8)
cv2.rectangle(img1, (1,0), (150,150), (150,255,0), -1)
cv2.rectangle(img1, (150,150), (300,300), (150,255,0), -1)
cv2.rectangle(img1, (300,300), (450,450), (150,255,0), -1)
cv2.rectangle(img1, (450,450),(600,600), (150,255,0), -1)
temp = numpy.ones((600,600,3),numpy.uint8)*1

#showing image
cv2.imshow('image1',img1)
cv2.waitKey(700)
cv2.destroyAllWindows()

import numpy
import cv2

#creating 2nd image using rectangle
img2 = numpy.ones((600,600,3), numpy.uint8)*255

cv2.rectangle(img2, (600,0), (450,150), (150,255,0), -1)
cv2.rectangle(img2, (450,150), (300,300), (150,255,0), -1)
cv2.rectangle(img2, (300,300), (150,450), (150,255,0), -1)
cv2.rectangle(img2, (150,450),(0,600), (150,255,0), -1)
  
#showing image
cv2.imshow('image2',img2)
cv2.waitKey(600)
cv2.destroyAllWindows()

for i in range(150, 450):
    for j in range(150, 450):
        temp[i, j] = img2[i, j]
        img2[i, j] = img1[i, j]
        img1[i, j] = temp[i, j]

#showing swapped image 1        
cv2.imshow('image1: swapped',img1)
cv2.waitKey(600)
cv2.destroyAllWindows()        
        
#showing swapped image 2  
cv2.imshow('image2: swapped',img2)
cv2.waitKey(600)
cv2.destroyAllWindows()

#appending both swapped image
image = numpy.append(img1, img2, axis=1 )
cv2.imshow('finalimage',image)
cv2.waitKey(600)
cv2.destroyAllWindows()
