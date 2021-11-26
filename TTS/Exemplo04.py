# pip install pyttsx3==2.71
import pyttsx3
f = open('frase.txt', 'r')
conteudo = f.read()
engine = pyttsx3.init()
engine.setProperty("voice", "brazil")
frase=conteudo
engine.say(frase)
f.close()
engine.runAndWait()
