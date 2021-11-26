# pip install pyttsx3==2.71
import pyttsx3
engine = pyttsx3.init()
frase="Hello World"
engine.say(frase)
engine.runAndWait()