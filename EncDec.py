import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image, ImageTk

# Set dark theme colors
BACKGROUND_COLOR = "#282828"
FRAME_COLOR = "#303030"
BUTTON_COLOR = "#505050"
TEXT_COLOR = "#FFFFFF"

# Configure UI
ctk.set_appearance_mode("dark")

# Key derivation function
def derive_key(password: str, salt: bytes):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000, dklen=32)

# Get password from user
def get_password(prompt_text):
    popup = tk.Toplevel(app)
    popup.configure(bg=FRAME_COLOR)
    popup.title("Enter Password")
    popup.geometry("320x180")
    popup.resizable(False, False)
    popup.grab_set()

    label = ctk.CTkLabel(popup, text=prompt_text, font=("Arial", 14, "bold"), text_color=TEXT_COLOR)
    label.pack(pady=15)

    # Password entry field (visible text)
    entry = ctk.CTkEntry(popup, width=250)  # Removed `show="*"`
    entry.pack(pady=10)
    entry.focus_set()

    password_var = tk.StringVar()

    def submit_password():
        password_var.set(entry.get())
        popup.destroy()
        app.focus_force()

    btn_submit = ctk.CTkButton(popup, text="OK", command=submit_password, fg_color=BUTTON_COLOR,
                               hover_color="#666666", font=("Arial", 14, "bold"), width=120, height=40)
    btn_submit.pack(pady=10)

    popup.wait_window()
    app.focus_force()
    return password_var.get()

# Encrypt file
def encrypt_file(file_path):
    if not file_path:
        return

    password = get_password("Enter encryption password:")
    if not password:
        return

    salt = get_random_bytes(16)
    key = derive_key(password, salt)
    iv = get_random_bytes(16)

    with open(file_path, 'rb') as f:
        plaintext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    encrypted_data = salt + iv + len(plaintext).to_bytes(4, 'big') + ciphertext
    encrypted_file_path = file_path + ".enc"

    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_data)

    messagebox.showinfo("Success", f"File encrypted successfully!\nSaved as: {encrypted_file_path}")

# Decrypt file
def decrypt_file(file_path):
    if not file_path:
        return

    password = get_password("Enter decryption password:")
    if not password:
        return

    with open(file_path, 'rb') as f:
        data = f.read()

    salt, iv, original_length_bytes, ciphertext = data[:16], data[16:32], data[32:36], data[36:]
    key = derive_key(password, salt)
    original_length = int.from_bytes(original_length_bytes, 'big')

    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)[:original_length]
    except (ValueError, KeyError):
        messagebox.showerror("Error", "Invalid password or corrupted file!")
        return

    original_name = os.path.splitext(file_path)[0]
    save_path = filedialog.asksaveasfilename(initialfile=os.path.basename(original_name),
                                             filetypes=[["All Files", "*.*"]],
                                             title="Save Decrypted File")
    if save_path:
        with open(save_path, 'wb') as f:
            f.write(decrypted_data)
        messagebox.showinfo("Success", f"File decrypted successfully!\nSaved as: {save_path}")

# Drag & Drop functionality
def on_drop(event):
    file_path = event.data.strip().replace("{", "").replace("}", "")
    drag_label.configure(text="📂 Processing...")

    if file_path.endswith(".enc"):
        decrypt_file(file_path)
    else:
        encrypt_file(file_path)

    drag_label.configure(text="📂 Drag & Drop files here!")

# UI Setup
app = TkinterDnD.Tk()
app.title("Secure File Encryption Tool")
app.geometry("750x550")
app.configure(bg=BACKGROUND_COLOR)

frame = ctk.CTkFrame(app, fg_color=FRAME_COLOR)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Set taskbar icon
try:
    icon_path = "cryptify_logo.ico"  # Use an .ico file for best results
    app.iconbitmap(icon_path)  # Works on Windows
except Exception as e:
    print(f"Error loading icon: {e}")

# Load and display logo
try:
    logo_img = Image.open("cryptify_main.png")
    logo_img = logo_img.resize((300, 168), Image.LANCZOS)  # Fixed PIL.Image.ANTIALIAS issue
    logo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(frame, image=logo, bg=FRAME_COLOR)
    logo_label.pack(pady=10)
    app.wm_iconphoto(True, logo)  # Set PNG as taskbar icon for Linux/Mac
except Exception as e:
    print(f"Error loading logo: {e}")

label = ctk.CTkLabel(frame, text="🔐 File Encryption & Decryption Tool", font=("Arial", 24, "bold"), text_color=TEXT_COLOR)
label.pack(pady=20)

btn_width, btn_height = 260, 55

encrypt_btn = ctk.CTkButton(frame, text="🔒 Encrypt File", command=lambda: encrypt_file(filedialog.askopenfilename()),
                            fg_color=BUTTON_COLOR, hover_color="#666666", font=("Arial", 16, "bold"), width=btn_width, height=btn_height)
encrypt_btn.pack(pady=15)

decrypt_btn = ctk.CTkButton(frame, text="🔓 Decrypt File", command=lambda: decrypt_file(filedialog.askopenfilename()),
                            fg_color=BUTTON_COLOR, hover_color="#666666", font=("Arial", 16, "bold"), width=btn_width, height=btn_height)
decrypt_btn.pack(pady=15)

drag_label = ctk.CTkLabel(frame, text="📂 Drag & Drop files here!", font=("Arial", 18, "bold"), text_color=TEXT_COLOR)
drag_label.pack(pady=30)

frame.drop_target_register(DND_FILES)
frame.dnd_bind("<<Drop>>", on_drop)

app.mainloop()
