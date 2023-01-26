import os
import pyttsx3
import sys
import speech_recognition as sr
import time
import webbrowser


recognition = sr.Recognizer()
with sr.Microphone() as src:
    print("How can i help you: ")

    audio=recognition.listen(src)
    text=recognition.recognize_google(audio)

    shut_down = ["shut down the computer","shut down the pc","shut down","close the computer",'close the pc']

    if text in shut_down:
        print(input("Are you sure? "))

        if text in["yes","yep"]:
            sec=30
            os.system(f'shutdown /s /t  {sec}')
            pyttsx3.speak(f"i will shutdown after{sec} seconds")

        elif text in["restart the computer","restart the pc","restart"]:
            print(input("Are you sure? "))

        if text in["yes","yep"]:
            os.system(f'shutdown /r /t  {sec}')
            pyttsx3.speak(f"i will restart after{sec} seconds")

    elif text in["open browser","open the browser"]:
            print(input("Which type of browser(google/Bing)"))

            if text in("google"):
                pyttsx3.speak("openning google")
                webbrowser.open("https://www.google.com.eg/")

            elif text in("bing"):
                pyttsx3.speak("openning Bing")
                webbrowser.open("https://www.bing.com/")

    elif text in["open google","open Google"]:
            pyttsx3.speak("openning google")
            webbrowser.open("https://www.google.com.eg/")

    elif text in["open facebook","open Facebook","Open Facebook","Open facebook"]:
        pyttsx3.speak("openning facebook")
        webbrowser.open("https://www.facebook.com/")

    elif text in["Open Youtube","Open youtube","open youtube"]:
        pyttsx3.speak("openning Youtube")
        webbrowser.open("https://www.youtube.com/")

    elif text in["open fifa","open Fifa","Open Fifa","open FIFA","Open FIFA"]:
        pyttsx3.speak("openning FIFA")
        os.startfile("D:\Games\FIFA 19\FIFA19.exe")
    
    elif text in ("close the program","Close the program"):
        pyttsx3.speak("clossing the program")
        print("closing the program....")
        sys.exit