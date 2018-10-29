import cv2
import numpy as np

img= cv2.imread('img/147.jpeg')

#res = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

height,width = img.shape[:2]

res = cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)

while(1):
    cv2.imshow('img',img)
    cv2.imshow('res',res)

    if cv2.waitKey(1)&0XFF==27:
        break

cv2.destroyAllWindows()