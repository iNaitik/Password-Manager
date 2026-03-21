# 🔐 Password Manager (CLI)

A secure command-line password manager built using Python.

## Features
- Master password authentication (bcrypt)
- Encrypted password storage (Fernet)
- Add / View / Update / Delete passwords
- List all saved credentials

## Tech Stack
- Python
- bcrypt (secure hashing)
- cryptography (Fernet encryption)
- JSON (local storage)

## How it works
- Master password is hashed using bcrypt
- Encryption key is derived from the master password
- All stored passwords are encrypted using Fernet (AES)

## Run
```bash
pip install -r requirements.txt
python main.py


Note
Passwords are not recoverable if the master password is lost.