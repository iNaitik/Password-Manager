import os
import json
from Password_manage_CLI.crypto import hash_password, verify_password

file_name = "Passwords.json"

def setup_master_password():
    password = input("Enter a master password: ")
    confirm_password = input("Confirm master password: ")
    if password != confirm_password:
        print("Passwords do not match. Try again.")
        return setup_master_password()
    if len(password) < 1:
        print("Password cannot be empty. Try again.")
        return setup_master_password()

    with open(file_name, "r") as file:
        data = json.load(file)

    hashed_password = hash_password(password)
    data["master_password"] = hashed_password.decode()
    with open(file_name, "w") as file:
        json.dump(data, file)
    print("Master password set successfully!")

def verify_master_password():
    password = input("Enter your master password: ")
    with open(file_name, 'r') as file:
        data = json.load(file)

    hashed_password = data.get("master_password")
    if hashed_password and verify_password(password, hashed_password.encode()):
        print("Access granted.")
        return password
    else:
        print("Incorrect master password.")
        return None
