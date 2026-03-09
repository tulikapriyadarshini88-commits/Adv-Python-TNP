'''warehouse automation'''
class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Warehouse:
    def __init__(self):
        self.inventory = {}

    def add_goods(self):
        name = input("Product name: ")
        qty = int(input("Quantity: "))
        if name in self.inventory:
            self.inventory[name].quantity += qty
        else:
            self.inventory[name] = Product(name, qty)
        print("Goods added.")

    def remove_goods(self):
        name = input("Product name: ")
        qty = int(input("Quantity: "))
        if name in self.inventory and self.inventory[name].quantity >= qty:
            self.inventory[name].quantity -= qty
            print("Goods removed.")
        else:
            print("Insufficient stock.")

    def report(self):
        print("\nInventory Report")
        for p in self.inventory.values():
            print(p.name, ":", p.quantity)

    def forecast(self):
        name = input("Enter product name: ")
        if name in self.inventory:
            print("Forecast demand:", self.inventory[name].quantity * 2)


wh = Warehouse()

while True:
    print("\n1.Add Goods 2.Remove Goods 3.Inventory Report 4.Forecast Demand 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        wh.add_goods()
    elif choice == "2":
        wh.remove_goods()
    elif choice == "3":
        wh.report()
    elif choice == "4":
        wh.forecast()
    elif choice == "5":
        break