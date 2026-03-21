import json
from crypto import encrypt_password, decrypt_password

FILE_NAME = "Passwords.json"

def add_password(site, username, password, key):
    encrypted_password = encrypt_password(password, key)
    with open(FILE_NAME, "r") as file:
        data = json.load(file)

    if "passwords" not in data:
        data["passwords"] = []

    for entry in data["passwords"]:
        if entry["site"].lower() == site.lower():
            print("Site already exists. Use a different name or update the existing entry.")
            return

    data['passwords'].append({"site": site, "username": username, "password": encrypted_password})
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
        print("Password added successfully!")

def get_password(site, key):
    with open(FILE_NAME, "r") as file:
        data = json.load(file)

    for entry in data.get("passwords", []):
        if entry["site"].lower() == site.lower():
            decrypted_password = decrypt_password(entry["password"], key)
            print(f"Site: {entry['site']}\nUsername: {entry['username']}\nPassword: {decrypted_password}\n")
            return
            
    print("Password not found.")

def delete_password(site):
    with open(FILE_NAME, 'r') as file:
        data = json.load(file)

    for entry in data.get("passwords", []):
        if entry["site"].lower() == site.lower():
            data["passwords"].remove(entry)
            with open(FILE_NAME, "w") as file:
                json.dump(data, file, indent=4)
                print("Password deleted successfully!")
            return
            
    print("Site not found.")

def update_password(site, key, updated_pass):
    with open(FILE_NAME, 'r') as file:
        data = json.load(file)

    for entry in data.get("passwords", []):
        if entry["site"].lower() == site.lower():
            encrypted = encrypt_password(updated_pass, key)
            entry["password"] = encrypted
            with open(FILE_NAME, "w") as file:
                json.dump(data, file, indent=4)
                print("Password updated successfully.")
            return

    print("Site not found.")

def list_passwords(key):
    with open(FILE_NAME, 'r') as file:
        data = json.load(file)

    passwords_list = data.get("passwords", [])
    if not passwords_list:
        print("No passwords saved yet.")
        return

    for entry in passwords_list:
        decrypted_password = decrypt_password(entry["password"], key)
        print("==============================================================")
        print(f"Site: {entry['site']}\nUsername: {entry['username']}\nPassword: {decrypted_password}")
    print("==============================================================")