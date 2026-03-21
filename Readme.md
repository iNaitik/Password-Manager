# 🔐 Secure Password Manager (CLI)

A command-line password manager built with a focus on **security fundamentals** like authentication, encryption, and secure storage.

---

## 🚀 Features

* 🔑 Master password authentication using **bcrypt**
* 🔒 Encrypted password storage using **Fernet (AES)**
* ➕ Add new credentials
* 🔍 Retrieve saved passwords
* ✏️ Update existing passwords
* ❌ Delete credentials
* 📋 List all stored accounts

---

## 🧠 How It Works

* Master password is **hashed using bcrypt** (with salt)
* Encryption key is derived from the master password
* All passwords are stored in **encrypted format**
* Decryption happens only after successful authentication

---

## 🔐 Security Design

- Master password is hashed using bcrypt (with salt)
- Encryption key is derived from the master password
- Passwords are encrypted using Fernet (AES-based encryption)
- System is resistant to offline brute-force attacks due to slow hashing

---

## 🛠️ Tech Stack

* Python
* bcrypt (secure password hashing)
* cryptography (Fernet encryption)
* JSON (local storage)

---

## ▶️ Run the Project

```bash
pip install -r requirements.txt
python main.py
```

---

## ⚠️ Security Note

* Passwords are **not recoverable** if the master password is lost
* Security depends on the strength of the master password

---

## 📌 Learning Highlights

This project demonstrates:

* Difference between **hashing and encryption**
* Secure authentication design
* Key derivation for encryption
* Protection against brute-force attacks

---

## 💻 Demo

1. Add a new password
2. Get a password
3. Delete a password
4. Update a password

Example:

Enter your choice: 1
Enter site: gmail
Enter username: user123
Enter password: *****

Password stored successfully.


<img width="1269" height="823" alt="image" src="https://github.com/user-attachments/assets/7aca4631-60cf-4d88-a59a-5241c249fe1d" />


---

## ⚠️ Limitations

- Security depends on strength of master password
- No cloud sync (local storage only)
- No password recovery if master password is lost

---

## 👤 Author

Naitik
Engineering Student | Python Developer
