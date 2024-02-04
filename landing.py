from tkinter import * 
from tkinter import ttk
import tkinter.messagebox
import customtkinter as ct
import pyttsx3 as p
import speech_recognition as sr
import multiprocessing
import subprocess

def register():
    land.destroy()
    if __name__ == "__main__":
    # File paths of the Python files to execute
        file1_path = "C://Users//Ravikrishna J//OneDrive//Desktop//Athena//register.py"
        file2_path = "C://Users//Ravikrishna J//OneDrive//Desktop//Athena//regvoice.py"

        # Create subprocesses for each file
        subprocess.Popen(["python", file1_path])
        subprocess.Popen(["python", file2_path])

        print("Both files executed successfully.")
    


ct.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
land= ct.CTk(fg_color="#28282B")
def center_window(land, width, height):
    screen_width = land.winfo_screenwidth()
    screen_height = land.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    land.geometry('%dx%d+%d+%d' % (width, height, x, y))
    land.resizable(width=False,height=False)
center_window(land, 1000,500)



land.title("ATHENA 2.0")

my_font1 = ct.CTkFont(family="Microsoft Sans Serif", size=30)
my_font3 = ct.CTkFont(family="Microsoft Sans Serif", size=18)
my_font2 = ct.CTkFont(family="Microsoft Sans Serif", size=15)

title=ct.CTkFrame(land,width=1500,height=350,border_width=3,fg_color='black',border_color='black',corner_radius=5)
title.pack(pady=0,ipady=10)

text_var = tkinter.StringVar(value="ATHENA 2.0 ")

label = ct.CTkLabel(master=title,
                               textvariable=text_var,
                               width=400,
                               height=23,
                               fg_color=("white", "black"),
                               font=my_font1,
                               corner_radius=8)
label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
button= ct.CTkButton(master=title,border_color='#B1D4E0',width=80, text="ABOUT",
                     font=my_font2,command=None,fg_color=("black"),hover=None,text_color=("#B1D4E0"),
                     border_width=1)
button.place(relx=0.15, rely=0.3, anchor=tkinter.CENTER)

button= ct.CTkButton(master=title,border_color='#A020F0',width=80, text="Help",
                     font=my_font2,command=None,fg_color=("black"),hover=None,text_color=("#B1D4E0"),
                     border_width=1)
button.place(relx=0.93, rely=0.1, anchor=tkinter.CENTER)

title1=ct.CTkFrame(title,width=500,height=180,border_width=1,fg_color='black',border_color='#B1D4E0',corner_radius=5)
title1.place(relx=0.35, rely=0.65, anchor=tkinter.CENTER)
#1
label4 = ct.CTkLabel(master=title1, text=" Hi, I am ATHENA 2.0 an advanced AI Assisant.",width=50,
                        font=my_font2, 
                        height=12,               
                        text_color=('#B1D4E0'),

                         padx=2,pady=6)
label4.place(relx=0.35, rely=0.2, anchor=tkinter.CENTER)
#2
label4 = ct.CTkLabel(master=title1, text="Powered by cutting-edge AI technology.",width=50,
                        font=my_font2, 
                        height=12,               
                         text_color=('#B1D4E0'),

                         padx=2,pady=6)
label4.place(relx=0.3, rely=0.4, anchor=tkinter.CENTER)
#3
label4 = ct.CTkLabel(master=title1, text="seamlessly integrates into your daily routine,",width=50,
                        font=my_font2, 
                        height=12,               
                         text_color=('#B1D4E0'),

                         padx=2,pady=6)
label4.place(relx=0.33, rely=0.6, anchor=tkinter.CENTER)
#4
label4 = ct.CTkLabel(master=title1, text="becoming your trusted aide in navigating the complexities of modern life.",width=50,
                        font=my_font2, 
                        height=12,               
                         text_color=('#B1D4E0'),

                         padx=2,pady=6)
label4.place(relx=0.51, rely=0.8, anchor=tkinter.CENTER)












# second part
text_var = tkinter.StringVar(value="New User ?")
label = ct.CTkLabel(master=land,
                               textvariable=text_var,
                               width=80,
                               height=30,
                               
                               font=my_font3,
                               corner_radius=8)
label.place(relx=0.35, rely=0.78, anchor=tkinter.CENTER)
button= ct.CTkButton(master=land,border_color='white',width=130, text="Register",
                     command=register,font=my_font3 ,fg_color=("#008000"),hover=None,text_color=("white"))
button.place(relx=0.35, rely=0.85, anchor=tkinter.CENTER)


text_var = tkinter.StringVar(value="Already Registered ?")
label = ct.CTkLabel(master=land,
                               textvariable=text_var,
                               width=80,
                               height=30,
                               
                               font=my_font3,
                               corner_radius=8)
label.place(relx=0.64, rely=0.78, anchor=tkinter.CENTER)
button= ct.CTkButton(master=land,border_color='#008000',width=130, text="Login",
                     command=None,font=my_font3 ,border_width=1,fg_color="#28282B",hover=None,text_color=("#008000"))
button.place(relx=0.64, rely=0.85, anchor=tkinter.CENTER)



label4 = ct.CTkLabel(master=land, text='\u00A9 2024 AI Powered Assistant | Designed by Ravikrishna',width=1000,
                        font=my_font2, 
                        height=15,               
                         text_color=('white'),
                        fg_color="black",

                         padx=2,pady=6)
label4.place(relx=0.5, rely=0.98, anchor=tkinter.CENTER)



# speech part


land.mainloop()