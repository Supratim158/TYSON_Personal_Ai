from playsound import playsound
import eel


# Playing Assistant sound func
@eel.expose
def playAssistantSound():
    music_dir = "frontend\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)