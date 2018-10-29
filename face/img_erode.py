import numpy as np
import cv2


img = cv2.imread('img/456.jpeg')

kernel = np.ones((5,5),np.uint8)

erossion = cv2.erode(img,kernel,iterations = 1)  #腐蚀

dilation = cv2.dilate(img,kernel,iterations = 1)   #膨胀

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
while(1):

    cv2.imshow('img',img)
    cv2.imshow('erode',erossion)
    #cv2.imshow('dilation',dilation)

    #cv2.imshow('gradient',gradient)
    cv2.imshow('tophat', tophat)
    if cv2.waitKey(1)&0XFF==27:
        break

cv2.destroyAllWindows()
#print(kernel)
