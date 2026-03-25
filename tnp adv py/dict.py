students = {"A": 90, "B": 80}

students["C"] = 85
students["A"] = 95
del students["B"]

print("Keys:", students.keys())
print("Values:", students.values())
print("Items:", students.items())