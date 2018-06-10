import cv2

#
cameraCapture=cv2.VideoCapture(0)
FPS=30
size=(int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
      ,int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWrite=cv2.VideoWriter('../test.avi',cv2.VideoWriter_fourcc('I','4','2','0'),FPS,size)

success,frame=cameraCapture.read()
numFramesRemaining=10*FPS-1
while success and numFramesRemaining>0:
    videoWrite.write(frame)
    success,frame=cameraCapture.read()
    numFramesRemaining-=1
cameraCapture.release()