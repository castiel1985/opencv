#图像金字塔

import cv2
import numpy as np
from matplotlib import  pyplot as plt

img = cv2.imread('img/123.jpeg',0)
img_up = cv2.pyrUp(img)

img_down = cv2.pyrDown(img)

plt.subplot(131),plt.imshow(img)
plt.title('Original Image'),plt.xticks([]),plt.yticks([])

plt.subplot(132),plt.imshow(img_up)
plt.title('up Image'),plt.xticks([]),plt.yticks([])

plt.subplot(133),plt.imshow(img_down)
plt.title('down Image'),plt.xticks([]),plt.yticks([])

plt.show()