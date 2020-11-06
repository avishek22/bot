import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Eveving!")
    speak("How may I help your sir?")


def takeCommand():  # It takes microphone input from user and give's string value.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        speak("Listening..")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        r.energy_threshold = 600  # for noisy background environment.
        audio = r.listen(source)

        try:
            print("Recognizing..")
            speak("Recognizing..")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")

        except Exception as e:
           # print(e)
            print("Say that again Please.")
            speak("Say that again Please.")
            query = "None"
        return query


if __name__ == "__main__":
    wish()
    # speak("avishek is good")
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {time}")
            speak(f"Sir, the time is {time}")
        elif 'open code' in query:
            path = ""
            os.startfile(path)
