import cv2
import numpy as np
from matplotlib import pyplot as plt

class img():
    def totest(self):
        print("this is one test")

    def togray(self):
        img = cv2.imread('test.jpg', 0)
        plt.imshow(img, cmap='gray', interpolation='bicubic')
        plt.xticks([]), plt.yticks([])
        plt.show()




