import customtkinter as tk # type: ignore
from tkinter import ttk
import pywhatkit as kit # type: ignore
import schedule,time # type: ignore
from tkinter import messagebox
def wish():
    def send_birthday_wish():
        name = name_entry.get()
        phone_number = phone_entry.get()
        birthdate = birthdate_entry.get()
        message = message_entry.get()

        birthday_person = {
            "name": name,
            "phone_number": phone_number,
            "birthdate": birthdate,
            "message": message,
        }

        kit.sendwhatmsg(phone_number, message)


    def schedule_birthday_wish():
        today = time.strftime("%m/%d")
        global birthday_person
        if today == birthday_person["birthdate"]:
            send_birthday_wish()


    def on_start_button_click():
        schedule.every().day.at("00:01").do(schedule_birthday_wish)    ##### Change time to 00:01
        start_button.configure(state=tk.DISABLED)
        stop_button.configure(state=tk.NORMAL)
        messagebox.showinfo('Birthday Wish','Your wish would be send at 00:01')         ##### Change time to 00:01

    def on_stop_button_click():
        schedule.clear()
        start_button.configure(state=tk.NORMAL)
        stop_button.configure(state=tk.DISABLED)
        root.destroy()

    # GUI setup
    root = tk.CTk()
    root.resizable(False,False)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - root.winfo_reqwidth()) / 2
    y_coordinate = (screen_height - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x_coordinate, y_coordinate))

    root.title("Birthday Wish Scheduler")

    # Entry labels
    name_label = tk.CTkLabel(root, text="Recipient's Name:")
    phone_label = tk.CTkLabel(root, text="Phone Number:")
    birthdate_label = tk.CTkLabel(root, text="Birthdate (MM/DD):")
    message_label = tk.CTkLabel(root, text="Birthday Wish Message:")

    # Entry widgets
    name_entry = tk.CTkEntry(root,width=180)
    phone_entry = tk.CTkEntry(root,width=180)
    birthdate_entry = tk.CTkEntry(root,width=180)
    message_entry = tk.CTkEntry(root,width=180)

    # Start and Stop buttons
    start_button = tk.CTkButton(root, text="Start", command=on_start_button_click)
    stop_button = tk.CTkButton(root, text="Cancel", command=on_stop_button_click, state=tk.DISABLED)

    # Grid layout
    name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    birthdate_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    message_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

    name_entry.grid(row=0, column=1, padx=10, pady=5)
    phone_entry.grid(row=1, column=1, padx=10, pady=5)
    birthdate_entry.grid(row=2, column=1, padx=10, pady=5)
    message_entry.grid(row=5, column=1, padx=10, pady=5)

    start_button.grid(row=6, column=0, columnspan=2, pady=10)
    stop_button.grid(row=7, column=0, columnspan=2, pady=10)

    root.mainloop()
