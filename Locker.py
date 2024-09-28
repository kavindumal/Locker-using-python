import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import font as tkFont
from cryptography.fernet import Fernet

# Function to generate a key and save it into a file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

# Function to load the key from the current directory
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt a folder
def encrypt_folder(folder_path, key):
    fernet = Fernet(key)
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                file_data = f.read()
            encrypted_data = fernet.encrypt(file_data)
            with open(file_path, "wb") as f:
                f.write(encrypted_data)
    messagebox.showinfo("Success", "Folder encrypted successfully!")

# Function to decrypt a folder
def decrypt_folder(folder_path, key):
    fernet = Fernet(key)
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                encrypted_data = f.read()
            decrypted_data = fernet.decrypt(encrypted_data)
            with open(file_path, "wb") as f:
                f.write(decrypted_data)
    messagebox.showinfo("Success", "Folder decrypted successfully!")

# Function to browse folder
def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_var.set(folder_path)

# Function to lock/encrypt the folder
def lock_folder():
    folder_path = folder_var.get()
    if folder_path:
        if not os.path.exists("secret.key"):
            key = generate_key()
        else:
            key = load_key()
        encrypt_folder(folder_path, key)
    else:
        messagebox.showwarning("Input Error", "Please select a folder.")

# Function to unlock/decrypt the folder
def unlock_folder():
    folder_path = folder_var.get()
    if folder_path:
        if os.path.exists("secret.key"):
            key = load_key()
            decrypt_folder(folder_path, key)
        else:
            messagebox.showerror("Error", "No key found for decryption.")
    else:
        messagebox.showwarning("Input Error", "Please select a folder.")

# Setup the GUI
app = tk.Tk()
app.title("Locker Advanced")
app.geometry("800x600")
app.configure(bg="#2b2b2b")  # Set background color for the app

# Set custom fonts
title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
button_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
label_font = tkFont.Font(family="Helvetica", size=12)

# Title Label
title_label = tk.Label(app, text="Secure Folder Locker", font=title_font, fg="white", bg="#2b2b2b")
title_label.pack(pady=20)

# Folder selection section
folder_var = tk.StringVar()

folder_frame = tk.Frame(app, bg="#2b2b2b")
folder_frame.pack(pady=10)

folder_label = tk.Label(folder_frame, text="Select Folder:", font=label_font, fg="white", bg="#2b2b2b")
folder_label.pack(side=tk.LEFT, padx=5)

folder_entry = tk.Entry(folder_frame, textvariable=folder_var, width=40, font=label_font, bg="#393939", fg="white", relief="flat")
folder_entry.pack(side=tk.LEFT, padx=5)

browse_button = tk.Button(folder_frame, text="Browse", command=browse_folder, font=button_font, bg="#0077B6", fg="white", relief="flat", activebackground="#005f8a")
browse_button.pack(side=tk.LEFT, padx=5)

# Buttons for lock and unlock
button_frame = tk.Frame(app, bg="#2b2b2b")
button_frame.pack(pady=20)

lock_button = tk.Button(button_frame, text="Lock Folder", command=lock_folder, font=button_font, bg="red", fg="white", relief="flat", width=15, activebackground="#b30000")
lock_button.grid(row=0, column=0, padx=10)

unlock_button = tk.Button(button_frame, text="Unlock Folder", command=unlock_folder, font=button_font, bg="green", fg="white", relief="flat", width=15, activebackground="#007f00")
unlock_button.grid(row=0, column=1, padx=10)

# Run the application
app.mainloop()
