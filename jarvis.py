import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
# Initializing text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use the first voice in the list

# Function to make the engine speak a given text
def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to announce the current time in AM/PM format
def current_time():
    Speak("Fredrick Fredrick, wake up and stop sleeping")
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    Speak(f"The current time is {current_time}")

# Function to get a summary from Wikipedia,3 sentence longs
def wiki():
    query = "iPhone"
    results = wikipedia.summary(query, sentences=3)
    print(results)
    Speak("According to Wikipedia")
    Speak(results)
    
    # Function to send a Command via microphone
def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
    except Exception as e:
        print("Could not understand audio. Please say that again.")
        print(f"Error: {e}")
        return None
    return query

    
# Main function to execute the tasks
if __name__ == "__main__":
    current_time()
    wiki()
    TakeCommand()
