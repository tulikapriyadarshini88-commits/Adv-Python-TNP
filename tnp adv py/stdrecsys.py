students = {}

while True:
    name = input("Enter name (or exit): ")
    if name == "exit":
        break
    marks = list(map(int, input("Enter marks: ").split()))
    students[name] = marks

for k, v in students.items():
    print(k, "Average:", sum(v)/len(v))

topper = max(students, key=lambda x: sum(students[x]))
print("Topper:", topper)