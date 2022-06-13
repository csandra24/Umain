import time
import numpy as np
import speech_recognition as sr
from numpy import true_divide
from playsound import playsound
import os

listener = sr.Recognizer()
os.startfile('saluda.mp4')

def record_audio():
    with sr.Microphone() as source:
        voice = listener.listen(source)
        voice_data = ''
        try:
            voice_data = listener.recognize_google(voice, language='es-ES')
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
        except sr.RequestError:
            print('Battery low')
        return voice_data

def respond(voice_data):
    if 'presentaros' in voice_data:
        os.startfile('1.mp4')

    if 'conocerte' in voice_data:
        os.startfile('2.mp4')
    
    if 'objetivo' in voice_data:
        os.startfile('3.mp4')

    if 'llego tarde' in voice_data:
        os.startfile('4.mp4')
    
    if 'glorieta' in voice_data:
        os.startfile('5.mp4')
    
    if 'sin gasolina' in voice_data:
        os.startfile('7.mp4')
    
    if 'nombre' in voice_data:
        os.startfile('8.mp4')
        print('')

    if 'hasta luego' in voice_data:
        os.startfile('6.mp4')
        exit()

       

time.sleep(1)
print('Say Something!')
while 1:
    voice_data = record_audio()
    respond(voice_data)
