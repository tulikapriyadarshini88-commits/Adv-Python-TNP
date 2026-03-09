class Billing:
    def __init__(self):
        self.cart = []
        self.transactions = []

    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        self.cart.append((name, price, quantity))
        print("Product Added")

    def generate_bill(self):
        total = 0
        print("\n--- BILL ---")
        for name, price, quantity in self.cart:
            amount = price * quantity
            total += amount
            print(name, "x", quantity, "=", amount)

        discount = float(input("Enter discount %: "))
        final = total - (total * discount / 100)

        print("Total:", total)
        print("Final Amount:", final)

        self.transactions.append(final)
        self.cart.clear()

    def show_transactions(self):
        print("\nTransactions:")
        for t in self.transactions:
            print(t)


store = Billing()

while True:
    print("\n1.Add Product")
    print("2.Generate Bill")
    print("3.Show Transactions")
    print("4.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        store.add_product()
    elif choice == "2":
        store.generate_bill()
    elif choice == "3":
        store.show_transactions()
    elif choice == "4":
        break
    else:
        print("Invalid Choice")

        