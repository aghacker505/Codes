import datetime
import os
import smtplib
import time
import webbrowser
import pyjokes
import pyttsx3
import speech_recognition as sr


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print('Recognizing...')
            qurey = recognizer.recognize_google(audio), 
            language='en-in'
            print(qurey)
            return qurey
        except sr.UnknownValueError:
            print('Say that again please...')

# sptext()

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    engine.say(x)
    engine.runAndWait()
# speechtx("What are you doing guysss")

if __name__ == '__main__':

    if "tom" in sptext().lower():
        while True:
            data = sptext().lower()
            if "your name" in data:
                name = "I am your tom"
                speechtx(name)
            elif "old you" in data:
                age = "I've always wanted to do this. How old do you think I am?"
                speechtx(age)
            elif "now time" in data:
                now = datetime.datetime.now().strftime("%I%M%p")
                speechtx(now)
            elif 'youtube' in data:
                webbrowser.open("https://www.youtube.com/")
            elif "joke" in data:
                joke = pyjokes.get_joke(language="en", category="neutral")
                speechtx(joke)
            elif "play song" in data:
                song = "path of song"
                listsong = os.listdir(song)
                print(listsong)
                os.startfile(os.path.join(song, listsong[0]))
            
            elif "exit" in data:
                speechtx("thank you for using me")
                break

            # time.sleep(2)
        
    else:
        print("sorry try again")

#we can also send email through this