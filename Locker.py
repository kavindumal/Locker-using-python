import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import hashlib
import time

PASSWORD_HASH = hashlib.sha256("Mal@1234".encode()).hexdigest()

def password_page():
    root = tk.Tk()
    root.title("Secure Access")
    root.geometry("400x300")
    root.configure(bg="#2b2b2b")

    title_font = ("Helvetica", 16, "bold")
    label_font = ("Helvetica", 12)
    button_font = ("Helvetica", 12, "bold")

    def fade_in(widget, start_alpha=0.0, end_alpha=1.0, step=0.05, delay=10):
        alpha = start_alpha
        widget.attributes('-alpha', alpha)
        while alpha < end_alpha:
            alpha += step
            root.update_idletasks()
            widget.attributes('-alpha', alpha)
            time.sleep(delay / 1000.0)

    def check_password():
        entered_password = password_var.get()
        hashed_entered_password = hashlib.sha256(entered_password.encode()).hexdigest()

        if hashed_entered_password == PASSWORD_HASH:
            messagebox.showinfo("Access Granted", "Correct Password!")
            root.destroy()  # Close password window
            folder_locker_page()  # Open folder locker page
        else:
            messagebox.showerror("Access Denied", "Incorrect Password!")
            password_entry.delete(0, tk.END)  # Clear password field

    def folder_locker_page():
        import os
        import tkinter as tk
        import ctypes
        from tkinter import filedialog, messagebox
        from tkinter import font as tkFont
        from cryptography.fernet import Fernet

        def get_documents_folder():
            return os.path.join(os.path.expanduser("~"), "Documents")

        def create_hidden_folder(folder_name="locker"):
            documents_path = get_documents_folder()

            hidden_folder_path = os.path.join(documents_path, folder_name)

            if not os.path.exists(hidden_folder_path):
                os.makedirs(hidden_folder_path)
                print(f"Folder '{hidden_folder_path}' created successfully.")
            else:
                print(f"Folder '{hidden_folder_path}' already exists.")

            if os.name == 'nt':
                ctypes.windll.kernel32.SetFileAttributesW(hidden_folder_path, 2)

            return hidden_folder_path

        def generate_key():
            key = Fernet.generate_key()

            folder_path = create_hidden_folder()

            key_file_path = os.path.join(folder_path, "secret.key")
            with open(key_file_path, "wb") as key_file:
                key_file.write(key)

            return key_file_path

        def load_key():
            folder_path = create_hidden_folder()
            key_file_path = os.path.join(folder_path, "secret.key")

            if os.path.exists(key_file_path):
                with open(key_file_path, "rb") as key_file:
                    return key_file.read()
            else:
                raise FileNotFoundError("Encryption key not found.")

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

        def browse_folder():
            folder_path = filedialog.askdirectory()
            folder_var.set(folder_path)

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

        app = tk.Tk()
        app.title("Locker Advanced")
        app.geometry("800x600")
        app.configure(bg="#2b2b2b")

        title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
        button_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        label_font = tkFont.Font(family="Helvetica", size=12)

        title_label = tk.Label(app, text="Secure Folder Locker", font=title_font, fg="white", bg="#2b2b2b")
        title_label.pack(pady=20)

        folder_var = tk.StringVar()

        folder_frame = tk.Frame(app, bg="#2b2b2b")
        folder_frame.pack(pady=10)

        folder_label = tk.Label(folder_frame, text="Select Folder:", font=label_font, fg="white", bg="#2b2b2b")
        folder_label.pack(side=tk.LEFT, padx=5)

        folder_entry = tk.Entry(folder_frame, textvariable=folder_var, width=40, font=label_font, bg="#393939",
                                fg="white", relief="flat")
        folder_entry.pack(side=tk.LEFT, padx=5)

        browse_button = tk.Button(folder_frame, text="Browse", command=browse_folder, font=button_font, bg="#0077B6",
                                  fg="white", relief="flat", activebackground="#005f8a")
        browse_button.pack(side=tk.LEFT, padx=5)

        button_frame = tk.Frame(app, bg="#2b2b2b")
        button_frame.pack(pady=20)

        lock_button = tk.Button(button_frame, text="Lock Folder", command=lock_folder, font=button_font, bg="red",
                                fg="white", relief="flat", width=15, activebackground="#b30000")
        lock_button.grid(row=0, column=0, padx=10)

        unlock_button = tk.Button(button_frame, text="Unlock Folder", command=unlock_folder, font=button_font,
                                  bg="green", fg="white", relief="flat", width=15, activebackground="#007f00")
        unlock_button.grid(row=0, column=1, padx=10)

    title_label = tk.Label(root, text="Secure Folder Locker", font=title_font, fg="white", bg="#2b2b2b")
    title_label.pack(pady=30)

    password_label = tk.Label(root, text="Enter Password:", font=label_font, fg="white", bg="#2b2b2b")
    password_label.pack(pady=10)

    password_var = tk.StringVar()
    password_entry = ttk.Entry(root, textvariable=password_var, show="*", font=label_font, width=25)
    password_entry.pack(pady=10)

    submit_button = ttk.Button(root, text="Enter", command=check_password)
    submit_button.pack(pady=20)

    style = ttk.Style()
    style.configure("TButton", font=button_font, padding=6, relief="flat", background="#0077B6", foreground="white")

    fade_in(root)

    root.mainloop()

password_page()