# Import OpenCV module used for computer vision tasks like image processing
import cv2

# Import MediaPipe module used for AI-based face and hand landmark detection
import mediapipe as mp

# Import winsound module (built-in Windows module) used to play sound files
import winsound


# Initialize variables to store coordinates of two facial landmarks
# These are normal Python variables
x1 = 0
y1 = 0
x2 = 0
y2 = 0


# mp.solutions.face_mesh is a MediaPipe module for face landmark detection
# FaceMesh() is a class used to detect facial landmarks (468 points)
# refine_landmarks=True improves accuracy around lips and eyes
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)


# VideoCapture is an OpenCV class used to access webcam
# 0 means default webcam
camera = cv2.VideoCapture(0)


# Infinite loop to continuously capture frames from webcam
while True :

    # read() is a method of VideoCapture object
    # It captures one frame from webcam
    _ , image = camera.read()


    # flip() is an OpenCV function used to flip image horizontally
    # 1 means horizontal flip (mirror effect)
    image = cv2.flip(image,1)


    # shape is a NumPy attribute returning dimensions of image
    # fh -> frame height
    # fw -> frame width
    # _ -> number of color channels (BGR)
    fh, fw, _ = image.shape


    # cvtColor() converts color format
    # OpenCV uses BGR but MediaPipe requires RGB
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)


    # process() is a method of FaceMesh object
    # It detects face landmarks from the RGB image
    output = face_mesh.process(rgb_image)


    # multi_face_landmarks contains detected face landmarks
    landmark_points = output.multi_face_landmarks


    # If a face is detected
    if landmark_points : 

        # Access first detected face
        landmarks = landmark_points[0].landmark


        # enumerate() is a Python built-in function
        # It gives index (id) and value (landmark point)
        for id, landmark in enumerate(landmarks) :


           # Convert normalized coordinates (0–1) to pixel coordinates
           x = int(landmark.x * fw)
           y = int(landmark.y * fh)


           # Landmark ID 43 corresponds to one side of mouth
           if id == 43 :
                x1 = x
                y1 = y


           # Landmark ID 287 corresponds to other side of mouth
           if id == 287 :
                x2 = x
                y2 = y     


        # Calculate distance between two mouth points
        # **2 = square
        # **0.5 = square root (distance formula)
        dist =int(((x2-x1)**2 + (y2-y1)**2)**(0.5))


        # Print distance value for debugging
        print(dist) 


        # If distance between mouth points is large
        # That means user is smiling
        if dist > 99 :

            # imwrite() is an OpenCV function used to save image
            cv2.imwrite("selfie.png",image)


            # Play sound using winsound module
            # SND_FILENAME tells it to play a sound file
            winsound.PlaySound("sound.wav",winsound.SND_FILENAME)


            # waitKey() pauses program for 100 milliseconds
            cv2.waitKey(100)


    # imshow() displays image in a window
    cv2.imshow("Auto selfie for smiling faces using python", image)


    # waitKey() waits for keyboard input
    key = cv2.waitKey(100)


    # If ESC key (ASCII value 27) is pressed
    # break exits the loop
    if key == 27 :
        break


# release() releases the webcam resource
camera.release()


# destroyAllWindows() closes all OpenCV windows
cv2.destroyAllWindows()