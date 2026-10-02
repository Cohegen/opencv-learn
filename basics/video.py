#import library
import cv2
import os

#read video
video_path = os.path.join('.','videos','nature.mp4')

video = cv2.VideoCapture(video_path)

#visualize
ret = True 
while ret:
    ret,frame = video.read()
    if ret:
        cv2.imshow('frame',frame)
        cv2.waitKey(40)

video.release()
video.de