emp = {}

while True:
    ch = input("1.Add 2.Remove 3.Show 4.Exit: ")

    if ch == "1":
        name = input("Name: ")
        emp[name] = "Present"

    elif ch == "2":
        name = input("Remove: ")
        emp.pop(name, None)

    elif ch == "3":
        print(emp)

    else:
        break