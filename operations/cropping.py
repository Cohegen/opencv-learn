import os
import cv2 

#original image
img = cv2.imread("Fish/fish2.jpg")
print(img.shape)


img_cropped = img[0:200,0:250]
print(img_cropped.shape)
cv2.imshow('image',img)
cv2.imshow('cropped image',img_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()