 # Change this to your video file
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import customtkinter
import os
import speech_recognition as sr
import pyttsx3 as p
import webbrowser
import datetime
import wikipedia
import pywhatkit as wk
import pygame
import pyautogui
import wmi # adjusting brightness
import requests
from bs4 import BeautifulSoup
import time
import brightness


def play_video():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (1502, 752))  # Resize the frame to 1000x500
        photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        canvas.create_image(0, 0, image=photo, anchor=tk.NW)
        canvas.photo = photo  # Prevent garbage collection
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset video to start
    window.after(5,play_video)  



customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
window= customtkinter.CTk()
window.title("ATHENA 2.0")


def center_window(land, width, height):
    screen_width = land.winfo_screenwidth()
    screen_height = land.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    land.geometry('%dx%d+%d+%d' % (width, height, x, y))
    land.resizable(width=False,height=False)
center_window(window, 1000, 500)

video_source = "C://Users//Ravikrishna J//OneDrive//Desktop//Athena//ai.mp4"   # Change this to your video file
cap = cv2.VideoCapture(video_source)

canvas = tk.Canvas(window, width=1500, height=750)
canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

play_video()



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

def execute_command(command):
    def write():
            speak("speak now")
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                audio = recognizer.listen(source)

            try:
                text1 = recognizer.recognize_google(audio)
                pyautogui.write(text1)
                speak("written successfully")
            except sr.UnknownValueError:
                speak("Sorry, I couldn't understand.")

    

    
    if "athena" in command:
        textbox.insert("0.0",f"Athena <-- yes sir {query} \n","end")
        speak("YES SIR...")
        speak("how can i help you sir ")
    
        
        

    
    elif "search" in command:
        
        query=command.replace("search","")
        speak(f"searching {query} on google")
        textbox.insert("0.0",f"Athena <-- searching {query} \n","end")
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting search result summaries
        search_results = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")
        summaries = [result.text for result in search_results]

    # Concatenate the summaries
        summary = " ".join(summaries[3])  # Consider the first 3 search results
    
    # Speak out the summary
        speak(summary)
        
        
        speak("According to google")    
           

    
    elif "open google" in command:
        webbrowser.open('google.com')
        textbox.insert("0.0",f"Athena <-- opening google... \n","end")
        speak("Opening google..")

    

    elif "just open youtube" in command:
        webbrowser.open('youtube.com')
            
    
        
            
    elif "play on youtube" in command:
        query=command.replace("play on youtube","")
        speak(f"playing {query} on youtube")
        textbox.insert("0.0",f"Athena <-- playing {query} on youtube... \n","end")
        wk.playonyt(query)
            
    elif 'close browser' in command:
        textbox.insert("0.0",f"Athena <-- close brower \n","end")
        speak(f"closing browser")
        os.system('taskkill /f /im msedge.exe')    
        
   
    elif "open notepad" in command.lower():
        textbox.insert("0.0",f"Athena <-- opening notepad... \n","end")
        speak("Opening notepad..")
        os.system("start notepad")
    elif "open calculator" in command.lower():
        textbox.insert("0.0",f"Athena <-- opening calculator... \n","end")
        speak("Opening calculator..")
        os.system("start calc")
    
    elif "file explorer" in command.lower():
        textbox.insert("0.0",f"Athena <-- opening file explorer... \n","end")
        speak("Opening file explorer..")
        os.system("start explorer")    
   

    elif "open settings" in command.lower():
        textbox.insert("0.0", f"Athena <-- opening Settings... \n", "end")
        speak("Opening Settings..")
        os.system("start ms-settings:")

    elif "open task manager" in command.lower():
        textbox.insert("0.0", f"Athena <-- opening Task Manager... \n", "end")
        speak("Opening Task Manager..")
        os.system("taskmgr")

    elif "open microsoft store" in command.lower():
        textbox.insert("0.0", f"Athena <-- opening Microsoft Store... \n", "end")
        speak("Opening Microsoft Store..")
        os.system("start ms-store:")

    elif "open word" in command.lower():
        textbox.insert("0.0", f"Athena <-- opening Microsoft Word... \n", "end")
        speak("Opening Microsoft Word..")
        os.system("start winword")

    elif "open ppt" in command.lower():
        textbox.insert("0.0", f"Athena <-- opening PowerPoint... \n", "end")
        speak("Opening PowerPoint..")
        os.system("start powerpnt")

    elif "open excel" in command.lower():
        textbox.insert("0.0", f"Athena <-- opening Excel... \n", "end")
        speak("Opening Excel..")
        os.system("start excel")
    
    

    elif "write on notepad" in command.lower():
        textbox.insert("0.0", f"Athena <-- opening Notepad... \n", "end")
        speak("Opening Notepad..")
        os.system("start notepad")
        # Wait for Notepad to open
        pyautogui.sleep(2)
        write()

    elif "write on word" in command.lower():
        textbox.insert("0.0", f"Athena <-- opening word document... \n", "end")
        speak("Opening word document..")
        os.system("start winword")
        # Wait for Notepad to open
        pyautogui.sleep(2)
        write()

    elif "write on cmd" in command.lower():
        textbox.insert("0.0", f"Athena <-- opening command prompt... \n", "end")
        speak("Opening command prompt..")
        os.system("start cmd")
        # Wait for Notepad to open
        pyautogui.sleep(2)
        write()

    elif "set brightness to " in command.lower():
        query=command.replace("set brightness to","")
        def set_brightness(brightness_level):
            speak(f"setting brightness to  {query}")
            textbox.insert("0.0", f"Athena <-- setting brightness to  {query}", "end")
            c = wmi.WMI(namespace='wmi')
            methods = c.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(brightness_level, 0)


        set_brightness(query)

    elif "close word" in command.lower():
        textbox.insert("0.0", "Athena <-- Closing Microsoft Word...\n", "end")
        speak("Closing Microsoft Word..")
        os.system('taskkill /f /im winword.exe')

    elif "close excel" in command.lower():
        textbox.insert("0.0", "Athena <-- Closing Microsoft Excel...\n", "end")
        speak("Closing Microsoft Excel..")
        os.system('taskkill /f /im excel.exe')
    elif "close powerpoint" in command.lower():
        textbox.insert("0.0", "Athena <-- Closing Microsoft PowerPoint...\n", "end")
        speak("Closing Microsoft PowerPoint..")
        os.system('taskkill /f /im powerpnt.exe')

    elif "close settings" in command.lower():
        textbox.insert("0.0", "Athena <-- Closing Settings...\n", "end")
        speak("Closing Settings..")
        os.system('taskkill /f /im SystemSettings.exe')
    elif "close store" in command.lower():
        textbox.insert("0.0", "Athena <-- Closing Microsoft Store...\n", "end")
        speak("Closing Microsoft Store..")
        os.system('taskkill /f /im WinStore.App.exe')
    

    elif "restart" in command.lower():
        textbox.insert("0.0", "Athena <-- Restarting the system...\n", "end")
        speak("Restarting the system..")
        os.system("shutdown /r /t 1")

    elif "sleep" in command.lower():
        textbox.insert("0.0", "Athena <-- Putting the system to sleep...\n", "end")
        speak("Putting the system to sleep..")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    
    elif "take screenshot as" in command.lower():
        query=command.replace("take screenshot as","")
        
        time.sleep(3)
        ima=pyautogui.screenshot()
        ima.save(f'{query}.png')
        textbox.insert("0.0", "Athena <-- screenshot saved...\n", "end")
        speak("screenshot saved")
    
    elif "volume up" in command.lower():
        textbox.insert("0.0", "Athena <-- volume increased...\n", "end")
        speak("volume increaded")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        
    
    elif "volume down" in command.lower():
        textbox.insert("0.0", "Athena <-- volume increased...\n", "end")
        speak("volume increaded")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif "mute" or "muted" in command.lower():
        pyautogui.press("volumemute")

    else:
        speak("Application not recognized")
        textbox.insert("0.0",f"Athena <-- could not open \n","end")

        



    
        
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Night!")
    speak("What can I do now")

def on_click():
    command = entry1.get()
    if command:
        execute_command(command)
        textbox.insert("0.0",f"Me --> {command} \n","end")
        entry1.delete(0, tk.END)
        
    else:
        speak("could not understand")

def voice_command():
    command = recognize_speech()
    if command:
        execute_command(command)
        
    else:
        speak("could not understand")

def takecommand():
    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        audio = recognizer.listen(source)

    try:
        
        
        text1 = recognizer.recognize_google(audio)
        label4 = customtkinter.CTkLabel(master=frame, text=text1,width=80,height=20,               
                         text_color=('white'),font=('Microsoft Sans Serif', 25))

                        
        label4.place(relx=0.5, rely=0.54, anchor=tk.CENTER)
        def destroy_label():
            label4.destroy()
        window.after(2000, destroy_label)
        textbox.insert("0.0", f'=> {text1}')
        execute_command(text1)

        
        
        
        
    except sr.UnknownValueError:
        """label4 = customtkinter.CTkLabel(master=frame, text="Sorry, I couldn't understand.",width=80,height=20,               
                         text_color=('white'),font=('Microsoft Sans Serif', 25))

                        
        label4.place(relx=0.5, rely=0.54, anchor=tk.CENTER)"""
        speak("Sorry, I couldn't understand.")
        #label4.destroy()
        return None





       






frame = customtkinter.CTkFrame(master=window, width=350, height=420, corner_radius=5, fg_color="black")
frame.place(relx=0.75, rely=0.5, anchor=tk.CENTER)




mac1=customtkinter.StringVar()

entry1 = customtkinter.CTkEntry(master=frame,height=30, width=200,textvariable=mac1,corner_radius=200,fg_color="white",border_color="white",text_color="black",font=('Microsoft Sans Serif', 15))
entry1.place(relx=0.4, rely=0.9, anchor=tk.CENTER)
entry1.icursor("insert")


image = Image.open('C://Users//Ravikrishna J//OneDrive//Desktop//Athena//send.png')
python_image = ImageTk.PhotoImage(image)

image2 = Image.open('C://Users//Ravikrishna J//OneDrive//Desktop//Athena//delete.png')
python_image2 = ImageTk.PhotoImage(image2)


image1= Image.open('C://Users//Ravikrishna J//OneDrive//Desktop//Athena//mic.png')
python_image1= ImageTk.PhotoImage(image1)


button1 = customtkinter.CTkButton(master=frame,text="", width=40,image=python_image, command=on_click, corner_radius=200,fg_color="black",text_color="white",hover=None)
button1.place(relx=0.78, rely=0.9, anchor=tk.CENTER)
def delete():
    textbox.delete("0.0", "end") 
button1 = customtkinter.CTkButton(master=frame,text="", width=50,height=20,image=python_image2, command=delete, corner_radius=200,fg_color="black",text_color="white",hover=None)
button1.place(relx=0.9, rely=0.9, anchor=tk.CENTER)


button1 = customtkinter.CTkButton(master=frame,border_color="grey",text="", width=50,image=python_image1, command=takecommand, corner_radius=1000,fg_color="black",text_color="white",hover=None)
button1.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

textbox = customtkinter.CTkTextbox(frame,font=('Microsoft Sans Serif', 15),text_color="black", width=300)

textbox.place(relx=0.5, rely=0.3, anchor=tk.CENTER)



window.mainloop()

# Release the video capture when the window is closed
cap.release()





