import cv2
import numpy as np
from matplotlib import  pyplot as plt



img = cv2.imread('img/123.jpeg',0)
i,k = img.shape
print(img.shape)


dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum =20*np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1]))


plt.subplot(121),plt.imshow(img, cmap='gray')
plt.title('INput Image'), plt.xticks([]), plt.yticks([])


plt.subplot(122),plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Image'), plt.xticks([]), plt.yticks([])

plt.show()

#傅立叶变换-OK