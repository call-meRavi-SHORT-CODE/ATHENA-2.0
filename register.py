import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
import cv2
from tkinter_webcam import webcam
import os
import pyttsx3 as p
import speech_recognition as sr
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("green")
import multiprocessing
import subprocess

engine = p.init() # to initialize the variable for pyttsx3
rate=engine.getProperty('rate') # to show the rate of the voice
engine.setProperty('rate',170) # to change the rate value
voices=engine.getProperty('voices') # it returns the list two voices
engine.setProperty('voice',voices[1].id) # to get a female voice
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.25)# to change the volumecd

def speak(text):
    engine.say(text)
    engine.runAndWait() #process any pending text-to-speech (TTS) tasks and blocks the program's execution until all the text has been spoken

# Function to capture image from webcam and save it
def capture_image():
    
    cap = cv2.VideoCapture(0)
    
    file_name = mac1.get()
    
    ret, frame = cap.read()
    if ret:
        # Convert frame to PIL Image
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img)

        # Get file name from user input
        file_name = mac1.get()
        
        # Save the captured image
        file_path = os.path.join("captured_images", file_name + ".png")
        img_pil.save(file_path)
        speak("YOUR FACE IS SUCESSFULLY VERIFIED")
        speak("NOW CLICK THE REGISTER BUTTON TO REGISTER")
    cap.release()
    cv2.destroyAllWindows()
def close():
    speak("SUCCESSFULLY REGISTERED")
    app.destroy()
    if __name__ == "__main__":
    # File paths of the Python files to execute
        file1_path = "C://Users//Ravikrishna J//OneDrive//Desktop//Athena//main.py"
        file2_path = "C://Users//Ravikrishna J//OneDrive//Desktop//Athena//main_voice.py"

        # Create subprocesses for each file
        subprocess.Popen(["python", file1_path])
        subprocess.Popen(["python", file2_path])

    
        

# Create tkinter window
app = customtkinter.CTk()
app.title('Login')





# Function to center the window
def center_window(app, width, height):
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    app.geometry('%dx%d+%d+%d' % (width, height, x, y))
    app.resizable(width=False, height=False)

center_window(app, 1000, 500)

# Label for displaying captured image
label_img = customtkinter.CTkLabel(app)
label_img.place(relx=0.0, rely=0.0)

# Frame for webcam feed
webcam_frame = customtkinter.CTkFrame(master=app, width=700, height=700, fg_color='black')
webcam_frame.place(relx=0.0, rely=0.0)


# Load an image
img1 = ImageTk.PhotoImage(Image.open("C://Users//Ravikrishna J//OneDrive//Desktop//Athena//ai.jpg"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.place(relx=0.5, rely=0.0)

# Create custom frame
frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=5, fg_color='#89CFF0')
frame.place(relx=0.20, rely=0.32, anchor=tk.CENTER)

# Label for "Register"
l2 = customtkinter.CTkLabel(master=frame, text="Register", font=('Microsoft Sans Serif', 30), text_color='#000000')
l2.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

mac1=customtkinter.StringVar()
# Entry for username
l2 = customtkinter.CTkLabel(master=frame, text="name", font=('Microsoft Sans Serif', 20), text_color='#000000')
l2.place(relx=0.244, rely=0.255, anchor=tk.CENTER)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username',textvariable=mac1)
entry1.place(x=50, y=110)

# Entry for password
l2 = customtkinter.CTkLabel(master=frame, text="password", font=('Microsoft Sans Serif', 20), text_color='#000000')
l2.place(relx=0.3, rely=0.49, anchor=tk.CENTER)
entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
entry2.place(x=50, y=200)

# Create custom button for login
button1 = customtkinter.CTkButton(master=frame, width=180, text="Register", command=close, corner_radius=6)
button1.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def cameron():
    speak("  TURNING ON YOUR CAMERA ")
    speak("PLEASE WAIT..")
   

    video = webcam.Box(webcam_frame, width=740, height=650)
    video.show_frames()
       
    



button1 = customtkinter.CTkButton(master=app, width=150, text="Turn On", command=cameron, corner_radius=6)
button1.place(relx=0.15, rely=0.93, anchor=tk.CENTER)

button1 = customtkinter.CTkButton(master=app, width=150, text="Verify", command=capture_image, corner_radius=6)
button1.place(relx=0.35, rely=0.93, anchor=tk.CENTER)










os.makedirs("captured_images", exist_ok=True)

# Run GUI loop
app.mainloop()

