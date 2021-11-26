# pip install pyttsx3==2.71
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("voice", "brazil")
frase="Testando função de leitura de texto"
engine.say(frase)
engine.runAndWait()