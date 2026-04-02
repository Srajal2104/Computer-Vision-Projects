# Import OpenCV library (module) used for computer vision tasks
import cv2

# Import MediaPipe library (module) used for hand tracking and ML pipelines
import mediapipe as mp

# Import PyAutoGUI library (module) used to control keyboard, mouse, system actions
import pyautogui


# Initialize variables to store coordinates of two fingers
# These are normal Python variables
x1 = y1 = x2 = y2 = 0


# VideoCapture is a built-in OpenCV class used to capture video from webcam
# 0 means the default system webcam
webcam = cv2.VideoCapture(0)


# mp.solutions.hands is a MediaPipe solution module for hand tracking
# Hands() is a class that loads the hand detection model
# my_hands becomes an object of Hands class
my_hands = mp.solutions.hands.Hands()


# drawing_utils is a MediaPipe utility module used for drawing hand landmarks
drawing_utils = mp.solutions.drawing_utils


# Infinite loop to continuously read frames from webcam
# while is a Python built-in loop keyword
while True :

    # read() is a built-in method of VideoCapture object
    # It captures a frame from webcam
    # _ stores True/False if frame captured successfully
    # image stores the captured frame
    _ , image = webcam.read()


    # flip() is an OpenCV built-in function
    # It flips the image horizontally (mirror view)
    image = cv2.flip(image,1)


    # shape is a NumPy attribute that gives image dimensions
    # frame_height = height of image
    # frame_width = width of image
    # _ = number of color channels (BGR)
    frame_height, frame_width, _ = image.shape


    # cvtColor() is an OpenCV built-in function
    # Converts image color space from BGR to RGB
    # MediaPipe requires RGB format
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)


    # process() is a method of the Hands object
    # It detects hands and returns results
    output = my_hands.process(rgb_image)


    # multi_hand_landmarks is an attribute containing detected hand landmarks
    # Each hand has 21 landmark points
    hands = output.multi_hand_landmarks


    # If any hand is detected
    if hands : 

        # Loop through each detected hand
        for hand in hands :

            # draw_landmarks() is a MediaPipe utility function
            # It draws the hand skeleton on the image
            drawing_utils.draw_landmarks(image,hand)


            # landmark is a list of 21 points representing finger joints
            landmarks = hand.landmark


            # enumerate() is a Python built-in function
            # It returns index(id) and value(landmark)
            for id, landmark in enumerate(landmarks) :


                # Convert normalized coordinates (0-1) to pixel coordinates
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)


                # id == 8 represents INDEX FINGER TIP
                if id == 8 :

                    # circle() is an OpenCV function used to draw a circle
                    cv2.circle(img=image,center=(x,y),radius=8,color=(0,255,255),thickness=3)

                    # Store coordinates of index finger
                    x1 = x
                    y1 = y


                # id == 4 represents THUMB TIP
                if id == 4 :

                    # Draw red circle on thumb
                    cv2.circle(img=image,center=(x,y),radius=8,color=(0,0,255),thickness=3)

                    # Store thumb coordinates
                    x2 = x
                    y2 = y


        # Calculate distance between thumb and index finger
        # ** is exponent operator in Python
        # **0.5 calculates square root
        dist = ((x2-x1)**2 + (y2-y1)**2)**(0.5)//4


        # line() is an OpenCV function to draw line between fingers
        cv2.line(image,(x1,y1),(x2,y2),(0,255,0),5)


        # If distance between fingers is large
        if dist > 50 :

            # press() is a PyAutoGUI function that simulates keyboard press
            # "volumeup" increases system volume
            pyautogui.press("volumeup")

        else :

            # "volumedown" decreases system volume
            pyautogui.press("volumedown")


    # imshow() is an OpenCV function to display image in a window
    cv2.imshow("Hand Volume Control Using Python",image)


    # waitKey() waits for keyboard input for 10 milliseconds
    key = cv2.waitKey(10)


    # If ESC key (ASCII 27) is pressed, exit loop
    if key == 27 :
        break


# release() method releases the webcam resource
webcam.release()


# destroyAllWindows() closes all OpenCV windows
cv2.destroyAllWindows()