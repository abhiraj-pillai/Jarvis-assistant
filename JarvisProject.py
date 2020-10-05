import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
v = engine.getProperty("rate")

engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",150)
# print(v)

def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    name = "Abrajh"
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning! {name}")
    elif hour>=12 and hour<=16:
        speak(f"Good Evening! {name}")
    else:
        speak(f"Good evening! {name}")
    speak("How may I help You Sir!")

def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1.00
        query = r.listen(source) 
    try:
        print("Recognizing...")
        input = r.recognize_google(query, language="en-IN")
        print("User Said : ", query)
    except Exception:
        print("Repeat Again")
        return "None"
    return query

if __name__ == "__main__":
     wishMe()
     if 1:
        cmd =takeCommand().lower()
        if "wikipedia" in cmd:
            speak("Searching Wikipedia")
            cmd = cmd.replace("wikipedia"," ")
            summary = wikipedia.summary(cmd, sentences = 2)
            speak(summary)
        elif "open youtube" in cmd:
            webbrowser.open("youtube.com")
        elif "open google" in cmd:
            webbrowser.open("google.com")
        elif "open facebook" in cmd:
            webbrowser.open("facebook.com")
        elif "play music" in cmd:
            path = "D:\\abhiraj\\s"
            song = os.listdir(path)
            os.startfile(os.path.join(path,song[0]))
        elif "open code" in cmd:
            os.startfile("C:\\Users\\Pillai\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
