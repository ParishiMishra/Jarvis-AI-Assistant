import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Emma,your assistant. Please tell me how may I help you?")
     
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio= r.listen(source)


    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query



def main():
    wishMe()
    while True:
        query=takecommand().lower()
        query_split=query.split()
        if 'open wikipedia' in query:
            webbrowser.open("wikipedia.org")
        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            speak(results)
        elif "open code" in query:
            codepath="C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "open notepad" in query:
            codepath="C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2309.28.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            os.startfile(codepath)
        elif "calculate"in query:
            speak("Please tell me the calculation you want to perform.")
            query = takecommand().lower()
            try:
                result = eval(query)
                speak(f"The result is {result}")
            except Exception as e:
                speak("Sorry, I couldn't understand the calculation. Please try again.")
        elif "joke" in query:
            jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why don't programmers like nature? It has too many bugs.",
            "What do you call 8 hobbits? A hobbyte!"
            ]
            speak(random.choice(jokes))

        elif "open" in query:
            comm=query_split[query_split.index('open')+1 ]
            webbrowser.open(f"{comm}.com")
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'The time is {strTime}')
        elif "the date" in query:
                strDate=datetime.date.today().strftime("%B:%d:%Y")
                speak(f' The date is {strDate}')
        elif "open code" in query:
            codepath="D:\\Jarvis-AI-Assistant\\jarvis.py"
            os.startfile(codepath)
        elif "open notepad" in query:
            codepath="D:\\text1.txt"
            os.startfile(codepath)
        elif "bye" in query:
            speak("Bye, have a great day!")
            exit()
        else:
            speak("Sorry, I didn't understand that. Please try again.")
main()
