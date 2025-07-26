import tkinter as tk
from tkinter import messagebox, simpledialog
from cryptography.fernet import Fernet
import os
import json
import bcrypt
import random
import string

# Load the secret key
def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# Load and return the encrypted password data
def load_passwords():
    if not os.path.exists("passwords.dat"):
        return {}
    
    with open("passwords.dat", "rb") as f:
        encrypted_data = f.read()
    
    try:
        data = fernet.decrypt(encrypted_data)
        return json.loads(data)
    except Exception as e:
        messagebox.showerror("Error", "Failed to load or decrypt saved passwords.")
        return {}

# Save passwords to file (encrypted)
def save_passwords(passwords):
    data = json.dumps(passwords).encode()
    encrypted_data = fernet.encrypt(data)
    
    with open("passwords.dat", "wb") as f:
        f.write(encrypted_data)

# Generate a strong random password
def generate_random_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

# GUI Functions
def add_password():
    site = simpledialog.askstring("Site", "Enter the site or app name:")
    if not site:
        return

    choice = messagebox.askyesno("Generate Password", "Do you want to generate a strong password?")
    if choice:
        password = generate_random_password()
        messagebox.showinfo("Generated Password", f"Password: {password}\n\nYou can copy and save it manually.")
    else:
        password = simpledialog.askstring("Password", f"Enter password for {site}:")

    if not password:
        return

    passwords = load_passwords()
    passwords[site] = password
    save_passwords(passwords)
    messagebox.showinfo("Saved", "Password saved successfully.")

def retrieve_password():
    site = simpledialog.askstring("Site", "Enter the site or app name to retrieve password:")
    if not site:
        return
    
    passwords = load_passwords()
    password = passwords.get(site)

    if password:
        messagebox.showinfo("Password Found", f"Password for {site}:\n{password}")
    else:
        messagebox.showerror("Not Found", f"No password found for {site}.")

# Master Password Verification
def verify_master_password():
    if not os.path.exists("master.hash"):
        messagebox.showerror("Error", "Master password is not set up.")
        return False
    
    input_pwd = simpledialog.askstring("Master Password", "Enter master password:", show="*")
    if not input_pwd:
        return False

    with open("master.hash", "rb") as f:
        stored_hash = f.read()

    return bcrypt.checkpw(input_pwd.encode(), stored_hash)

# Main GUI Setup
def main():
    if not verify_master_password():
        messagebox.showerror("Access Denied", "Wrong or no master password entered.")
        return

    global fernet
    key = load_key()
    fernet = Fernet(key)

    root = tk.Tk()
    root.title("Password Manager")

    tk.Button(root, text="Add Password", width=30, command=add_password).pack(pady=10)
    tk.Button(root, text="Retrieve Password", width=30, command=retrieve_password).pack(pady=10)
    tk.Button(root, text="Exit", width=30, command=root.destroy).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
