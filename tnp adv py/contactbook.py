class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        try:
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone: ").strip()

            if name == "" or phone == "":
                raise ValueError("Fields cannot be empty")

            if name in self.contacts:
                raise ValueError("Contact already exists")

            if not phone.isdigit() or len(phone) != 10:
                raise ValueError("Invalid phone number")

            self.contacts[name] = phone
            print("Contact saved")

        except ValueError as e:
            print("Error:", e)

    def edit_contact(self):
        try:
            name = input("Enter Name to edit: ").strip()

            if name not in self.contacts:
                raise KeyError("Contact not found")

            phone = input("Enter new phone: ").strip()

            if not phone.isdigit() or len(phone) != 10:
                raise ValueError("Invalid phone number")

            self.contacts[name] = phone
            print("Contact updated")

        except (ValueError, KeyError) as e:
            print("Error:", e)

    def search_contact(self):
        name = input("Enter Name to search: ").strip()
        if name in self.contacts:
            print(name, ":", self.contacts[name])
        else:
            print("Contact not found")


book = ContactBook()

while True:
    print("\n1.Add 2.Edit 3.Search 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        book.add_contact()
    elif choice == "2":
        book.edit_contact()
    elif choice == "3":
        book.search_contact()
    elif choice == "4":
        break
    else:
        print("Invalid choice")