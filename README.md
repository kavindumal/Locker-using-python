# 📁 Folder Locker Advanced

Folder Locker Advanced is a Python-based GUI application that enables users to **lock (encrypt)** and **unlock (decrypt)** folders on their local machine using a secure key. With a user-friendly interface, it provides robust encryption using the **cryptography** package, ensuring that your folder contents remain private and protected.

## ✨ Features

- 🔒 **Encrypt Folders**: Securely encrypts all files within a selected folder, making them inaccessible without the key.
- 🔓 **Decrypt Folders**: Easily decrypt encrypted files using the correct security key.
- 🖥️ **User-Friendly Interface**: Simple and professional UI, designed using `tkinter` for ease of use.
- 🔑 **Key Management**: Automatically generates and securely stores a secret key for folder encryption and decryption.

## 🛠️ Tech Stack

- **Python**: Core programming language for the entire application.
- **tkinter**: To build an intuitive graphical user interface (GUI).
- **cryptography**: Handles encryption and decryption of folder contents.

## 📝 Prerequisites

Ensure you have the following installed before running the application:

- Python 3.x
- A virtual environment (optional but recommended)
- Required Python packages (detailed in the installation steps below)

## 🚀 Installation

1. **Clone the repository** to your local machine:
    ```bash
    git clone https://github.com/yourusername/FolderLockerAdvanced.git
    cd FolderLockerAdvanced
    ```

2. **Create and activate a virtual environment** (recommended):
    - For Linux/Mac:
      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```
    - For Windows:
      ```bash
      python -m venv .venv
      .venv\Scripts\activate
      ```

3. **Install the required dependencies**:
    ```bash
    pip install cryptography
    ```

4. **Run the application**:
    ```bash
    python Locker.py
    ```

## 🛡️ How It Works

1. **Folder Encryption**: Select a folder to encrypt. The application will use the cryptography library to securely encrypt all files within the folder.
2. **Folder Decryption**: Select a previously encrypted folder and input the correct security key to decrypt and restore access to your files.

## 📦 Project Structure

```plaintext
FolderLockerAdvanced/
│
├── Locker.py               # Main script to run the application
├── README.md               # Project documentation
├── requirements.txt        # List of dependencies (for future expansion)
└── /encrypted_folders      # Folder to store encrypted folders (optional)
