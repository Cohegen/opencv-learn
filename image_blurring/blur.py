import os
import cv2

# Add quotes around the file path
img = cv2.imread('Fish/fish1.jpg')

# Check if the image loaded successfully
if img is None:
    print("Error: Image not found.")
else:
    img_resize = cv2.resize(img, (640, 480))
    kernel_size = 7
    
    # Removed the invalid '3' argument from cv2.blur
    blurred_img = cv2.blur(img_resize, (kernel_size, kernel_size))
    img_blurred = cv2.GaussianBlur(img_resize, (kernel_size, kernel_size), 0)
    img_median_blur = cv2.medianBlur(img_resize,kernel_size)
    # Fixed window names to be strings
    #cv2.imshow('Resized Image', img_resize)
    #cv2.imshow('Box Blurred', blurred_img)
    cv2.imshow('Gaussian Blurred', img_blurred)
    cv2.imshow("Median blur",img_median_blur)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
