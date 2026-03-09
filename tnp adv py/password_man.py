'''Password Manager'''
import base64

class PasswordEntry:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = base64.b64encode(password.encode()).decode()

    def get_password(self):
        return base64.b64decode(self.password.encode()).decode()

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self):
        website = input("Enter website: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.passwords[website] = PasswordEntry(website, username, password)
        print("Password stored successfully.")

    def edit_password(self):
        website = input("Enter website to update: ")
        if website in self.passwords:
            new_pass = input("Enter new password: ")
            self.passwords[website].password = base64.b64encode(new_pass.encode()).decode()
            print("Password updated.")
        else:
            print("Website not found.")

    def retrieve_password(self):
        website = input("Enter website to retrieve: ")
        if website in self.passwords:
            entry = self.passwords[website]
            print("Username:", entry.username)
            print("Password:", entry.get_password())
        else:
            print("No record found.")


pm = PasswordManager()

while True:
    print("\n1.Add Password 2.Edit Password 3.Retrieve Password 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        pm.add_password()
    elif choice == "2":
        pm.edit_password()
    elif choice == "3":
        pm.retrieve_password()
    elif choice == "4":
        break