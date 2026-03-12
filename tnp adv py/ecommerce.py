class ECommerce:
    def __init__(self):
        self.products = {"laptop": 5, "phone": 10, "headphones": 7}
        self.orders = {}

    def place_order(self):
        try:
            product = input("Enter product: ").lower()
            qty = int(input("Enter quantity: "))
            coupon = input("Enter coupon code: ")
            payment = input("Payment method (card/upi/cash): ").lower()

            if product not in self.products:
                raise KeyError("Product not found")

            if self.products[product] < qty:
                raise ValueError("Out of stock")

            if coupon != "" and coupon != "SAVE10":
                raise ValueError("Invalid coupon code")

            if payment not in ["card", "upi", "cash"]:
                raise ValueError("Invalid payment method")

            order_id = len(self.orders) + 1
            self.orders[order_id] = product
            self.products[product] -= qty

            print("Order placed. ID:", order_id)

        except (ValueError, KeyError) as e:
            print("Error:", e)

    def return_order(self):
        try:
            order_id = int(input("Enter order ID to return: "))
            if order_id not in self.orders:
                raise KeyError("Invalid order ID")

            product = self.orders[order_id]
            self.products[product] += 1
            print("Order returned")

        except (ValueError, KeyError) as e:
            print("Error:", e)

    def refund(self):
        try:
            order_id = int(input("Enter order ID for refund: "))
            if order_id not in self.orders:
                raise KeyError("Invalid order ID")

            print("Refund processed for order", order_id)

        except (ValueError, KeyError) as e:
            print("Error:", e)


shop = ECommerce()

while True:
    print("\n1.Place Order 2.Return Order 3.Refund 4.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        shop.place_order()
    elif ch == "2":
        shop.return_order()
    elif ch == "3":
        shop.refund()
    elif ch == "4":
        break
    else:
        print("Invalid choice")