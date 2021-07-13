import pyttsx3
import speech_recognition

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):  # here audio is var which contain query
    engine.say(audio)
    engine.runAndWait()

speak("hi bro")

