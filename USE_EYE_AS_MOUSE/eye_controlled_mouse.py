# Import OpenCV module used for image processing and webcam access
import cv2

# Import mediapipe module used for AI-based face landmark detection
import mediapipe

# Import pyautogui module used to control mouse and keyboard
import pyautogui


# FaceMesh is a class from mediapipe used for detecting facial landmarks
# refine_landmarks=True improves accuracy around eyes and lips
face_mesh_landmarks = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)


# VideoCapture is an OpenCV class used to capture video from webcam
cam = cv2.VideoCapture(0)


# pyautogui.size() is a function that returns screen resolution
# screen_w -> screen width
# screen_h -> screen height
screen_w, screen_h = pyautogui.size()


# Infinite loop to continuously read frames from webcam
while True :

    # read() method captures a frame from webcam
    _,image = cam.read()


    # flip() is an OpenCV function used to mirror the image horizontally
    image = cv2.flip(image,1)


    # shape attribute gives dimensions of the image
    # window_h -> frame height
    # window_w -> frame width
    # _ -> number of color channels
    window_h,window_w,_ = image.shape


    # Convert BGR image to RGB because mediapipe requires RGB format
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)


    # process() method detects facial landmarks from image
    processed_image = face_mesh_landmarks.process(rgb_image)


    # multi_face_landmarks contains landmarks of detected faces
    all_face_landmark_points = processed_image.multi_face_landmarks


    # If any face is detected
    if all_face_landmark_points :

        # Get landmarks of the first detected face
        one_face_landmark_points = all_face_landmark_points[0].landmark


        # Loop through eye tracking landmarks (474 to 477)
        for id,landmark_point in enumerate(one_face_landmark_points[474 : 478]) :

            # Convert normalized coordinates (0–1) to pixel coordinates
            x = int(landmark_point.x * window_w)
            y = int(landmark_point.y * window_h)


            # If landmark id is 1 (center point for cursor tracking)
            if id==1 :

                # Convert webcam coordinates to screen coordinates
                mouse_x = int(screen_w / window_w * x)
                mouse_y = int(screen_h / window_h * y)

                # moveTo() moves mouse cursor to calculated position
                pyautogui.moveTo(mouse_x,mouse_y)


            # circle() draws landmark points on the image
            cv2.circle(image,(x,y),3,(0,0,255))


        # Landmarks used for blink detection
        left_eye = [one_face_landmark_points[145],one_face_landmark_points[159]]   


        # Draw circles around eye landmarks
        for landmark_point in left_eye :

            x = int(landmark_point.x * window_w)
            y = int(landmark_point.y * window_h)

            cv2.circle(image,(x,y),3,(0,255,255)) 


        # Detect blink by measuring vertical distance between eye landmarks
        if(left_eye[0].y - left_eye[1].y < 0.01) :

            # click() performs a mouse click
            pyautogui.click()

            # sleep() pauses program for 2 seconds to avoid multiple clicks
            pyautogui.sleep(2)

            print("mouse clicked")   


    # Display the webcam window
    cv2.imshow("Eye controlled mouse", image)


    # waitKey() waits for keyboard input
    key = cv2.waitKey(100)


    # If ESC key (ASCII 27) is pressed exit loop
    if key == 27 :
        break


# release() releases the webcam resource
cam.release()


# destroyAllWindows() closes all OpenCV windows
cv2.destroyAllWindows()