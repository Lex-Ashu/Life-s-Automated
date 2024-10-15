import PyPDF2  # type: ignore
import os
from tkinter import filedialog,messagebox
import customtkinter as tk # type: ignore

def merge():
    def merge_pdfs(pdf_directory_path, merged_pdf_file_name,save_location):
        try:
            os.chdir(save_location)
            if not merged_pdf_file_name.endswith(".pdf"):
                merged_pdf_file_name += ".pdf"
            merger = PyPDF2.PdfMerger()

            for file in os.listdir(pdf_directory_path):
                if file.lower().endswith(".pdf"):
                    file_path = os.path.join(pdf_directory_path, file)

                    if os.path.exists(file_path):
                        merger.append(file_path)
                    else:
                        messagebox.showinfo("Message",f"Warning: Skipping non-existent file: {file_path}")

            merger.write(merged_pdf_file_name)
            merger.close()

            messagebox.showinfo("Success",f"Pdfs are merged into:{merged_pdf_file_name}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")

    def browse_directory():
        pdf_directory_path = filedialog.askdirectory()
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, pdf_directory_path)

    def save_browse():
        save_path = filedialog.askdirectory()
        save_entry.delete(0,tk.END)
        save_entry.insert(0,save_path)

    def merge_pdfs_gui():
        pdf_directory_path = directory_entry.get()
        merged_pdf_file_name = filename_entry.get()
        save_location = save_entry.get()
        merge_pdfs(pdf_directory_path, merged_pdf_file_name,save_location)


    root = tk.CTk()
    root.resizable(False,False)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - root.winfo_reqwidth()) / 2
    y_coordinate = (screen_height - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x_coordinate, y_coordinate))

    root.title("PDF Merger")

    directory_label = tk.CTkLabel(root, text="PDF Directory:")
    filename_label = tk.CTkLabel(root, text="Output PDF Filename:")
    save_label = tk.CTkLabel(root,text="Pdf save location")

    directory_entry = tk.CTkEntry(root, width=200)
    filename_entry = tk.CTkEntry(root, width=200)
    save_entry = tk.CTkEntry(root,width=200)

    save_br_butt = tk.CTkButton(root,text="Browse",command= save_browse)
    browse_button = tk.CTkButton(root, text="Browse", command=browse_directory)
    merge_button = tk.CTkButton(root, text="Merge PDFs", command=merge_pdfs_gui)

    directory_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    filename_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    save_label.grid(row=2,column=0,sticky=tk.W,padx=10)
    directory_entry.grid(row=0, column=1, padx=10, pady=5, columnspan=2)
    filename_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=2)
    save_entry.grid(row=2,column=1,padx=10,pady=5,columnspan=2)
    browse_button.grid(row=0, column=3, pady=5)
    save_br_butt.grid(row=2,column=3,padx =10)
    merge_button.grid(row=3, column=1, columnspan=2, pady=10)

    root.mainloop()
