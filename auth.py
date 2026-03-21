import os
import json
from crypto import hash_password, verify_password

file_name = "Passwords.json"

def setup_master_password(password, confirm_password):
    """Set up the master password. Returns (success: bool, message: str)."""
    if password != confirm_password:
        return False, "Passwords do not match."
    if len(password) < 1:
        return False, "Password cannot be empty."

    with open(file_name, "r") as file:
        data = json.load(file)

    if "master_password" in data:
        return False, "Master password already exists."

    hashed_password = hash_password(password)
    data["master_password"] = hashed_password.decode()
    with open(file_name, "w") as file:
        json.dump(data, file)
    return True, "Master password set successfully!"

def verify_master_password(password):
    """Verify the master password. Returns (password_or_None, message: str)."""
    with open(file_name, 'r') as file:
        data = json.load(file)

    hashed_password = data.get("master_password")
    if hashed_password and verify_password(password, hashed_password.encode()):
        return password, "Access granted."
    else:
        return None, "Incorrect master password."

def has_master_password():
    """Check if a master password has been set. Returns bool."""
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            json.dump({}, file)
        return False
    with open(file_name, "r") as file:
        data = json.load(file)
    return "master_password" in data
