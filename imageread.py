import cv2
import  numpy as np

img = cv2.imread('img/1.jpg')
img[:, :, 1] = 0

print(img.shape)
print(img.size)
print(img.dtype)
cv2.imwrite('test1.jpg',img)
