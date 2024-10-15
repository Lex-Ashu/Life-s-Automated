import customtkinter as tk,pytube,os # type: ignore
from tkinter import ttk
from tkinter import messagebox , filedialog

def VIDEO():
    def get_video_size():
        url = url_entry.get()
        Reso = quality_menu.get()
        try:
            yt = pytube.YouTube(url)
            streams = yt.streams.filter(res=Reso)
            if len(streams) > 0:
                stream = streams[0]
                size = stream.filesize / (1024 * 1024)  # Convert to MB
                size_label.configure(text=f"Video Size: {size:.2f} MB")
            else:
                size_label.configure(text=f"No matching stream found\nfor the selected resolution.")
        except pytube.exceptions.RegexMatchError:
            size_label.configure(text="Invalid URL or no stream found")
        except Exception as e:
            size_label.configure(text=str(e))

    def download_video():
            url = url_entry.get()
            Reso = quality_menu.get()
            try:
                yt = pytube.YouTube(url)
                streams = yt.streams.filter(res=Reso , progressive=True)
                if len(streams) > 0:
                    stream = streams[0]
                    stream.download()
                    messagebox.showinfo("Success", "Video downloaded successfully.")
                else:
                    messagebox.showerror("Error", "No matching stream found for the selected resolution.")
            except pytube.exceptions.RegexMatchError:
                messagebox.showerror("Error", "Invalid URL or no stream found")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def browse_directory():
        # Open a directory dialog to choose the download location
            download_path = filedialog.askdirectory()
            os.chdir(download_path)
            text1 = "Video Save location:\n"+download_path
            Location_Label.configure(text=text1)

    def title():
            url = url_entry.get()
            try:
                yt = pytube.YouTube(url)
                video_title = yt.title
                print(video_title)
                messagebox.showinfo("Title",video_title)

            except pytube.exceptions.RegexMatchError:
                messagebox.showerror("Error", "Invalid URL or no stream found")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    os.chdir('/Users/ashuchoudhary/Downloads')     #Change this file location to your downloads folder 
    tk.set_appearance_mode("system")
    tk.set_default_color_theme("dark-blue")
    root = tk.CTk()
    root.title("Youtube Video Downloader")
    root.geometry("350x450")
    
    root.resizable(False,False)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - root.winfo_reqwidth()) / 2
    y_coordinate = (screen_height - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x_coordinate, y_coordinate))

    url_label = tk.CTkLabel(root, text="Enter YouTube URL:",font=('Helvetica', 18))
    url_label.pack(pady=10)
    url_entry = tk.CTkEntry(root, width=300,font=('Helvetica', 18))
    url_entry.pack(pady = 10)

    quality_var = tk.StringVar()
    quality_var.set("Select video quality")
    quality_menu = ttk.Combobox(root,textvariable=quality_var, values=["2160p","1440p","1080p", "720p","480p", "360p","240p","144p"], font=('Helvetica', 14),state="readonly")
    quality_menu.pack(pady=10)
    quality_menu.configure(font=('Helvetica', 18))

    tit_but = tk.CTkButton(root,text='Get Title',command=title,font=('Helvetica', 18))
    tit_but.pack(padx =10,pady=20)

    get_size_button = tk.CTkButton(root, text="Get Video Size", command=get_video_size,font=('Helvetica', 18))
    get_size_button.pack()

    size_label = tk.CTkLabel(root, text="",font=('Helvetica', 18))
    size_label.pack(pady=10)

    DEF = 'Downloads'
    Location_Label = tk.CTkLabel(root,text="Default Save location:"+DEF,font=('Helvetica', 18))
    Location_Label.pack(pady=5)
    browse_button = tk.CTkButton(root, text="Browse save location", command=browse_directory,font=('Helvetica', 18))
    browse_button.pack(pady=10)

    download_button = tk.CTkButton(root, text="Download Video", command=download_video,font=('Helvetica', 18))
    download_button.pack(pady=10)

    root.mainloop()
