import cv2
import numpy as np
from matplotlib import  pyplot as plt

img = cv2.imread('img/789.jpeg',0)
edges = cv2.Canny(img, 200, 200)

plt.subplot(131),plt.imshow(img, cmap='gray')
plt.title('Original Image'),plt.xticks([]),plt.yticks([])

plt.subplot(132),plt.imshow(edges, cmap='gray')
plt.title('Original Image'),plt.xticks([]),plt.yticks([])

plt.subplot(133),plt.imshow(edges, cmap='gray')
plt.title('Original Image'),plt.xticks([]),plt.yticks([])


plt.show()