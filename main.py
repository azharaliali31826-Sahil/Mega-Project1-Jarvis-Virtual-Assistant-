import speech_recognition as sr
import webbrowser
import pyttsx3

# pip install PocketSphinx

recognizer=sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
   
    if"open google" in c.lower():
       webbrowser.open("https://www.google.com")
    elif "open chat" in c.lower():
       webbrowser.open("https://www.chatgpt.com") 
    elif "open youtube" in c.lower():
       webbrowser.open("https://www.youtube.com")
    elif "open naukri" in c.lower():
       webbrowser.open("https://www.naukri.com")
    
if __name__=="__main__":
    speak("Initializing Jarvis.....")
    while True:
        # Listen for the wake word "Jarvis"
        # Obtain audio from the microphone
        r=sr.Recognizer()
        

        
        print("recognizing...") 
        try:
            with sr.Microphone() as sourse:
             print("Listening...")
             audio=r.listen(sourse,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Ya")
                # Listen for command 
                with sr.Microphone() as sourse:
                 print("jarvis Active...")
                 audio=r.listen(sourse)
                 command=r.recognize_google(audio)

                 processCommand(command)


        except Exception as e :
            print("Error; {0}",format(e))  
        


