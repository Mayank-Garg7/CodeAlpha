# First of all You need to install SpeechRecognition for 
# taking voice as a input

#  pip install SpeechRecognition gTTS


import speech_recognition as sr
from gtts import gTTS
import os

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
        return ""

def speak(text):
    tts = gTTS(text)
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")  # You may need to change this command based on your OS.

if __name__ == "__main__":
    while True:
        user_input = listen()
       
        if "hello" in user_input:
            speak("Hello! How can I assist you?")
        elif "goodbye" in user_input:
            speak("Goodbye!")
            break

