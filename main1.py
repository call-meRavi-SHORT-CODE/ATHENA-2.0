import pyttsx3 as p
import speech_recognition as sr 
import datetime
import webbrowser
import wikipedia
import pywhatkit as wk
import os

engine = p.init("sapi5") # to initialize the variable for pyttsx3
rate=engine.getProperty('rate') # to show the rate of the voice
engine.setProperty('rate',180) # to change the rate value
voices=engine.getProperty('voices') # it returns the list two voices
engine.setProperty('voice',voices[1].id) # to get a female voice
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.25)# to change the volume

def speak(text):
    engine.say(text)
    engine.runAndWait()



def command (query):
    
    wish()
    while True:
        query = takecommand()
        if query is not None and query.strip():  # Check if query is not empty
            query = query.lower()
            if "athena" in query:
                say("YES SIR...")
            elif "what is" in query:
                speak("searching.....")
                query=query.replace("what is","")
                results=wikipedia.summary(query,sentence=2)
                speak("According to wikipedia")    
                speak(results)    

            elif "who is" in query:
                speak("searching.....")
                query=query.replace("who is","")
                results=wikipedia.summary(query,sentence=2)
                speak("According to wikipedia")    
                speak(results) 

            elif "just open google" in query:
                webbrowser.open('google.com')

            elif 'open google' in query:
                speak("what should I search ?")
                q=takecommand().lower()
                webbrowser.open(f'{q}')
                search=wikipedia.summary(q,sentence=1)  
                speak(results)

            elif "just open youtube" in query:
                webbrowser.open('youtube.com')
            
            elif "open youtube" in query:
                speak("what you like to watch ?")
                q=takecommand().lower()
                wk.playony(f'{query}')
            
            elif "search on youtube" in query:
                query=query.replace("search on youtube","")
                webbrowser.open(f"www.youtube.com/results?search_query={query}")
            
            elif 'close browser' in query:
                os.system('taskkill /f /im msedge.exe')

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Night!")
    speak("What can I do now")

def takecommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        """label4 = customtkinter.CTkLabel(master=frame, text="Listening...",width=80,height=20,               
                         text_color=('white'),font=('Microsoft Sans Serif', 25))

                        
        label4.place(relx=0.5, rely=0.54, anchor=tk.CENTER)
        def destroy_label():
            label4.destroy()
        window.after(2000, destroy_label)"""
        
        speak("Listening...")
        recognizer.pause_threshold=1
        audio = recognizer.listen(source)

    try:
        
        
        text1 = recognizer.recognize_google(audio)
        '''label4 = customtkinter.CTkLabel(master=frame, text=text1,width=80,height=20,               
                         text_color=('white'),font=('Microsoft Sans Serif', 25))

                        
        label4.place(relx=0.5, rely=0.54, anchor=tk.CENTER)
        label4.destroy()'''

        return text1
        
        
        
    except sr.UnknownValueError:
        """label4 = customtkinter.CTkLabel(master=frame, text="Sorry, I couldn't understand.",width=80,height=20,               
                         text_color=('white'),font=('Microsoft Sans Serif', 25))

                        
        label4.place(relx=0.5, rely=0.54, anchor=tk.CENTER)"""
        speak("Sorry, I couldn't understand.")
        #label4.destroy()
        return None



        

"""elif 'open google' in command:
        speak("what should I search ?")
        q=takecommand().lower()
        webbrowser.open(f'{q}')
        search=wikipedia.summary(q,sentence=1)  
        speak(results)"""

elif " open notepad" in command.lower():
        label4 = customtkinter.CTkLabel(master=frame, text="opening Notepad...",width=80,height=20,               
                         text_color=('white'),font=('Microsoft Sans Serif', 25))

                        
        label4.place(relx=0.5, rely=0.54, anchor=tk.CENTER)
        def destroy_label():
            label4.destroy()
        window.after(2000, destroy_label)
        speak("opening Notepad...")
        
        os.system("start notepad")
        label4.destroy()
    elif " open calculator" in command.lower():
        label4 = customtkinter.CTkLabel(master=frame, text="opening calculator...",width=80,height=20,               
                         text_color=('white'),font=('Microsoft Sans Serif', 25))

                        
        label4.place(relx=0.5, rely=0.54, anchor=tk.CENTER)
        speak("opening Calculator...")
        
        def destroy_label():
            label4.destroy()
        window.after(2000, destroy_label)
        os.system("start calc")
       
    elif "open file explorer" in command.lower():
        label4 = customtkinter.CTkLabel(master=frame, text="opening file explorer...",width=80,height=20,               
                         text_color=('white'),font=('Microsoft Sans Serif', 25))

                        
        label4.place(relx=0.5, rely=0.54, anchor=tk.CENTER)
        speak("opening file explorer...")
        
