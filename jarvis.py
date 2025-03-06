import pyttsx3 #pip install pyttsx3
import pywhatkit
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import time
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        speak("Good Evening!")
        print("Good Evening!")

    print("I am Jarvis ma'am. Please tell me how may I help you")
    speak("I am Jarvis ma'am. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 300  # minimum audio energy to consider for recording

        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login ('amritasinghjadon@gmail.com', 'pythonprograming')
    server.sendmail('amritasinghjadon@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:



        query = takeCommand().lower()
        # print(type(query))

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        # elif 'play music' in query:
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"ma'am, the time is {strTime}")

        elif 'open vs code' in query:

            codePath = "C:\\Users\\asing\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)


        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to ="amritasinghjadon@gmail.com" 
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this message")
        elif 'whatsapp' in query:
            try:
                speak("Tell me the phone number")
                phonenumber = takeCommand()
                speak("What should I say?")
                messege = takeCommand()
                pywhatkit.sendwhatmsg_instantly(f"+91{phonenumber} ",messege )
                speak("Message has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email at this moment")
        elif 'song' in query:
            try:
                speak("Tell me the song name")
                songname = takeCommand()
                pywhatkit.playonyt(songname)
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to play music")
        elif 'topic' in query:
            try:
                speak("Tell me the topic name")
                topic = takeCommand()
                kit.search(topic)
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to Search this topic")
        elif 'text to handwriting' in query:
            try:
                speak("Tell me the text i will convert it into the handwriting image")
                text = takeCommand()
                kit.text_to_handwriting(text,"C:/Users/ASHISH/PycharmProjects/ss.png")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to convert this text to image")

        elif 'shutdown' in query:
            try:
                speak("Thanku for you time")
                exit()
            except Exception as e:
                print(e)
        time.sleep(2)
         