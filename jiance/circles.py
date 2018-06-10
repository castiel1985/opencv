import cv2
import numpy as np

#读入图像
img=cv2.imread('../img/2.jpg')
#更换颜色空间
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#中值边滤
imgMb=cv2.medianBlur(gray,5)

#圆检测
circles=cv2.HoughCircles(imgMb,
                         cv2.HOUGH_GRADIENT,
                         1,
                         120,
                         param1=100,
                         param2=30,
                         minRadius=0,
                         maxRadius=0)
circles=np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imwrite('../houghCircles.jpg',img)
cv2.imshow('../houghCircles.jpg',img)
cv2.waitKey()
cv2.destroyAllWindows()