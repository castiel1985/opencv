# -*- coding: utf-8 -*-

# @Time   : 2016/11/28 14:45

# @Author : Retacn

# @Site   : cameo实现,有两种启动方法: run() 和 onkeypress()

# @File   : cameo.py

# @Software: PyCharm


import cv2

import filters

from Managers import WindowManager, CaptureManager


class Cameo(object):

    def __init__(self):

        self._windowManager = WindowManager('Cameo', self.onkeypress)

        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)

    # self._curveFilter=filters.BGRPortraCurveFilter()

    def run(self):

        self._windowManager.createWindow()

        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()

            frame = self._captureManager.frame

            # filters.strokeEdges(frame,frame)

            # self._curveFilter.apply(frame,frame)

            self._captureManager.exitFrame()

            self._windowManager.processEvents()

    def onkeypress(self, keycode):

        '''

            space-> 载图

            tab->启动和停止视频录制

            esc->退出应用



        :param keycode:

        :return:

        '''

        if keycode == 32:  # space

            self._captureManager.writeImage('screenshot.png')

        elif keycode == 9:  # tab

            if not self._captureManager.isWritingVideo:

                self._captureManager.startWritingVideo('screencast.avi')

            else:

                self._captureManager.stopWritingVideo()

        elif keycode == 27:  # esc

            self._windowManager.destroyWindow()


if __name__ == '__main__':
    Cameo().run()