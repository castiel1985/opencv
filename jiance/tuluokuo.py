import cv2
import numpy as np

#读入图像
img=cv2.pyrDown(cv2.imread('../img/2.jpg'),cv2.IMREAD_UNCHANGED)
#修改颜色空间,设置阈值
ret,thresh=cv2.threshold(cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY),
                         127,
                         255,
                         cv2.THRESH_BINARY)
#更换颜色空间
black=cv2.cvtColor(np.zeros((img.shape[0],img.shape[1]),
                    dtype=np.uint8),
                   cv2.COLOR_GRAY2BGR)
#检测轮廓
image,contours,hier=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    #轮廓的周长
    epsilon=0.01*cv2.arcLength(cnt,True)
    approx=cv2.approxPolyDP(cnt,epsilon,True)
    hull=cv2.convexHull(cnt)

    cv2.drawContours(black,[cnt],-1,(0,255,0),2)#绿,精确的轮廓
    cv2.drawContours(black,[approx],-1,(255,255,0),2)#蓝色 近似多边形
    cv2.drawContours(black,[hull],-1,(0,0,255),2)#红

cv2.imshow('hull',black)
cv2.waitKey()
cv2.destroyAllWindows()