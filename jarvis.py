import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Goodnight")
    speak("I am jarvis, How may i help you") 

def takeCommand():
    """it take microphone input from the user and 
    returns string output"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        print("done")

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...") 
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('darshanharsh2000@gmail.com', 'your-password')
    server.sendmail('darshanharsh2000@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for excecuting task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 1)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' or 'youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' or 'google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' or 'facebook' in query:
            webbrowser.open("facebook.com")
        
        
        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\Harsh Chaudhary\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 
        elif 'email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "1803013044@ipec.org.in"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry i am unable to send the email")
        elif 'quit' in query:
            break