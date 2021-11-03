import re
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import os 
import webbrowser as wb 
import pyautogui
import psutil
import pyjokes
from wikipedia.wikipedia import search
from PyQt5 import QtCore, QtGui, QtWidgets

def say(audio):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    vrate=150
    engine.setProperty('rate',vrate)
    engine.say(audio)
    engine.runAndWait()
#audio="hi hrithik how can i help you "
def jokes():
    say(pyjokes.get_jokes())
def welcome():
    say("welcome back  hrithik , how can i help you")
def greetings():
    say("Hi Hrithik , it's me jarvis")
def time():
    
    h=datetime.datetime.now().hour
    if h>=12 and h<=17:
        say("good noon ")
    elif h>17 and h<=24:
        say("good evening")
    else:
        say("good morning") 
def cpu():
    usage=str(psutil.cpu_percent())
    say("here is cpu usage"+usage)
def mail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('hrithikpaul2001@gmail.com','hrithik@123@:)')
    server.sendmail("hrithikpaul2001@gmail.com",to,content)
    server.close()
def ss():
    img=pyautogui.screenshot()
    img.save("C:\\Users\\MY PC\\Desktop\\vassit\\ss.png")

def wiki(audio):
    audio=audio.replace('wikipedia','')
    result=wikipedia.summary(audio)
    say(result)
def micr():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listinening..")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("memorizing....")
        query=r.recognize_google(audio,language='en=US')
        
    except Exception as e:
        print(e)
        say('say it again')
        return 'None'

        
    return query
if __name__=="__main__":
    welcome()
    time()
    while True:

        query=micr().lower()
        print(query)

        if 'hi' in query:
            greetings()
        if 'good noon' in query or 'good morning' in query or 'good afternoon' in query:
            time()

        if 'wikipedia' in query:
            say("searching in wikipedia please wait for a while")
            wiki(query)
        if 'email' in query:
            to="sgsayanighatak@gmail.com"
            content="hi"
            mail(to,content)     
            #print(search)
            #wb.get(chromepath).open_new_tab(search + '.com')
        if 'remember' in query or 'write' in query :
            say("yes say I am making txt file ")
            data=micr()
            f=open("input.txt","w")
            f.write(data)
            f.close()
        if 'read' in query:
            say("what file you want to read")
            data=micr()
            data=data+"."+"txt"
            f=open(data,'r')
            con=f.read()
            say(con)
        if 'screenshot' in query:
            ss()
        if 'jokes'in query:
            jokes()
        if "cpu" in query:
            cpu()
        
        if "bye" in query or "goodbye" in query or "tata" in query:
            say("good bye , have a nice day ")
            quit()
        elif 'shutdown' in query:
            say("pc is now shutdowning")
            os.system('shutdown /s /t 1')
        elif 'restart' in query:
            say("pc is now restarting")
            os.system('shutdown /r /t 1')
        elif 'logout' in query:
            say("pc will logout")
            os.system('shutdown - l')
        elif 'browser' in query:
            say("say what you want to search")
            search=micr().lower()
            wb.open(search+".com")
        elif 'da' in query:
            say("are dada how are you")
            
