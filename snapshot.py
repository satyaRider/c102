import cv2

def take_snapshot():
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        print(ret)
        cv2.imwrite("NewPicture1.jpg",frame)
        result=False
        videoCaptureObject.release()
        cv2.destroyAllwindows()


take_snapshot()