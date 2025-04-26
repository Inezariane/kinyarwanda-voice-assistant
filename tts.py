from gtts import gTTS
import os

def speak(text, lang='rw'):
    tts = gTTS(text=text, lang=lang)
    filename = "response.mp3"
    tts.save(filename)
    os.system("start response.mp3") 
