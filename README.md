# Computer Vision Projects

This repository contains a collection of **computer vision and automation projects built using Python**.<br>
These projects demonstrate **real-time applications of OpenCV, MediaPipe, and Python automation libraries** such as PyAutoGUI, SpeechRecognition, and PyWhatKit.<br><br>

The projects focus on **face tracking, hand gesture recognition, motion detection, automation, and AI interaction using webcam-based systems.**

---

# Projects

## 1. Face Detection
- Detects faces in **real-time using a webcam**<br>
- Uses **OpenCV Haar Cascade Classifier**<br>
- Draws **bounding boxes around detected faces**<br>
- Works with **live camera feed**<br><br>

## 2. Auto Selfie (Smile Detection)
- Uses **MediaPipe Face Mesh (468 facial landmarks)**<br>
- Detects smile based on **mouth landmark distance**<br>
- Automatically **captures a selfie when the user smiles**<br>
- Plays **sound feedback after capturing the image**<br><br>

## 3. AI Assistant (Voice-Based)

A simple **voice-controlled AI assistant built using Python.**<br><br>

### Features
- Converts **speech to text** using `SpeechRecognition`<br>
- Responds using **text-to-speech** with `pyttsx3`<br>

### Capabilities
- Play songs on **YouTube**<br>
- Tell **date and time**<br>
- Fetch information from **Wikipedia**<br>
- Retrieve saved **phone numbers**<br><br>

## 4. Face Controlled Mouse
- Uses **MediaPipe Face Mesh**<br>
- Tracks **facial landmarks**<br>
- Moves the **mouse cursor based on face movement**<br>
- **Eye blink detection** triggers mouse click<br>
- Demonstrates **hands-free computer control**<br><br>

## 5. Hand Gesture Mouse Control
- Uses **MediaPipe Hands**<br>
- Tracks **hand landmarks**<br>
- Moves mouse pointer using **index finger**<br>
- Click action triggered by **finger distance**<br>
- Provides a **touchless mouse interface**<br><br>

## 6. Security Camera (Motion Detection)
- Detects **motion using frame differencing**<br>
- Converts frames to:<br>
  - Grayscale<br>
  - Threshold image<br>
- Identifies **movement using contours**<br>
- Plays **beep sound alert when motion is detected**<br><br>

## 7. Hand Gesture Volume Control
- Uses **hand landmarks to measure finger distance**<br>
- Controls **system volume using hand gestures**<br>
- Implements **real-time gesture tracking**<br>
- Uses **PyAutoGUI for keyboard simulation**<br><br>

## 8. WhatsApp Automation
- Sends **scheduled WhatsApp messages automatically**<br>
- Built using **pywhatkit**<br>
- Useful for **automated reminders or greetings**<br><br>

---

# Tech Stack

- Python<br>
- OpenCV<br>
- MediaPipe<br>
- PyAutoGUI<br>
- SpeechRecognition<br>
- pyttsx3<br>
- pywhatkit<br>
- Wikipedia API<br>

---

# Key Learnings

- Real-time **computer vision using OpenCV**<br>
- **Hand and face tracking** using MediaPipe<br>
- Building **gesture-based system controls**<br>
- Creating **automation scripts with Python**<br>
- Working with **webcam video streams**<br>
- Implementing **AI voice assistants**<br>
