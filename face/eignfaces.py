import cv2
import numpy as np
import sys
import os.path


# 生成人脸识别数据
def generate():
    face_cascade = cv2.CascadeClassifier('data/cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('data/cascades/haarcascade_eye.xml')

    # 读取摄像头视频数据
    camera = cv2.VideoCapture(0)
    count = 0
    while (True):
        ret, frame = camera.read()
        # 更换颜色空间
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            f = cv2.resize(gray[y:y + h, x:x + w], (200, 200))
            cv2.imwrite('data/retacn/%s.pgm' % str(count), f)
            count += 1
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1000 / 12) & 0xFF == ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()


# 加载识别数据
def read_image(path, sz=(200, 200)):
    c = 0
    x, y = [], []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                try:
                    if (filename == '.directory'):
                        continue
                    filepath = os.path.join(subject_path, filename)
                    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
                    if (sz is not None):
                        img = cv2.resize(img, (200, 200))
                    x.append(np.asarray(img, dtype=np.uint8))
                    y.append(c)
                except IOError as ioe:
                    print(ioe)
                except:
                    print('Unexpected error:', sys.exc_info()[0])
                    raise
            c += 1
    return [x, y]


# 基于三种模型的人脸识别
def face_rec():
    names = ['Yue', 'Retacn', 'Three']
    # 需要输入样本数据的存放路径
    if len(sys.argv) < 2:
        print('USAGE: facerec_defo.py </path/to/images> [/path/to/store/images/at]')
        sys.exit()
    # 读入图像数组,第二个参数为样本图像的存放位置
    [x, y] = read_image(sys.argv[1])
    y = np.asarray(y, dtype=np.int32)
    # [x, y] = read_image('D:/workspace_pycharm/opencv3_python/data/at')


    # 如果有三个参数,则将第三个参数设为输出目录
    if len(sys.argv) == 3:
        out_dir = sys.argv[2]

    # 创建人脸识别模型
    # model = cv2.face.createEigenFaceRecognizer()
    # 基于Fisherfaces的人脸识别
    # model = cv2.face.createFisherFaceRecognizer()
    # 基于lbph的人脸识别
    model = cv2.face.createLBPHFaceRecognizer()
    model.train(np.asarray(x), np.asarray(y))
    camera = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('data/cascades/haarcascade_frontalface_default.xml')

    while (True):
        read, img = camera.read()
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            roi = gray[x:x + w, y:y + h]
            try:
                roi = cv2.resize(roi, (200, 200), interpolation=cv2.INTER_LINEAR)
                # roi = cv2.resize(gray, (200, 200), interpolation=cv2.INTER_LINEAR)

                # 置信度评分
                params = model.predict(roi)
                print(params)
                print('Lable:%s,Confidence:%02f' % (params[0], params[1]))
                cv2.putText(img, names[params[0]], (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
            except:
                continue
        cv2.imshow("camera", img)
        if cv2.waitKey(33) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # generate()
    # [X, y] = read_image('D:/workspace_pycharm/opencv3_python/data/at')
    face_rec()
    # generate()