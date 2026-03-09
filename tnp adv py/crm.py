''' CRM(Customer Relationship Manager)'''
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logs = []


class CRM:
    def __init__(self):
        self.customers = []

    def add_customer(self):
        name = input("Customer name: ")
        email = input("Customer email: ")
        self.customers.append(Customer(name, email))
        print("Customer added.")

    def add_log(self):
        name = input("Customer name: ")
        message = input("Communication message: ")
        for c in self.customers:
            if c.name == name:
                c.logs.append(message)
                print("Log added.")

    def show_customers(self):
        for c in self.customers:
            print("\nName:", c.name)
            print("Email:", c.email)
            print("Logs:", c.logs)


crm = CRM()

while True:
    print("\n1.Add Customer 2.Add Communication Log 3.Show Customers 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        crm.add_customer()
    elif choice == "2":
        crm.add_log()
    elif choice == "3":
        crm.show_customers()
    elif choice == "4":
        break