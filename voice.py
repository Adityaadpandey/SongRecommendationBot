import pyttsx3
import speech_recognition as sr 
import function

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):  # here audio is var which contain query
    engine.say(audio)
    engine.runAndWait()

def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising.")
        text = r.recognize_google(audio, language='en-IN')
        print(text)
    except Exception:  # For Error handling
        speak("error... speak aloud ")
        print("error... speak aloud")
        return "none"

    return text
r = sr.Recognizer()
print(r)
run = True
while run:
    query = takecom().lower()
    
    if "history" in query:
        function.try2()
        print("ok")
    else:
        run = False
