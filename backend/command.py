import time
import pyttsx3
import eel
import speech_recognition as sr



def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 200)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
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
def allCommands(message = 1):
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
        
    else:
        query = message
        eel.senderText(query)
    
    try:
        
        if "open" in query:
            from backend.features import openCommand
            openCommand(query)
            
        elif "on youtube" in query:
            from backend.features import PlayYoutube
            PlayYoutube(query)
            
            
        elif "send message" in query or "phone call" in query or "video call" in query:
            from backend.features import findContact, whatsApp, makeCall,sendMessage
            contact_no, name = findContact(query)
            if(contact_no != 0):
                speak("Which mode you want to use whatsapp or mobile")
                preferance = takecommand()
                print(preferance)

                if "mobile" in preferance:
                    if "send message" in query or "send sms" in query: 
                        speak("what message to send")
                        message = takecommand()
                        sendMessage(message, contact_no, name)
                    elif "phone call" in query:
                        makeCall(name, contact_no)
                    else:
                        speak("please try again")
                elif "whatsapp" in preferance:
                    message = ""
                    if "send message" in query:
                        message = 'message'
                        speak("what message to send")
                        query = takecommand()
                                        
                    elif "phone call" in query:
                        message = 'call'
                    else:
                        message = 'video call'
                                        
                    whatsApp(contact_no, query, message, name)
                    
        elif "click photo" in query.lower() or "take photo" in query.lower() or "take a picture" in query.lower():
            from backend.features import clickPhoto
            clickPhoto()
            
        elif "take video" in query.lower():
            from backend.features import takeVideo
            takeVideo()

        else:
            from backend.features import chatBot
            chatBot(query)
            
    except:
        print("Error")
    eel.ShowHood()
    
