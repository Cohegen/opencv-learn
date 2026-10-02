import cv2

# Use 0 for default built-in webcam, or 1/2 for external webcams
webcam = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not webcam.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = webcam.read()
    
    # If frame reading failed, break the loop
    if not ret:
        print("Error: Failed to grab frame.")
        break
        
    cv2.imshow('frame', frame)
    
    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
webcam.release()
cv2.destroyAllWindows()
