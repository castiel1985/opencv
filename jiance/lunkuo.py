import cv2
import numpy as np

img=np.zeros((200,200,),dtype=np.uint8)
#将指定的区域设为白色
img[50:150,50:150]=255
#设定阈值
ret,thresh=cv2.threshold(img,127,255,0)
#查找轮廓
image,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#更换颜色空间
color=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
img=cv2.drawContours(color,contours,-1,(0,255,0),2)
cv2.imshow('contours',color)
cv2.waitKey()
cv2.destroyAllWindows()