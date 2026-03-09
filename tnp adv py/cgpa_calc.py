class Student:

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def calculate_gpa(self):
        avg = sum(self.marks) / len(self.marks)

        if avg >= 90:
            return "O"
        elif avg >= 80:
            return "E"
        elif avg >= 70:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "Fail"

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Marks:", self.marks)
        print("CGPA:", self.calculate_gpa())


name = input("Enter student name: ")
roll = input("Enter roll number: ")

marks = []
for i in range(6):
    m = int(input("Enter marks: "))
    marks.append(m)


s1 = Student(name, roll, marks)

s1.display()