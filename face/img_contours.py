import cv2
import numpy as np
from matplotlib import  pyplot as plt


img = cv2.imread('img/369.jpeg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



x = cv2.drawContours(img, contours, -1, (0,255,0),3)


cnt=contours[0]
M=cv2.moments(cnt)
print(cv2.contourArea(cnt))
perimeter=cv2.arcLength(cnt, True)
print(perimeter)

k = cv2.isContourConvex(cnt)
print(k)




#plt.imshow(x)
#plt.show()






print('********************')



mask=np.zeros(img_gray.shape,np.uint8)

#print(mask)
m = cv2.drawContours(mask, [cnt],0,255,-1)
x,y,w,h =cv2.boundingRect(cnt)
p = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
plt.imshow(p)
plt.show()