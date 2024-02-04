import pyttsx3 as p
import speech_recognition as sr
def intro():
    engine = p.init() # to initialize the variable for pyttsx3
    rate=engine.getProperty('rate') # to show the rate of the voice
    engine.setProperty('rate',180) # to change the rate value
    voices=engine.getProperty('voices') # it returns the list two voices
    engine.setProperty('voice',voices[1].id) # to get a female voice
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume+0.25)# to change the volumecd

    def speak(text):
        engine.say(text)
        engine.runAndWait() #process any pending text-to-speech (TTS) tasks and blocks the program's execution until all the text has been spoken

    r= sr.Recognizer()# it is instance help us to retrieve information from the source(microphone)

    speak(" WELCOME To 'ATHENA' 2.0 World...")
    #speech_to_text(takes the audio from the microphone and coverts the audio into text using google API)
    speak("I am your Personal Desktop Assistant....")
    speak("Powered by Cutting Edge AI Technology.....")
    speak("If you already Have an account click the LOGIN button...")
    speak("OR Click On REGISTER BUTTON to register your self....")
    speak("TO know more about me Click 'ABOUT'  BUTTON...")

intro()
    
        
    

    
           
        

