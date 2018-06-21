import numpy as np
import cv2
from matplotlib import pyplot as plt

# 读取图像
img = cv2.imread('img/1.jpg',0)
plt.imshow(img)
plt.show()
