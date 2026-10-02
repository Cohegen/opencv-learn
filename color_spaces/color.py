import os
import cv2 

img = cv2.imread("Fish/fish3.jpg")
img_resize = cv2.resize(img,(640,480))

img_rgb = cv2.cvtColor(img_resize,cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img_resize,cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img_resize,cv2.COLOR_BGR2HSV)
cv2.imshow('image',img_resize)
cv2.imshow('image',img_rgb)
cv2.imshow('image',img_gray)
cv2.imshow('image',img_hsv)
cv2.waitKey(0)
