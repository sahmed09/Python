import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import random

"""
pip install pipwin
pipwin install pyaudio
(If error occurred to install pyaudio)
"""

engine = pyttsx3.init('sapi5')  # sapi5 is used for taking voices
voices = engine.getProperty('voices')
print(voices)
print(voices[0].id)
engine.setProperty('voice', voices[0].id)  # using female voice. 0 for male for voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    # It wishes according to time after the program opening.
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I'm Gideon. How can I help you?")


def take_command():
    # It takes microphone input from the user and returns string output.

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:  # device_index=1 as I used earphone
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # reduce noise
        r.pause_threshold = 1.0  # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)  # take voice input from the microphone

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")  # to print voice into tex  ('en-in')
        print(f"User said: {query}")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def send_email(to, content):
    """To send email from gmail:
    Go to your gmail account from which you want to send email.
    Click Security.
    Under Less secure apps, select Go to settings for less secure apps .
    In the subwindow, select the Enforce access to less secure apps for all users radio button. ...
    Click the Save button."""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(os.environ.get('DB_USER'), os.environ.get('DB_PASSWORD'))
        server.sendmail(os.environ.get('DB_USER'), to, content)
        server.close()
        print("Email has been sent successfully.")
    except:
        print("There is an error.Plaese check out.")


if __name__ == '__main__':
    wish_me()
    while True:

        query = take_command().lower()

        # Login for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = ""  # directory in my computer
            songs = os.listdir(music_dir)  # creating lists of music in that specified directory
            print(songs)
            pick_song = random.randint(0, len(songs))
            os.startfile(os.path.join(music_dir, songs[pick_song]))
            """task: play random songs using random module. detect video or mp3"""

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Current time is {strTime}")

        elif 'open firefox' in query:
            codePath = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
            os.startfile(codePath)

        elif 'email to shihab' in query:
            """to detect name and send email to that specified person, create a dictionary using keys as names
            and values as email address """
            try:
                speak("What should I say?")
                content = take_command()
                to = "shihabahmed1995@gmail.com"
                send_email(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e)
                print("Sorry Shihab! I'm Unable to send this email at this moment.")

        elif 'exit' in query:
            speak("Closing the Program")
            exit()  # close the program
