import pyttsx3
import speech_recognition as sr       #external module
import datetime
import os                             #external module
import wikipedia                      #external module
import webbrowser
import smtplib
import sys

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

#To convert Text to Speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert Voice to Text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio =r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query

#To wish
def wish():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Sir!")
    elif hour==12 and hour<=18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Void! Please tell me how can i help you.")

#To send emails
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("abhijeetsinghkang2000@gmail.com","9411085331")
    server.sendmail("abhijeetsinghkang2000@gmail.com",to,content)
    server.close()


if __name__=="__main__":
    wish()
    while True:
        query = takecommand().lower()

        #logic building for tasks
        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("open youtube.com")

        elif "open google" in query:
            webbrowser.open("open google.com")

        elif"search on chrome" in query:
            speak("What should i search sir!")
            search=takecommand()
            chromepath = "C://Program Files//Google//Chrome//Application//chrome.ex %s"
            webbrowser.get(chromepath).open_new_tab(search+'.com')

        elif "play music" in query:
            music="C:\\Users\\ABHIJEET SINGH\\Music"
            songs =os.listdir(music)
            os.startfile(os.path.join(music,songs[1]))

        elif"open command prompt" in query:
            os.system("start cmd")

        elif "what is the time now" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is {strTime}")

        elif "open vs" in query:
            vsPath="C:\\Users\\ABHIJEET SINGH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsPath)

        elif "open photoshop" in query:
            photoPath="C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe"
            os.startfile(photoPath)

        elif "send email" in query:
            try:
                speak("What should i say Sir?" )
                content=takecommand()
                to= "abhijeet.singh.cs.2019@mitmeerut.ac.in"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Bro! I am not able to send email!")
        elif "no thanks" in query:
            speak("Thanks you for using me sir. Have a good day. ")
            sys.exit()

        speak("Sir,Do you have any other work?")