class OutOfStockError(Exception):
    pass

class InvalidProductIDError(Exception):
    pass

class Inventory:
    def __init__(self):
        self.products = {"P101": 5, "P102": 3, "P103": 0}

    def purchase(self):
        try:
            pid = input("Enter Product ID: ")
            qty = int(input("Enter Quantity: "))

            if pid not in self.products:
                raise InvalidProductIDError("Invalid Product ID")

            if self.products[pid] < qty:
                raise OutOfStockError("Product out of stock")

            self.products[pid] -= qty
            print("Purchase successful")

        except InvalidProductIDError as e:
            print("Error:", e)
        except OutOfStockError as e:
            print("Error:", e)
        except ValueError:
            print("Quantity must be a number")

    def show_products(self):
        for p, q in self.products.items():
            print(p, ":", q)


inv = Inventory()

while True:
    print("\n1.Purchase 2.Show Products 3.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        inv.purchase()
    elif ch == "2":
        inv.show_products()
    elif ch == "3":
        break
    else:
        print("Invalid choice")