import json
import os
from Password_manage_CLI.auth import verify_master_password, setup_master_password
from Password_manage_CLI.storage import add_password, get_password, delete_password, list_passwords,update_password
from Password_manage_CLI.crypto import generate_key

if __name__ == "__main__":
    file_name = "Passwords.json"
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            json.dump({}, file)  #creating an empty dictionary and dumping it into the file

    with open("Passwords.json","r") as file:
        data = json.load(file)
        if "master_password" not in data:
            setup_master_password()

    original_pass = verify_master_password()
    if original_pass:
        key = generate_key(original_pass)
        while True:
            print("1. Add a new password")
            print("2. Get a password")
            print("3. delete a password")
            print("4. Update a password")
            print("5. List all saved passwords")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                site = input("Enter the site name: ")
                username = input("Enter the username: ")
                password = input("Enter the password: ")
                add_password(site,username,password,key)
            elif choice == "2":
                site = input("Enter the site name: ")
                get_password(site,key)
            elif choice == "3":
                site = input("Enter the site name: ")
                delete_password(site)
            elif choice == "4":
                site = input("Enter the site name: ")
                updated_pass = input("Enter Updated Password: ")
                update_password(site,key,updated_pass)
            elif choice == "5":
                list_passwords(key)
                
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    else:
        print("Master password verification failed. Exiting.")

