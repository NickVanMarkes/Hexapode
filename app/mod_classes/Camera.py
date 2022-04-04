#Camera.py

# import the necessary packages
import cv2
ds_factor=0.5
class VideoCamera(object):
    def __init__(self):
       # capturing video
       self.video = cv2.VideoCapture(cv2.CAP_V4L2)
    
    def __del__(self):
        # releasing camera
        self.video.release()
    def get_frame(self):
       # extracting frames
        ret, frame = self.video.read()
        #frame=cv2.resize(frame,(1280,720))                    
        # encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()