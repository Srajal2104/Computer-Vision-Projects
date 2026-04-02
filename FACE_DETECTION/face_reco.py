# Import the OpenCV library
# cv2 is a built-in module from OpenCV used for computer vision tasks
import cv2

# Create an object of CascadeClassifier class
# CascadeClassifier is a built-in class in OpenCV used for object detection (faces, eyes, etc.)
# 'haarcascade_frontalface_default.xml' is a pre-trained model file used to detect faces
face_cascade = cv2.CascadeClassifier("FACE_DETECTION/haarcascade_frontalface_default.xml")

# VideoCapture is a built-in OpenCV class used to capture video from camera or file
# 0 means the default webcam of the system
webcam = cv2.VideoCapture(0) 

# Infinite loop to continuously capture frames from webcam
# while is a Python built-in loop keyword
while True:

    # read() is a built-in method of VideoCapture object
    # It captures a single frame from the webcam
    # It returns two values:
    # _  -> boolean value (True if frame captured successfully)
    # img -> the captured frame (image object)
    _, img = webcam.read()

    # cvtColor() is a built-in OpenCV function used to convert image color formats
    # img is the input image
    # cv2.COLOR_BGR2GRAY is a built-in constant that converts BGR image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detectMultiScale() is a built-in method of CascadeClassifier object
    # It detects objects (faces here) in the grayscale image
    # Parameters:
    # gray -> input image
    # 1.2  -> scale factor (how much image size is reduced at each step)
    # 4    -> minNeighbors (number of neighbors required for detection)
    # faces will store coordinates of detected faces
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)

    # Loop through all detected faces
    # Each face is represented by (x, y, w, h)
    # x,y -> top-left corner of rectangle
    # w,h -> width and height of rectangle
    for (x, y, w, h) in faces:

        # rectangle() is a built-in OpenCV function used to draw rectangles
        # img -> image on which rectangle is drawn
        # (x,y) -> starting point (top-left)
        # (x+w,y+h) -> ending point (bottom-right)
        # (0,255,0) -> color in BGR format (green)
        # 3 -> thickness of rectangle border
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)

    # imshow() is a built-in OpenCV function used to display an image in a window
    # "Face detection" is the window title
    # img is the frame to display
    cv2.imshow("Face detection", img)

    # waitKey() is a built-in OpenCV function
    # It waits for a keyboard key press
    # 10 means delay of 10 milliseconds
    # It returns the ASCII value of the pressed key
    key = cv2.waitKey(10)

    # If the pressed key is ESC (ASCII value = 27)
    # break exits the while loop
    if key == 27:
        break

# release() is a built-in method of VideoCapture object
# It releases the webcam resource
webcam.release()

# destroyAllWindows() is a built-in OpenCV function
# It closes all OpenCV windows created by imshow()
cv2.destroyAllWindows()