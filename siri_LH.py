import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("Hi, Lindsay where do you want to go shopping?")
    print("Listening...")
    audio = r.listen(source)
    print("Thinking...")


try:
    words = r.recognize_google(audio)
    speak.Speak("Ok Lindsay, let's look for " + r.recognize_google(audio) + " on Google.")
    wb.open("https://www.google.com/search?q=" + words)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results fromn Google Speech Recognition service; {0}".format(e))
