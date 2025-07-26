# 🔐 Python Password Manager

A simple yet secure password manager built with Python. This app helps you generate strong passwords, store them safely with encryption, and retrieve them when needed — all through a clean graphical interface.



---------------------------------------

## 🚀 Features

- ✅ Generate strong, random passwords
- 🔒 Encrypt and store credentials using Fernet symmetric encryption
- 📋 Copy passwords to clipboard with a click
- 🧠 Auto-fill site/username fields
- 🔍 (Optional) Search saved entries
- 🔐 Master password (coming soon)
- 💾 Save data to local encrypted file

----------------------------------------

## 🛠 Tech Stack

- **Python 3.x**
- **Tkinter** – GUI
- **cryptography** – For secure encryption
- **pyperclip** – For clipboard access (optional)
- **json** – For saving data

----------------------------------------

## 🧑‍💻 How to Run

1. **Clone the repo**

   ```bash
   git clone https://github.com/Lee Christmas/password-manager.git
   cd password-manager

## Install Required Packages

- "pip install cryptography pyperclip"
- "pip install bcrypt"

## File Structure

📦 password-manager/
 ┣ 📄 password_manager.py
 ┣ 📄 secret.key
 ┣ 📄 data.json
 ┣ 📄 README.md
 ┗ 📸 screenshot.png

# Ignore Python cache and virtual environments
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.log

# Ignore environment files
.env
.venv/
env/
venv/

# Ignore editor configs
.vscode/
.idea/

# Ignore system files
.DS_Store
Thumbs.db

# Ignore secret and sensitive files
secret.key
data.json

## MIT License

Copyright (c) 2025 [Ankit Shukla]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

