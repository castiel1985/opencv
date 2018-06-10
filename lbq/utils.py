# -*- coding: utf-8 -*-

import cv2
import numpy
import scipy.interpolate

#边缘检测函数
def Laplacian(src,
            ddepth,
            dst=None,
            ksize=None,
            scale=None,
            delta=None,
            borderType=None)


def Sobel(src,
            ddepth,
            dx,
            dy,
            dst=None,
            ksize=None,
            scale=None,
            delta=None,
            borderType=None)

def Scharr(src,
            ddepth,
            dx,
            dy,
            dst=None,
            scale=None,
            delta=None,
            borderType=None)

#模糊滤波函数
def blur(src,  # 源图像
            ksize,  # 内核大小
            dst=None,  # 输出图像
            anchor=None,  # 中心锚点
            borderType=None)  # 边界模式
#高斯模糊函数
def GaussianBlur(src,  # 输入图像
            ksize,  # 高斯滤波模版大小
            sigmaX,  # 横向滤波系数
            dst=None,  # 输出图像
            sigmaY=None,  # 纵向滤波系数
            borderType=None)

#中值模糊函数
def medianBlur(src,  # 源图像
            ksize,  # 中值滤波器的模版的大小
            dst=None)  # 输出图像


#双边滤波
def bilateralFilter(src,  # 输入图像
            d,  # 每个像素邻域的直径
            sigmaColor,  # 颜色空间的标准偏差
            sigmaSpace,  # 坐标空间的标准偏差
            dst=None,  # 输出图像
            borderType=None)  # 边缘点插值类型