import customtkinter as tk # type: ignore
import VideoDownloader as V
from tkinter import filedialog
import fileorganiser as org
import PDF_merger as mer
import Bday_wish as BD
import web_blocker
import Backup
import healthy_eyes as eyes  


def fun1(): #Youtube video downloader
    V.VIDEO()
def fun2(): #File Organiser
    org.Files_assemble()
def fun3(): #File Backup System
    Backup.backup()
def fun4(): #pdf merger
    mer.merge()
def fun5(): #Birthday wish
    BD.wish()
def fun6(): #Website blocker
    web_blocker.block()
def fun7(): #Healthy eyes
    eyes.Healthy()
tk.set_appearance_mode("system")
tk.set_default_color_theme("dark-blue")


root = tk.CTk()
custom_label = tk.CTkLabel(root, text="Life's Automated", font=("Arial", 50, "bold")).pack()
root.title("Life's Automated")

FF1=tk.CTkFrame(master=root)
FF1.pack(side='top',fill='both',expand=True)
FF2 = tk.CTkFrame(master=root)
FF2.pack(side='bottom', fill='both', expand=True)
#FRAMES
BF1 = tk.CTkFrame(master=FF1)
BF1.pack(side="left", fill='both', expand=True)
BF2 = tk.CTkFrame(master=FF1)
BF2.pack(side="right", fill='both', expand=True)

#Youtube downloader
f1 = tk.CTkFrame(master=BF1 , border_width = 10 , corner_radius =10,border_color = 'white')
f1.pack(fill = 'both' ,expand=True,padx=10,pady=5)
tk.CTkLabel(f1,text="Download Youtube Videos",font=("Arial", 20, "bold")).pack(padx=20,pady=10)
tk.CTkLabel(f1,text="You can download youtube videos\nby pasting their link").pack(pady=10)
tk.CTkButton(f1,text="Open\nDownloader",command=fun1).pack(pady=15)


#File organiser
f2 = tk.CTkFrame(master=BF1 , border_width = 10 , corner_radius =10,border_color = 'white')
f2.pack(fill = 'both' ,expand=True,padx=10,pady=5)
tk.CTkLabel(f2,text = "File Organiser",font=("Arial", 20, "bold")).pack(padx=20,pady=10)
tk.CTkLabel(f2,text="Organise your files by creating\nfolders and subfolders").pack()
tk.CTkButton(f2,text="Open\nOrganizer",command=fun2).pack(pady=20)


#File Backup system
f3 = tk.CTkFrame(master=BF1 , border_width = 10 , corner_radius =10,border_color = 'white')
f3.pack(fill = 'both' ,expand=True,padx=10,pady=5) 
tk.CTkLabel(f3,text="File Backup",font=("Arial", 20, "bold")).pack(padx=20,pady=10)
tk.CTkLabel(f3,text="Keep losing your file\nHave its backup now").pack()
tk.CTkButton(f3,text="Backup Now",command=fun3).pack(pady=20)

#PDF Merger
f4 = tk.CTkFrame(master=BF2 , border_width = 10 , corner_radius =10,border_color = 'white')
f4.pack(fill = 'both' ,expand=True,padx=10,pady=5)
tk.CTkLabel(f4,text="PDF Merger",font=("Arial", 20, "bold")).pack(pady=20)
tk.CTkLabel(f4,text="Do you have so many PDFs\nMerge them all in one :)").pack(padx=20)
tk.CTkButton(f4,text="Merge",command=fun4).pack(pady=20) 


#Birthday wish
f5 = tk.CTkFrame(master=BF2 , border_width = 10 , corner_radius =10,border_color = 'white')
f5.pack(fill = 'both' ,expand=True,padx=10,pady=5)
tk.CTkLabel(f5,text="Birthday wish",font=("Arial", 20, "bold")).pack(pady=10)
tk.CTkLabel(f5,text="Do you want to be the first one\nto wish birthday to your friend").pack(padx=50)
tk.CTkButton(f5,text="Yes",command=fun5).pack(pady=20)

#Website blocker
f6 = tk.CTkFrame(master=BF2 , border_width = 10 , corner_radius =10,border_color = 'white')
f6.pack(fill = 'both' ,expand=True,padx=10,pady=5)
tk.CTkLabel(f6,text="Website Blocker",font=("Arial",20,"bold")).pack(pady=10)
tk.CTkLabel(f6,text="Are you distracted on web?\nBlock it to get productive").pack(padx=50)
tk.CTkButton(f6,text="Block",command=fun6).pack(pady=20)

#Healthy eyes
f7 = tk.CTkFrame(FF2,border_width = 10 , corner_radius =10,border_color = 'white')
f7.pack(side='bottom',fill='y', padx=10, pady=10)
tk.CTkLabel(f7,text="Healthy eyes",font=("Arial",20,"bold")).pack(pady=10)
tk.CTkLabel(f7,text="Is your eyes strained due to screens.\nThen No need to worry because Healthy eyes app will help you out\nClick the Button to proceede.").pack(pady=0,padx=100)
tk.CTkButton(f7,text="Launch app",command=fun7).pack(pady=20)

root.mainloop()

