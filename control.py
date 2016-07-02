import speech_recognition as sr
import os
# obtain audio from the microphone                                              
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
text = r.recognize_google(audio)
os.system(text)







