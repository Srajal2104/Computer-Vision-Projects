# pip install commands (used to install required libraries)
# These are Python packages used in this program

# pip install SpeechRecognition -> library for converting speech to text
# pip install pyttsx3 -> library for text to speech
# pip install pywhatkit -> library for YouTube automation
# pip install wikipedia -> library for fetching Wikipedia data


# Import SpeechRecognition module used for speech-to-text conversion
import speech_recognition as sr

# Import pyttsx3 module used for text-to-speech
import pyttsx3

# Import pywhatkit module used for playing YouTube videos
import pywhatkit

# Import wikipedia module used to fetch information from Wikipedia
import wikipedia

# Import datetime module used to get date and time
import datetime


# Create an object of Recognizer class
# Recognizer is a class in SpeechRecognition module
# r will be used to recognize speech from microphone
r = sr.Recognizer()


# Dictionary (Python data structure) storing phone numbers
# Key = name , Value = phone number
phone_numbers = {"srajal":"1123456","srishti":"9999932","arpit":"3343423"}


# Dictionary storing bank account numbers
bank_account_numbers = {"tt":"123456789","mm":"9999333399"}



# Function definition for speaking text
# def is Python keyword used to create functions
def speak(command) :

    # init() is a function in pyttsx3 module
    # It initializes the speech engine
    engine = pyttsx3.init()

    # getProperty() is a method used to get voice properties
    voices = engine.getProperty('voices')

    # setProperty() changes voice settings
    # voices[1] selects female voice
    engine.setProperty('voice',voices[1].id)

    # say() method converts text into speech
    engine.say(command)

    # runAndWait() executes the speech command
    engine.runAndWait()



# Function to capture and process voice commands
def commands() : 

    try : 

        # Microphone() is a class from SpeechRecognition
        # with statement manages microphone resource automatically
        with sr.Microphone() as source :

            # adjust_for_ambient_noise() removes background noise
            r.adjust_for_ambient_noise(source)

            # Print message to console
            print('Listening... Ask now...')

            # listen() method captures audio from microphone
            audioin = r.listen(source)

            # recognize_google() converts speech to text using Google API
            my_text = r.recognize_google(audioin)

            # lower() is a Python string method to convert text to lowercase
            my_text = my_text.lower()

            # Print recognized text
            print(my_text)


            # If user says "play song"
            if 'play' in my_text :

                # replace() removes the word play from text
                my_text = my_text.replace('play','')

                # speak() function will speak the song name
                speak('playing' + my_text)

                # playonyt() opens YouTube and plays the song
                pywhatkit.playonyt(my_text)


            # If user asks for date
            elif 'date' in my_text :

                # today() is a method of datetime module
                today = datetime.date.today()

                # Speak today's date
                speak(today)


            # If user asks for time
            elif 'time' in my_text :

                # now() gets current date and time
                # strftime() formats the time
                timenow = datetime.datetime.now().strftime('%H:%M')

                # Speak current time
                speak(timenow)


            # If user asks about a person
            elif "tell about" in my_text :

                # Remove the phrase "tell about"
                person = my_text.replace('tell about','')

                # summary() fetches short info from Wikipedia
                info = wikipedia.summary(person,1)

                # Speak the information
                speak(info)


            # If user asks for phone number
            elif "phone number" in my_text :

                # list() converts dictionary keys into list
                names = list(phone_numbers)

                # Loop through names
                for name in names :

                    # If name exists in spoken text
                    if name in my_text :

                        # Print phone number
                        print(name + " phone number is " + phone_numbers[name])

                        # Speak phone number
                        speak(name + " phone number is " + phone_numbers[name])


            # If user asks for bank account number
            elif "account number" in my_text :

                # Convert dictionary keys to list
                banks = list(bank_account_numbers)

                # Loop through bank names
                for bank in banks :

                    # Check if bank name exists in spoken text
                    if bank in my_text :

                        # Print account number
                        print(bank + " bank account number is " +bank_account_numbers[bank])

                        # Speak account number
                        speak(bank + " bank account number is " +bank_account_numbers[bank])


            # If command is not recognized
            else :

                # Speak error message
                speak("Please ask correct question")


    # If microphone error occurs
    except :

        # Print error message
        print("Error in capturing microphone...")      


# Call the commands() function
# This starts the voice assistant
commands()