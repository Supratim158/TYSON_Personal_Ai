import time
import pyttsx3
import eel
import speech_recognition as sr

def speak(text):
    # text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 200)
    eel.DisplayMessage(text)
    engine.say(text)
    # eel.receiverText(text)
    engine.runAndWait()
    
def takecommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)
        
    try:
        print('Rcognizing')
        eel.DisplayMessage('Rcognizing....')
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User Said : {query}")
        eel.DisplayMessage(query)
        # speak(query)
    
        
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose 
def allCommands():
    
    try:
        query = takecommand()
        print(query)
        
        if "open" in query:
            from backend.features import openCommand
            openCommand(query)
            
        elif "on youtube":
            from backend.features import PlayYoutube
            PlayYoutube(query)
            
        else:
            print("not run")
            
            
    except:
        print("Error")
    eel.ShowHood()
    
