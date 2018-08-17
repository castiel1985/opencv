import cv2
import numpy as np
from matplotlib import pyplot as plt

img_truename = '1.jpg'
path = '/home/castiel/git/结构图/' + img_truename

class img():
    def totest(self):
        print("this is one test")

    def togray(self):
        img = cv2.imread(path, 0)
        plt.imshow(img, cmap='gray', interpolation='bicubic')
        plt.xticks([]), plt.yticks([])
        plt.show()
    def toshow(self):
        image = cv2.imread(path, cv2.IMREAD_COLOR)
        plt.imshow(image, cmap=None)
        plt.show()




