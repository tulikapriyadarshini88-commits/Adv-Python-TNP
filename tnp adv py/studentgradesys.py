class StudentGradeSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        try:
            student_id = input("Enter Student ID: ").strip()
            if student_id == "":
                raise ValueError("Student ID cannot be empty")

            grade = input("Enter Grade: ").strip()
            if grade == "":
                raise ValueError("Grade cannot be empty")

            grade = float(grade)
            self.students[student_id] = grade
            print("Student added")

        except ValueError as e:
            print("Error:", e)

    def update_grade(self):
        try:
            student_id = input("Enter Student ID: ")
            if student_id not in self.students:
                raise KeyError("Invalid Student ID")

            grade = float(input("Enter new grade: "))
            self.students[student_id] = grade
            print("Grade updated")

        except ValueError:
            print("Grade must be a number")
        except KeyError as e:
            print("Error:", e)

    def delete_student(self):
        try:
            student_id = input("Enter Student ID: ")
            if student_id not in self.students:
                raise KeyError("Invalid Student ID")

            del self.students[student_id]
            print("Student deleted")

        except KeyError as e:
            print("Error:", e)

    def display(self):
        for sid, grade in self.students.items():
            print(sid, ":", grade)


system = StudentGradeSystem()

while True:
    print("\n1.Add 2.Update 3.Delete 4.Display 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        system.add_student()
    elif choice == "2":
        system.update_grade()
    elif choice == "3":
        system.delete_student()
    elif choice == "4":
        system.display()
    elif choice == "5":
        break
    else:
        print("Invalid choice")