import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from openai import OpenAI
from gtts import gTTS
import pygame
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "pub_955b0136f5de487280cac21f9dd26dc5"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    
    elif "open telegram" in c.lower():
        webbrowser.open("https://telegram.org")  # fixed Telegram URL
        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        
    else:
        # let open ai handle the requests
        pass
        
  
        
        
        
        
    # Placeholder: Do something with the command
    print(f"Processing command: {c}")
    speak(f"You said: {c}")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        with sr.Microphone() as source:
            print("Listening for wake word...")
            try:
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
                continue

        # recognize speech using Google Speech Recognition
        print("Recognizing...")
        try:
            word = recognizer.recognize_google(audio)
            print(f"Heard: {word}")

            if word.lower() == "jarvis":
                speak("Yes sir?")
                # Listen for the next command
                with sr.Microphone() as source:
                    print("Jarvis is active. Listening for your command...")
                    audio = recognizer.listen(source)

                    command = recognizer.recognize_google(audio) 
                    processCommand(command)

        except Exception as e:
            print("Error: {0}".format(e))
