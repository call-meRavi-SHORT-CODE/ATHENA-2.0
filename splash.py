from tkinter import * 
from PIL import Image
from tkinter import ttk
import tkinter.messagebox
import customtkinter as ct

import multiprocessing
import subprocess



ct.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
splash= ct.CTk()
splash.title("This is splash screen")
splash.geometry('620x350+420+200')

splash.wm_overrideredirect(True)


my_font1 = ct.CTkFont(family="Microsoft Sans Serif", size=30)
my_font2 = ct.CTkFont(family="Microsoft Sans Serif", size=20)
my_font3 = ct.CTkFont(family="Microsoft Sans Serif", size=15)

label4 = ct.CTkLabel(master=splash, text="Introducing Your AI Companion",width=50,
                        font=my_font1,
                        height=12,               
                        text_color=('white'),

                        padx=2,pady=6)
label4.place(x=0,y=30,relwidth=1)
label4 = ct.CTkLabel(master=splash, text="Redefining Possiblities...",width=50,
                        font=my_font2, 
                        height=12,               
                         text_color=('white'),

                         padx=2,pady=6)
label4.place(x=150,y=90,relwidth=1)

def loading():
    label4 = ct.CTkLabel(master=splash, text="Loading...",width=50,
                        font=my_font3,
                        height=12,               
                         text_color=('#e6e6e6'),

                         padx=2,pady=6)
    label4.place(relx=0.5,rely=0.8, anchor=tkinter.CENTER)

    progress=ct.CTkProgressBar(splash, orientation="horizontal",width=500,height=10,progress_color="grey",determinate_speed=0.1)
    progress.place(relx=0.5,rely=0.9, anchor=tkinter.CENTER)
    progress.configure(mode="determinate")
    progress.start()
    splash.after(3000,next)

button= ct.CTkButton(master=splash,border_color='white',width=210, text="Get Started ...",command=loading,font=my_font2 ,fg_color=("#008000"),hover=None,text_color=("white"))
button.place(x=40,y=210)
def next():
    splash.destroy()
    if __name__ == "__main__":
    # File paths of the Python files to execute
        file1_path = "C://Users//Ravikrishna J//OneDrive//Desktop//Athena//landing.py"
        file2_path = "C://Users//Ravikrishna J//OneDrive//Desktop//Athena//intovoice.py"

        # Create subprocesses for each file
        subprocess.Popen(["python", file1_path])
        subprocess.Popen(["python", file2_path])

        
    


    
        
        
    
splash.mainloop()


