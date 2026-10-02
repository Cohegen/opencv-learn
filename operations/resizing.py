import os
import cv2 

img = cv2.imread("Fish/fish2.jpg")

img_resized = cv2.resize(img,(640,480))
print(img.shape)
print(img_resized.shape)


cv2.imshow('img',img)
cv2.imshow('Resized image',img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
