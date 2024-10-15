import os
import shutil
from datetime import datetime
import customtkinter as tk # type: ignore
from tkinter import filedialog

def Files_assemble():
    def organize_files(directory_path):
        if not os.path.exists(directory_path):
            result_label.configure(text="Invalid directory path.")
            return
        
        # Define file types and corresponding folders
        file_types = {
            "Images": [".jpg", ".jpeg", ".png", ".gif",".avif"],
            "Documents": [".docx", ".pdf", ".txt",".doc",'.odt'],
            "Videos": [".mp4", ".mkv", ".avi",".3gp"],
            "Music": [".mp3", ".wav"],
            "Programing_files":[".py",".js",".java", ".cpp", ".html", ".css", ".php"]
        }

        # Create folders if they don't exist
        for folder in file_types.keys():
            folder_path = os.path.join(directory_path, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

        # Organize files
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                for folder, extensions in file_types.items():
                    if any(filename.lower().endswith(ext) for ext in extensions):
                        destination_folder = os.path.join(directory_path, folder)
                        shutil.move(file_path, destination_folder)
                        log_file_path = os.path.join(directory_path, "organizer_log.txt")
                        log_message = f"{datetime.now()} - Moved {filename} to {folder} folder.\n"
                        with open(log_file_path, "a") as log_file:
                            log_file.write(log_message)
        result_label.configure(text="File organization completed. Check the log file for details.")

    def browse_directory():
        directory_path = filedialog.askdirectory()
        entry_path.delete(0, tk.END)
        entry_path.insert(0, directory_path)

    def organize_button_click():
        directory_path = entry_path.get()
        organize_files(directory_path)
        

    # GUI setup
    root = tk.CTk()
    root.title("File Organizer")

    root.resizable(False,False)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - root.winfo_reqwidth()) / 2
    y_coordinate = (screen_height - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x_coordinate, y_coordinate))


    entry_path = tk.CTkEntry(root, width=300)
    entry_path.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    browse_button = tk.CTkButton(root, text="Browse", command=browse_directory)
    browse_button.grid(row=0, column=2, pady=10)

    organize_button = tk.CTkButton(root, text="Organize Files", command=organize_button_click)
    organize_button.grid(row=1, column=0, columnspan=3, pady=10)

    result_label = tk.CTkLabel(root, text="")
    result_label.grid(row=2, column=0, columnspan=3)

    root.mainloop()
