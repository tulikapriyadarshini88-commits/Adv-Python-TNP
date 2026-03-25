menu = {"burger": 100, "pizza": 200, "tea": 20}
total = 0

while True:
    item = input("Enter item (exit to stop): ")
    if item == "exit":
        break
    if item in menu:
        total += menu[item]

tax = total * 0.05
print("Total:", total)
print("Tax:", tax)
print("Final:", total + tax)