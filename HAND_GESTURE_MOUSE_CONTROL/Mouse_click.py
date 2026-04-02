# Import OpenCV module used for webcam access and image processing
import cv2

# Import mediapipe module used for AI-based hand landmark detection
import mediapipe

# Import pyautogui module used to control mouse and keyboard
import pyautogui


# Hands() is a class from mediapipe used to detect hand landmarks
# capture_hands becomes an object of Hands class
capture_hands = mediapipe.solutions.hands.Hands()


# drawing_utils is a mediapipe utility module used for drawing landmarks
drawing_option = mediapipe.solutions.drawing_utils


# pyautogui.size() returns screen resolution
# screen_width -> width of computer screen
# screen_height -> height of computer screen
screen_width, screen_height = pyautogui.size()


# VideoCapture is an OpenCV class used to access webcam
camera = cv2.VideoCapture(0)


# Variables used to store coordinates of thumb and index finger
x1 = y1 = x2 = y2 = 0


# Infinite loop to continuously capture frames
while True :

    # read() method captures frame from webcam
    _,image = camera.read()


    # shape attribute returns image dimensions
    image_height, image_width, _ = image.shape


    # flip() flips image horizontally (mirror effect)
    image = cv2.flip(image,1)


    # Convert BGR image to RGB because mediapipe requires RGB
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)


    # process() detects hand landmarks in the frame
    output_hands = capture_hands.process(rgb_image)


    # multi_hand_landmarks contains detected hand landmarks
    all_hands = output_hands.multi_hand_landmarks


    # If any hand is detected
    if all_hands :

        # Loop through each detected hand
        for hand in all_hands :

            # draw_landmarks() draws hand skeleton on image
            drawing_option.draw_landmarks(image,hand)


            # landmark list contains 21 hand landmark points
            one_hand_landmarks = hand.landmark


            # enumerate() gives index(id) and landmark point
            for id, lm in enumerate(one_hand_landmarks) :

                # Convert normalized coordinates (0–1) to pixel coordinates
                x = int(lm.x * image_width)
                y = int(lm.y * image_height)


                # id 8 corresponds to INDEX FINGER TIP
                if id == 8 :

                    # Convert webcam coordinates to screen coordinates
                    mouse_x = int(screen_width / image_width *x)
                    mouse_y = int(screen_height / image_height * y)

                    # Draw circle on index finger tip
                    cv2.circle(image,(x,y),10,(0,255,255))

                    # moveTo() moves mouse cursor to calculated position
                    pyautogui.moveTo(mouse_x,mouse_y)

                    # Store index finger coordinates
                    x1 = x
                    y1 = y


                # id 4 corresponds to THUMB TIP
                if id == 4 :

                    # Store thumb coordinates
                    x2 = x
                    y2 = y

                    # Draw circle on thumb tip
                    cv2.circle(image,(x,y),10,(0,255,255))


        # Calculate vertical distance between thumb and index finger
        dist = y2 - y1

        # Print distance for debugging
        print(dist)  


        # If fingers come close together
        if(dist < 20) :

            # Perform mouse click
            pyautogui.click()      

            print("clicked")    


    # Display webcam output window
    cv2.imshow("Hand movement video capture",image)


    # waitKey() waits for keyboard input
    key = cv2.waitKey(100)


    # If ESC key pressed exit loop
    if key == 27 :
        break


# Release webcam resource
camera.release()


# Close all OpenCV windows
cv2.destroyAllWindows()