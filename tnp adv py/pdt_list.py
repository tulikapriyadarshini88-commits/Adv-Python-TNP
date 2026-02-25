# Product list
products = {
    "Laptop": 800,
    "Phone": 500,
    "Headphones": 100,
    "Keyboard": 50
}

cart = {}

while True:
    print("\n1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for item in products:
            print(item, "-", products[item])

    elif choice == "2":
        item = input("Enter product name: ")
        if item in products:
            qty = int(input("Enter quantity: "))
            cart[item] = cart.get(item, 0) + qty
            print("Item added!")
        else:
            print("Product not found.")

    elif choice == "3":
        total = 0
        for item in cart:
            price = products[item]
            qty = cart[item]
            print(item, "-", qty, "x", price)
            total += price * qty
        print("Total =", total)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")