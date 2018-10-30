import cv2
import numpy as np
from matplotlib import  pyplot as plt

img = cv2.imread('img/hist.jpeg', 0)
equ = cv2.equalizeHist(img)   #cv2.equalizeHist()只提供灰度值图片的处理，当把上面的图片换成RGB
res = np.hstack((img, equ))  #在水平方向平铺

img2 =cv2.imread('img/hist2.jpeg',0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img2)

#test = cv2.imread('img/789.jpeg')
#print(test.shape)
#img_gray = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)


plt.imshow(cl1)
#plt.imshow(img)
plt.show()

#直方图均衡化
