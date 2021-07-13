import pyttsx3
import speech_recognition

engine = pyttsx3.init()


def speak(some):
    engine.say(some)
    engine.runAndWait

speak("hi bro")

