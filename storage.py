import json
from crypto import encrypt_password, decrypt_password

FILE_NAME = "Passwords.json"

def add_password(site, username, password, key):
    """Add a new password entry. Returns (success: bool, message: str)."""
    encrypted_password = encrypt_password(password, key)
    with open(FILE_NAME, "r") as file:
        data = json.load(file)

    if "passwords" not in data:
        data["passwords"] = []

    for entry in data["passwords"]:
        if entry["site"].lower() == site.lower():
            return False, "Site already exists. Use a different name or update the existing entry."

    data['passwords'].append({"site": site, "username": username, "password": encrypted_password})
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
    return True, "Password added successfully!"

def get_password(site, key):
    """Get a password entry by site name. Returns dict or None."""
    with open(FILE_NAME, "r") as file:
        data = json.load(file)

    for entry in data.get("passwords", []):
        if entry["site"].lower() == site.lower():
            decrypted_password = decrypt_password(entry["password"], key)
            return {
                "site": entry["site"],
                "username": entry["username"],
                "password": decrypted_password
            }
    return None

def delete_password(site):
    """Delete a password entry by site name. Returns (success: bool, message: str)."""
    with open(FILE_NAME, 'r') as file:
        data = json.load(file)

    for entry in data.get("passwords", []):
        if entry["site"].lower() == site.lower():
            data["passwords"].remove(entry)
            with open(FILE_NAME, "w") as file:
                json.dump(data, file, indent=4)
            return True, "Password deleted successfully."
    return False, "Site not found."

def update_password(site, key, updated_pass):
    """Update a password entry. Returns (success: bool, message: str)."""
    with open(FILE_NAME, 'r') as file:
        data = json.load(file)

    for entry in data.get("passwords", []):
        if entry["site"].lower() == site.lower():
            encrypted = encrypt_password(updated_pass, key)
            entry["password"] = encrypted
            with open(FILE_NAME, "w") as file:
                json.dump(data, file, indent=4)
            return True, "Password updated successfully."
    return False, "Site not found."

def list_passwords(key):
    """List all password entries. Returns list of dicts with decrypted passwords."""
    with open(FILE_NAME, 'r') as file:
        data = json.load(file)

    results = []
    for entry in data.get("passwords", []):
        decrypted_password = decrypt_password(entry["password"], key)
        results.append({
            "site": entry["site"],
            "username": entry["username"],
            "password": decrypted_password
        })
    return results
