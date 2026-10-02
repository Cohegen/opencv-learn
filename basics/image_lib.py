import cv2
import os

# read image
image_path = os.path.join('.', 'Fish', 'fish1.jpg')
img = cv2.imread(image_path)

# write image
cv2.imwrite(os.path.join('.', 'Fish', 'fish1_out.jpg'), img)

# visualize
cv2.imshow('fish Image', img)  
cv2.waitKey(0)                 
cv2.destroyAllWindows()     