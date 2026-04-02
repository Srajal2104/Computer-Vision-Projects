# Import OpenCV module used for image processing and computer vision
import cv2

# Import winsound module (built-in Windows module)
# It is used to play beep sounds
import winsound


# VideoCapture is a class from OpenCV
# It is used to access the webcam
# 0 means default system webcam
webcam = cv2.VideoCapture(0)


# Infinite loop to continuously capture frames from webcam
# while is a Python built-in loop keyword
while True :

    # read() is a method of VideoCapture class
    # It captures a frame from the webcam
    # _ stores True/False if frame captured successfully
    # im1 stores first image frame
    _,im1 = webcam.read()

    # Capture second frame immediately after first frame
    _,im2 = webcam.read()


    # absdiff() is an OpenCV function
    # It calculates the absolute difference between two images
    # This helps detect motion between frames
    diff = cv2.absdiff(im1,im2)


    # cvtColor() converts image color space
    # Here it converts BGR image into GRAY image
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)


    # threshold() is an OpenCV function used for image segmentation
    # Parameters:
    # gray -> input grayscale image
    # 20 -> threshold value
    # 255 -> maximum value
    # THRESH_BINARY -> converts pixels into black/white
    _,thresh = cv2.threshold(gray,20,255,cv2.THRESH_BINARY)


    # findContours() is an OpenCV function used to detect object boundaries
    # thresh -> binary image
    # RETR_TREE -> contour retrieval mode
    # CHAIN_APPROX_SIMPLE -> contour approximation method
    contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


    # Loop through all detected contours (moving objects)
    for c in contours :

        # contourArea() calculates area of contour
        # Small areas are ignored to remove noise
        if cv2.contourArea(c) < 5000 :
            continue


        # If large movement detected
        # winsound.Beep() plays beep sound
        # 500 -> frequency of sound
        # 100 -> duration in milliseconds
        winsound.Beep(500,100)


    # imshow() is an OpenCV function used to display image in window
    # "Security camera" is the window title
    cv2.imshow("Security camera",thresh)


    # waitKey() waits for keyboard input
    # 10 ms delay
    # If ESC key (ASCII 27) is pressed, exit loop
    if cv2.waitKey(10) == 27 :
        break


# release() method releases the webcam resource
webcam.release()


# destroyAllWindows() closes all OpenCV windows
cv2.destroyAllWindows()