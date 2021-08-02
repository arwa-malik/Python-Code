import speech_recognition as sr

import pyttsx3

r = sr.Recognizer()

def SpText(command):

engine = pyttsx3.init()

engine.say(command)

engine.runAndWait()

while(1):

try:

with sr.Microphone as source2:

r.adjust_for_ambient_noise(source2 , duration=0.2)

audio2 = r.listen(source2)

MyText = r.recognize_google(audio2)

MyText = MyText.lower()

print("Had you just prompted " + MyText)

SpText(MyText)

except sr.RequestError as e:

print("Oops sorry we are unable to process your request!! Try again ; {0}".format(e))

except sr.UnknownValueError:

print("An error with with some different named occurs")