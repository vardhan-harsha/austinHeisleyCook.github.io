#Make sure to make a directory to send the transcriptions
import speech_recognition as sr
import os
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
text = r.recognize_sphinx(audio)
os.system("cd transcriptions")
s = open("spokentext.docx", "w")
r = open("spokentext.docx", "r")
s.write(text)

