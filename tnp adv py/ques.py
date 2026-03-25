SECTION A: MCQs 
1. What will be the output? 
x = [1,2,3] 
print(x * 2) 
a) [1,2,3,1,2,3] (ANSWER)
b) Error 
c) [2,4,6] 
d) None 
2. What is the output? 
print(bool("")) 
a) True 
b) False (Answer)
c) Error 
d) None 
3. Which is mutable? 
a) tuple 
b) string 
c) list (Answer)
d) int 
4. What will be output? 
print(10 == 10.0) 
a) True 
b) False (Answer)
SECTION B: Output Prediction 
5.  
a = [1,2,3] 
b = a 
b.append(4) 
print(a) 
#Answer: [1, 2, 3, 4]
6. 
def func(x=[]): 
x.append(1) 
return x 
print(func()) 
print(func())
#Answer: [1] [1, 1] 
7. 
for i in range(5): 
if i == 3: 
break 
print(i) 
#Answer: 0 1 2
8. 
try: 
print(10/0) 
except: 
print("Error") 
finally: 
print("Done")
#Answer: Error Done
'''SECTION C: Coding Questions
9. Write a program to:
- Take input string
- Count vowels and consonants'''
# Take input from user
text = input("Enter a string: ")

vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for ch in text:
    if ch.isalpha():  # check only alphabets
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)
'''Enter a string: Kalyani
Vowels: 3
Consonants: 4'''

'''10. Write a program to:
- Read a file
- Count number of lines, words and characters'''

with open("sample.txt", "r") as file:
    content = file.read()
lines = content.split('\n')
line_count = len(lines)
words = content.split()
word_count = len(words)
char_count = len(content)

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)
'''Lines: 2
Words: 5
Characters: 25'''

'''11. Write a program:
- Create a class BankAccount
- Methods: deposit, withdraw, check balance'''
class BankAccount:
    def _init_(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current Balance:", self.balance)
acc = BankAccount()

acc.deposit(1000)
acc.withdraw(300)
acc.check_balance()
'''Deposited: 1000
Withdrawn: 300
Current Balance: 700'''

'''12. Write a program:
- Accept list of numbers
- Remove duplicates
- Sort it without using sort()'''
nums = list(map(int, input("Enter numbers separated by space: ").split()))
unique_nums = []
for n in nums:
    if n not in unique_nums:
        unique_nums.append(n)
for i in range(len(unique_nums)):
    for j in range(0, len(unique_nums) - i - 1):
        if unique_nums[j] > unique_nums[j + 1]:
            unique_nums[j], unique_nums[j + 1] = unique_nums[j + 1], unique_nums[j]

print("Result:", unique_nums)
'''Enter numbers separated by space: 2 16 18 75
Result: [2, 16, 18, 75]'''

'''13. Write a program using lambda + map + filter:
- Square only even numbers from list'''
nums = list(map(int, input("Enter numbers: ").split()))
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))

print("Result:", result)
'''Enter numbers separated by space: 1 2 3
Result: [1, 2, 3]
Enter numbers: 1265
Result: []'''

'''SECTION D: Advanced / Thinking
16. Write a program:
- Simulate login system
- Use file to store username/password'''
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")

    print("Registration successful!")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "r") as file:
        users = file.readlines()

    for user in users:
        u, p = user.strip().split(",")
        if u == username and p == password:
            print("Login successful!")
            return

    print("Invalid username or password")
while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
'''1. Register
2. Login
3. Exit
Enter choice: 1
Enter username: Tulika
Enter password: 1234
Registration successful!'''

'''17. Exception Handling:
- Create custom exception "InvalidAgeError"
- Raise error if age < 18'''
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    print("Age is valid")
except InvalidAgeError as e:
    print("Error:", e)
    '''Enter age: 16
Error: Age must be 18 or above'''

'''SECTION E: GUI + Database Based
18. Create a Tkinter form:
- Name input
- Submit button
- Show entered name'''
from tkinter import *

def show_name():
    name = entry.get()
    result_label.config(text="Entered Name: " + name)

# Create window
root = Tk()
root.title("Name Form")
root.geometry("300x200")

# Label
label = Label(root, text="Enter your name:")
label.pack(pady=10)

# Entry box
entry = Entry(root)
entry.pack(pady=5)

# Submit button
btn = Button(root, text="Submit", command=show_name)
btn.pack(pady=10)

# Result label
result_label = Label(root, text="")
result_label.pack(pady=10)

# Run app
root.mainloop()
'''Entered Name:Tulika'''

'''19. Python + SQL:
- Connect database
- Create table Student
- Insert 3 records
- Fetch and display all'''
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="testdb"
)

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
""")

# Insert records
cursor.execute("INSERT INTO Student VALUES (1, 'Tulika', 21)")
cursor.execute("INSERT INTO Student VALUES (2, 'Priti', 21)")
cursor.execute("INSERT INTO Student VALUES (3, 'Aditi', 19)")

conn.commit()

# Fetch records
cursor.execute("SELECT * FROM Student")
rows = cursor.fetchall()

# Display
for row in rows:
    print(row)

# Close connection
conn.close()
'''(1, 'Tulika', 21)
(2, 'Priti', 21)
(3, 'Aditi', 19)'''

'''20. Build mini project:
STUDENT MANAGEMENT SYSTEM
Features:
- Add student
- View student
- Delete student
- Store data in file or database'''

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    with open("students.txt", "a") as f:
        f.write(name + "," + age + "\n")
    print("Student added successfully!")

def view_students():
    try:
        with open("students.txt", "r") as f:
            students = f.readlines()
            if not students:
                print("No records found.")
                return
            print("\nStudent List:")
            for s in students:
                name, age = s.strip().split(",")
                print("Name:", name, "| Age:", age)
    except FileNotFoundError:
        print("No records found.")

def delete_student():
    name_to_delete = input("Enter name to delete: ")
    try:
        with open("students.txt", "r") as f:
            students = f.readlines()

        with open("students.txt", "w") as f:
            found = False
            for s in students:
                name, age = s.strip().split(",")
                if name != name_to_delete:
                    f.write(s)
                else:
                    found = True

        if found:
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No records found.")

# Main menu
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
        '''1. Add Student
2. View Students
3. Delete Student
4. Exit
Enter choice: 1
Enter name: Tulika
Enter age: 21
Student added successfully!'''