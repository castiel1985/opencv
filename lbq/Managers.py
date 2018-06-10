# -*- coding: utf-8 -*-
# @Time    : 2016/11/28 13:30
# @Author  : Retacn
# @Site    : 面向对象的设计
# @File    : cameo.py
# @Software: PyCharm

import cv2
import numpy as np
import time


'''
    视频管理
'''
class CaptureManager(object):
    def __init__(self,
                 capture, #摄像头通道
                 previewWindowManager=None,#窗口管理器
                 shouldMirrorPreview=False):#摄像头预览的镜像选项

        self.previewWindowManager=previewWindowManager
        self.shouldMirrorPreview=shouldMirrorPreview

        #定义非公有变量,单下划线开始,为保护变量,只有类对象或子类对象可以访问 protected
        #如果以双下划线开始,为私有成员变量,只有类对象自已可以访问,像private
        self._capture=capture
        self._channel=0
        self._enteredFrame=False
        self._frame=None
        self._imageFilename=None
        self._videoFilename=None
        self._videoEncoding=None
        self._videoWriter=None

        self.startTime=None
        self._framesElapsed=int(0)
        self._fpsEstimate=None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self,value):
        if self._channel!=value:
            self._channel=value
            self._frame=None

    @property
    def frame(self):
        if self._enteredFrame and self._frame is None:
            _,self._frame=self._capture.retrieve()
        return self._frame

    @property
    def isWritingImage(self):
        return self._imageFilename is not None

    @property
    def isWritingVideo(self):
        return self._videoFilename is not None


    #只能同步一帧
    def enterFrame(self):

        assert not self._enteredFrame, \
            'previous enterFrame() had no matching exitFrame()'

        if self._capture is not None:
            self._enteredFrame=self._capture.grab()

    #可以从当前通道中取得图像,估计帧率,显示图像,执行暂停的请求,向文件中写入图像
    def exitFrame(self):
        if self.frame is None:
            self._enteredFrame=False
            return

        #计算帧率
        if self._framesElapsed==0:
            self._startTime=time.time()
        else:
            timeElapsed=time.time()-self._startTime
            self._fpsEstimate=self._framesElapsed/timeElapsed

        self._framesElapsed+=1

        #通过窗体显示图像
        if self.previewWindowManager is not None:
            if self.shouldMirrorPreview:
                mirroredFrame=np.fliplr(self._frame).copy()
                self.previewWindowManager.show(mirroredFrame)
            else:
                self.previewWindowManager.show(self._frame)

        #保存图像文件
        if self.isWritingImage:
            cv2.imwrite(self._imageFilename,self._frame)
            self._imageFilename=None

        #保存视频文件
        self._writeVideoFrame()

        #释放资源
        self._frame=None
        self._enteredFrame=False

    #保存图片,公有函数
    def writeImage(self,filename):
        self._imageFilename=filename

    #开始保存视频,公有函数
    def startWritingVideo(self,filename,encoding=cv2.VideoWriter_fourcc('I','4','2','0')):
        self._videoFilename=filename
        self._videoEncoding=encoding

    #停止视频写入,公有函数
    def stopWritingVideo(self):
        self._videoFilename=None
        self._videoEncoding=None
        self._videoWriter=None

    #写入视频帧
    def _writeVideoFrame(self):
        if not self.isWritingVideo:
            return

        if self._videoWriter is None:
            fps=self._capture.get(cv2.CAP_PROP_FPS)
            if fps==0.0:
                if self._framesElapsed<20:
                    return
                else:
                    fps=self._fpsEstimate
            size=(int(self._capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                  int(self._capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

            self._videoWriter=cv2.VideoWriter(self._videoFilename,
                                              self._videoEncoding,
                                              fps,
                                              size)
        self._videoWriter.write(self._frame)

'''
    窗口管理,支持键盘事件
'''
class WindowManager(object):

    def __init__(self,
                 windowName,#窗体名称
                 keypressCallback=None):#按键回调函数
        self.keypressCallback=keypressCallback

        self._windowName=windowName
        self._isWindowCreate=False

    #检查窗体是否被创建
    @property
    def isWindowCreated(self):
        return self._isWindowCreate

    #创建窗体
    def createWindow(self):
        cv2.namedWindow(self._windowName)
        self._isWindowCreate=True

    #显示图像
    def show(self,frame):
        cv2.imshow(self._windowName,frame)

    #关闭窗体释放资源
    def destroyWindow(self):
        cv2.destroyWindow(self._windowName)
        self._isWindowCreate=False

    #处理键盘事件
    def processEvents(self):
        keycode=cv2.waitKey(1)
        if self.keypressCallback is not None and keycode!=-1:
            keycode&=0xFF #ESC 退出
            self.keypressCallback(keycode)
