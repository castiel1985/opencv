# -*- coding: utf-8 -*-


import cv2


def detect():
    # 加载haar级联文件
    face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
    camera = cv2.VideoCapture(1)

    # 捕获视频帧
    while (True):
        ret, frame = camera.read()
        # 转换颜色空间
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            # 绘制检测到的人脸矩形
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # roi_gray = gray[y:y + h, x:x + w]

            # 检测眼睛
            # eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, 0, (40, 40))
            eyes = eye_cascade.detectMultiScale(img, 1.03, 5, 0, (40, 40))

            # 绘制检测到的眼睛矩形
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            # print(x,y,w,h,ex,ey,ew,eh)
        # 显示图像
        cv2.imshow('Camers', frame)
        # 按q键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    detect()