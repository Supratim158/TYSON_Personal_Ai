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
            
        elif "on youtube" in query:
            from backend.features import PlayYoutube
            PlayYoutube(query)
            
            
        elif "send message" in query or "phone call" in query or "video call" in query:
            from backend.features import findContact, whatsApp
            message=""
            contact_no, name = findContact(query)
            if(contact_no != 0):
                # speak("Which mode you want to use whatsapp or mobile")
                # preferance = takecommand()
                # print(preferance)

                # if "mobile" in query:
                    if "send message" in query : 
                        speak("what message to send")
                        message = 'message'
                        query = takecommand()
                    elif "phone call" in query:
                        message = 'call'
                    else:
                        message = 'video call'
                                        
                    whatsApp(contact_no, query, message, name)
                    #     sendMessage(message, contact_no, name)
                    # elif "phone call" in query:
                    #     makeCall(name, contact_no)
                    # else:
                    #     speak("please try again")
                # elif "whatsapp" in query:
                #     message = ""
                #     if "send message" in query:
                #         message = 'message'
                #         speak("what message to send")
                #         query = takecommand()
                                        
                    # elif "phone call" in query:
                    #     message = 'call'
                    # else:
                    #     message = 'video call'
                                        
                    # whatsApp(contact_no, query, message, name)

        else:
            print("not run")
            
            
    except:
        print("Error")
    eel.ShowHood()
    
