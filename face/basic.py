import cv2

filename='../结构图/1.jpg'

def detect(filename):
    #用于人脸检测xml
    face_cascade=cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

    #读入图像
    img=cv2.imread(filename)
    #更换颜色空间
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,
                                        1.3,#图像的压缩率
                                        5)#人脸矩形保留邻近数目的最小值
    #在原始图像上绘制蓝色矩形
    for (x,y,w,h) in faces:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.namedWindow('Vikings Detected!!')
    cv2.imshow("Vikings Detected!!",img)
    cv2.imwrite('../vikings.jpg',img)
    cv2.waitKey(0)

if __name__=='__main__':
    detect(filename)