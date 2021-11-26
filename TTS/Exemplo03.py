# pip install gTTS
# pip install playsound
from gtts import gTTS
from playsound import playsound

frase="Olá. Vamos sintetizar voz com o Python"
tts = gTTS(frase,lang='pt-br',slow=False, tdl="co.in")
tts.save('hello.mp3')
print("Estou aprendendo o que você disse...")
playsound('hello.mp3')