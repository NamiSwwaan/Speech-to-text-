import speech_recognition
import pyttsx3
from googletrans import Translator

recognizer = speech_recognition.Recognizer()
translator = Translator()
engine= pyttsx3.init()  
print("say exit to exit the loop")
a = 'morb'

while a != "exit":
    try:
        with speech_recognition.Microphone() as mic:
            print("Say anything in english")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            
            voices=engine.getProperty('voices')
            engine.setProperty('voices',voices[0].id)
            engine.setProperty('rate' ,150)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            a = text

            tra = translator.translate(text, dest="hi")
            tt=tra.pronunciation
            if tra is not None:
                print(f"Translation of : {text}, is : {tra.text}")
                print(tt)
            else:
                print("Translation failed")
            engine.say(tt)
            engine.runAndWait()
            
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        continue
