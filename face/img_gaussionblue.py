import cv2
from matplotlib import pyplot as plt


img = cv2.imread('img/147.jpeg')

blur = cv2.GaussianBlur(img,(5,5),0)

#print(blur)

plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
#plt.xticks([]), plt.yticks([])
plt.show()