import os,shutil,customtkinter as tk # type: ignore
from tkinter import messagebox,filedialog
from datetime import datetime

def backup():
    def browse():
        file = filedialog.askdirectory()
        source_path.delete(0, tk.END) 
        source_path.insert(0, file)  

    def backup():
        path = source_path.get()
        if not os.path.exists(path):
            messagebox.showerror("Error", "Invalid source directory path.")
            return
        destination_path = "C:/Backups"
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        try:
            shutil.copytree(path, os.path.join(destination_path, os.path.basename(path)))
            log_file_path = os.path.join(destination_path, "backup_log.txt")
            log_message = f"{datetime.now()}   ---   Backup of {path}.\n"
            if not os.path.exists(log_file_path):
                with open(log_file_path, "w"): 
                    pass
            with open(log_file_path, "a") as log_file:
                log_file.write(log_message)
            messagebox.showinfo("Backup", "Backup successful.")
        except Exception as e:
            messagebox.showerror("Error", f"Error during backup: {str(e)}")

    def open_folder():
        destination_path = "C:/Backups"
        os.startfile(destination_path)


    root = tk.CTk()
    root.resizable(False,False)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - root.winfo_reqwidth()) / 2
    y_coordinate = (screen_height - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x_coordinate, y_coordinate))

    root.title("Files Backup system")
    tk.CTkLabel(root,text="File Backup system",font=("Arial",25,"bold")).grid(pady=10,padx=50)
    source_path = tk.CTkEntry(root,width=220)
    source_path.grid(pady=20,sticky='w',padx=10)
    browse_button = tk.CTkButton(root, text="Browse", font=("Arial", 15, "bold"), width=30, command=browse).grid(row=1, sticky='e', padx=10)
    backup_button = tk.CTkButton(root, text="Backup", font=("Arial", 15, "bold"),command=backup).grid(pady=20, padx=10)
    open_button = tk.CTkButton(root, text="Open Backup\nFolder", font=("Arial", 15, "bold"),command=open_folder).grid(pady=10,padx=10)
    root.mainloop()
