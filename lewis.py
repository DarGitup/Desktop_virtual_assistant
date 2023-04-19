import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import pywhatkit 
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voices',voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("hey aayush ,Good morning")
    elif hour>=12 and hour<18:
        speak("hey aayush ,Good afternoon")
    else:
        speak("hey aayush ,Good evening")
    speak("I am Lewis! How may i help you." )

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try: 
        print("Recognizing----")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("say That again please-----")
        return
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gamil.com',587)
    server.ehlo()
    server.starttls()
    server.login('20ee1034@mitsgwl.ac.in','********')
    server.sendmail('20ee1034@mitsgwl.ac.in',to,content)
    server.close

if __name__=="__main__":
    Wishme()
    while True:
        query=takeCommand().lower()

        if "wikipedia" in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")
        elif "play" in query:
            speak("This is what I found for your search!") 
            query = query.replace("play","")
            pywhatkit.playonyt(query)
            speak("Done, Sir")
        elif "search" and "on youtube" in query:
            speak("This is what I found for your search!") 
            query = query.replace("search","")
            query = query.replace("on youtube","")
            query = query.replace("lewis","")
            web  = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            speak("Done, Sir")
        elif "on google" in query:
            import wikipedia as googleScrap
            query = query.replace("lewis","")
            query = query.replace("search","")
            query = query.replace("on google","")
            speak("This is what I found on google")

            try:
                pywhatkit.search(query)
                result = googleScrap.summary(query,1)
                speak(result)

            except:
                speak("No speakable output available")
        elif 'send email to ayush' in query:
            try:
                speak("okay, sir what should i email")
                content=takeCommand()
                to='meenaayush0104@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent ,sir")
            except Exception as e:
                print(e)
                speak('sorry sir i was not able to send email')
        