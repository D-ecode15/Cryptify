# 🔐 CRYPTIFY - SECURING YOUR DATA

Cryptify is a powerful **Python-based** file encryption and decryption tool that utilizes **AES-256** (CBC mode). It provides a user-friendly GUI with drag-and-drop support, making it easy for users to securely encrypt and decrypt their files with password protection.

---

## 📌 Overview

Cryptify ensures your sensitive files remain secure through strong encryption, leveraging the advanced **AES-256** algorithm in CBC mode. With an intuitive user interface, you can quickly encrypt or decrypt files using simple drag-and-drop actions. This tool is available across multiple platforms, including **Windows**, **Mac**, and **Linux**.

---

## 🎯 Features

- ✅ **AES-256 Encryption (CBC Mode)**: Secure your files with industry-standard encryption.
- ✅ **User-Friendly GUI**: Built using **Tkinter** and **CustomTkinter**, ensuring an easy and smooth user experience.
- ✅ **Drag & Drop Support**: Quickly add files to be encrypted or decrypted by dragging them into the UI.
- ✅ **Password Protection**: Encrypt and decrypt files using a password that is essential for restoring the original file.
- ✅ **Cross-Platform Support**: Works seamlessly on **Windows**, **Mac**, and **Linux**.
- ✅ **Taskbar & Title Bar Icons**: Custom icons to enhance your app’s appearance.

---

## 🔧 Installation

To get started with **Cryptify**, follow these simple steps:

1️⃣ **Clone the Repository**  
   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/YOUR-GITHUB-USERNAME/Cryptify.git
   cd Cryptify
   ```

2️⃣ **Install Dependencies**  
   Ensure that you have **Python 3.7+** installed. Then, install the necessary dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

3️⃣ **Run the Application**  
   Once the dependencies are installed, you can launch the application:

   ```bash
   python EncDec.py
   ```

---

## 📂 File Structure

The project follows this structure:

```
📁 Cryptify
 ├── 📄 EncDec.py          # Main Python script
 ├── 📄 requirements.txt   # Required dependencies
 ├── 📄 README.md          # Project documentation
 ├── 🖼️ cryptify_logo.ico  # Taskbar icon (Windows)
 ├── 🖼️ cryptify_main.png  # Logo for the UI
```

---

## 📜 Requirements

Ensure you have **Python 3.7+** and the following dependencies installed:

```txt
customtkinter
tkinterdnd2
pycryptodome
pillow
```

---

## 🔒 How It Works

### 🔐 Encrypting a File

1️⃣ Click **"Encrypt File"** and select the file you want to encrypt.  
2️⃣ Enter a password. This password will be required for decryption.  
3️⃣ The encrypted file will be saved with a `.enc` extension.

### 🔓 Decrypting a File

1️⃣ Click **"Decrypt File"** and select the encrypted file (.enc).  
2️⃣ Enter the password used during encryption.  
3️⃣ The original file will be restored.

### 🖱️ Drag & Drop Support

For convenience, you can **drag** and **drop** a file directly into the application’s UI to quickly encrypt or decrypt it!

---

## 🚀 Contributing

We welcome contributions to improve **Cryptify**! To contribute:

1. Fork the repository.
2. Create a new branch (e.g., **feature-new** or **fix-bug**).
3. Commit your changes and open a pull request.

---

## 📜 License

This project is open-source and available under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

Stay secure, encrypt with ease! 💻🔒
