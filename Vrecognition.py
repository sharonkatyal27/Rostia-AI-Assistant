
from pyjokes.pyjokes import get_joke
import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes


engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hello! This is Rosita here your assistant.")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(" Today's date is ")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    elif hour >= 18 and hour <= 22:
        speak("Good evening!")
    else:
        speak("Good night!")

    speak("Welcome back Sharon! How can i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("I didn't get you. Can you say that again please")

        return"NONE"

    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sharonkatyal2000@gmail.com", "")
    server.sendmail("sharonkatyal2000@gmail.com", to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/hp/Pictures/ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU usage" + usage)

    battery = psutil.sensors_battery()
    speak("Battery is")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())



if __name__ == "__main__":

    

    while True:
        query = takeCommand().lower()
        print(query)

        if "hello" in query:
            wishme()
        elif "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should i write?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendemail(to, content)
                speak("Email sent successfully!")
            except Exception as e:
                speak(e)
                speak("Unable to send the mail ")
        elif "search in chrome" in query:
            speak("what should i search?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe  %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "log out" in query:
            os.system("shutdown - 1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "music" in query:
            songs_dir = "C:/Users/hp/Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif "remember" in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("You asked me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "tell" in query:
            remember = open("data.txt", "r")
            speak("I remember" + remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("Screenshot taken")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes()
        elif "offline" in query:
            speak("It was nice to help you ! See you soon !")
            quit()

