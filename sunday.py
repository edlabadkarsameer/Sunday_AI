import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import smtplib
import sys
import random
from requests import get
#import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)
def speak(audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()
def wishMe():
        hour = int(datetime.datetime.now().hour)
        
        if hour>=0 and hour<12:
                speak("sunday is activated, Good Morning Sir")

        elif hour>=12 and hour<18:
                speak("sunday is activated, Good Afternoon  Sir")
        
        else :
                speak("sunday is activated, Good Evening Sir")
def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                speak("i am listning sir ")
                r.pause_threshold = 0.8
                audio = r.listen(source)

        try:
                speak("recognizing")
                query = r.recognize_google(audio, language='en-in')
                print(f"user said :{query}")
        


        except Exception as e:
                speak("say that again sir...")
                return "none"
        return query
def sendEmail(to, content):
       server = smtplib.SMTP('smtp.gmail.com', 587)
       server.ehlo()
       server.starttls()
       server.login('edlabadkarsameer@gmsil.com', 'sameersameer7860')
       server.sendMail('edlabadkarsameer@gmail.com', to, content)
       server.close()
if __name__ == "__main__":
        wishMe()
        while True:
        #if 1:
                query = takeCommand().lower()


                if 'wikipedia' in query:
                        speak ('Searching Wikipedia...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=1)
                        speak ("According to Wikipedia")
                        speak(results)
                        print(results)
                elif 'open youtube' in query:
                        speak('opening youtube....')
                        webbrowser.open("youtube.com")
                elif 'open facebook' in query:
                        speak('opening facebook....')
                        webbrowser.open("facebook.com")
                elif 'open google' in query:
                        speak('opening google')
                        webbrowser.open("google.com")
                elif 'open stackoverflow' in query:
                        speak('opening stackoverflow')
                        webbrowser.open("stackoverflow.com")     
                elif 'how are you' in query: 
                        speak('I am good sir') 
                elif 'what is your name' in query: 
                        speak('my name is sunday. i am an artificial intelligence. designed and developed by mr sameer')
                elif 'who is sameer' in query: 
                        speak('he is god')
                elif 'how old you are' in query: 
                        speak('infinity years old  haaahahahahahhhaaaaaahhahahahahahahahahahhhhhhahahahahahahahahahahahahahahahahahahahahahahahheheheheheheheheheheeeeeeeehehehehehehehehehehehehehehehehehehheheheheheh')
                elif 'good morning' in query: 
                        speak('how can in help you')
                elif 'vaibhavi' in query: 
                        speak('yes i know vaibhavi danger , she is bhaitad and jhendu !!!!')
                elif 'what do you think' in query: 
                        speak('sir, i think you should not')
                elif 'good evening' in query: 
                        speak('how can in help you')
                elif 'good afternoon' in query: 
                        speak('how can in help you')
                elif 'open whatsapp' in query:
                        speak('opening whatsapp')
                        webbrowser.open("web.whatsapp.com")
                elif 'who is arya' in query:
                        speak('ohhh wow , hmmm, she is very smart girl and she is your girlfriend too')
                elif 'time' in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"sir, the time is {strTime}")
                elif 'shabash' in query:
                        speak('thank you sir, very glad to hear!!')
                elif 'hello' in query :
                        speak("hello sir, nice to see you again ")
                elif 'man' in query:
                        speak("there is only one man and that is sameer")
                elif 'computer configuration' in query:
                        speak("the computer configuration according to the hardware directory is OS is windows 10 home, AMD ryzen 5 quad core dual string processor and 500 GB Solid state drive")
                elif 'open code' in query:
                        codePath = "C:\\Users\\edlab\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                        os.startfile(codePath)
                #elif 'send messaege' in query:
                        #pywhatkit.sendwhatmsg("+918390770497","this is a testing protocol by sunday",1,59)
                #elif'play song on youtube' in query:
                        #pywhatkit.playonyt("see you again")
                elif 'email to sameer' in query:
                        try:
                                speak("what should i say?, sir ")
                                content = takeCommand()
                                to = "sameeredlabadkar4@gmail.com"
                                sendEmail = (to, content)
                                speak("EMail has been sent!")
                        except Exception as e:
                              speak("sorry sameer sir , i am not able to send the mail at this moment")
                
                elif "no thanks" in query:
                        speak("okay sir, i am taking leave")
                        sys.exit()

                speak("sir, do you have any other work?")