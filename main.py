import os
import eel

from backend.features import *
from backend.command import *
from backend.auth import recoganize


def start():
    eel.init('frontend')

    playAssistantSound()
    
    @eel.expose
    def init():
        subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak("Ready For Face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag ==1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello ,I am TYSON ur AI assistant")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Failed")
    

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode = None, host = 'localhost', block = True )
