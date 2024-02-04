engine = p.init() # to initialize the variable for pyttsx3
rate=engine.getProperty('rate') # to show the rate of the voice
engine.setProperty('rate',180) # to change the rate value
voices=engine.getProperty('voices') # it returns the list two voices
engine.setProperty('voice',voices[1].id) # to get a female voice
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.25)# to change the volumecd

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Night!")
    speak("What can I do now")

wish()