from gtts import gTTS
from playsound import playsound
import os

text = ''
tts = gTTS(text = text , lang='ko')

fileName = "tovoice"
fileExtension = "mp3"

fullPath:str = fr"{os.getcwd()}/{fileName}.{fileExtension}".replace("\\","/")

tts.save(fullPath)

playsound(fullPath)