# Folder Locker Advanced

Folder Locker Advanced is a Python-based GUI application that allows users to lock (encrypt) and unlock (decrypt) folders on their local machine using a security key. It uses the `cryptography` package to provide encryption and decryption, and `tkinter` for the graphical interface.

## Features

- **Encrypt Folders**: Securely encrypts all files within a selected folder.
- **Decrypt Folders**: Decrypt files using the same security key.
- **User-Friendly Interface**: Simple and professional UI built with `tkinter`.
- **Key Management**: Generates and stores a secret key for encryption and decryption.

## Tech Stack

- **Python**: Core programming language for the application.
- **tkinter**: For building the graphical user interface (GUI).
- **cryptography**: Used for encrypting and decrypting folder contents.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Virtual environment (optional but recommended)
- Required Python packages (see below)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/FolderLockerAdvanced.git
   cd FolderLockerAdvanced

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # For Linux/Mac
   .venv\Scripts\activate     # For Windows

3. Install the required dependencies:

   ```bash
   pip install cryptography

4. Run the application using Python:

   ```bash
   python Locker.py
