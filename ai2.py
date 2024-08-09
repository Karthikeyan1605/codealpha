import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

r = sr.Recognizer()
engine = pyttsx3.init()


def get_audio():
  with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
    said = ""
    try:
      said = r.recognize_google(audio)
      print(said)
    except Exception as e:
      print("Exception: " + str(e))
  return said


def speak(text):
  engine.say(text)
  engine.runAndWait()


def open_website(website_name):
  webbrowser.open("https://www." + website_name + ".com")
  speak("Opening " + website_name)


def tell_time():
  now = datetime.datetime.now()
  current_time = now.strftime("%H:%M:%S")
  speak("The time is " + current_time)

def open_application(app_name):
  try:
    os.startfile(app_name)
    speak("Opening " + app_name)
  except FileNotFoundError:
    speak("Application not found")

while True:
  text = get_audio().lower()

  if "open website" in text:
    speak("Which website?")
    website_name = get_audio().lower()
    open_website(website_name)
  elif "time" in text:
    tell_time()
  elif "open application" in text:
    speak("Which application?")
    app_name = get_audio().lower()
    open_application(app_name)
  elif "exit" in text:
    speak("Goodbye!")
    break