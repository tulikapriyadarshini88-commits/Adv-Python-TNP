class Task:
    def __init__(self, title, category, deadline, priority, tag):
        self.title = title
        self.category = category
        self.deadline = deadline
        self.priority = priority
        self.tag = tag

    def show(self):
        print(self.title, "|", self.category, "|", self.deadline, "|", self.priority, "|", self.tag)


class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Enter task title: ")
        category = input("Enter category: ")
        deadline = input("Enter deadline: ")
        priority = input("Enter priority (High/Medium/Low): ")
        tag = input("Enter tag: ")
        task = Task(title, category, deadline, priority, tag)
        self.tasks.append(task)
        print("Task Added Successfully")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available")
        for task in self.tasks:
            task.show()

    def filter_by_category(self):
        category = input("Enter category to filter: ")
        for task in self.tasks:
            if task.category == category:
                task.show()

    def filter_by_tag(self):
        tag = input("Enter tag to filter: ")
        for task in self.tasks:
            if task.tag == tag:
                task.show()


todo = ToDo()

while True:
    print("\n1. Add Task")
    print("2. Show All Tasks")
    print("3. Filter by Category")
    print("4. Filter by Tag")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        todo.add_task()
    elif choice == "2":
        todo.show_tasks()
    elif choice == "3":
        todo.filter_by_category()
    elif choice == "4":
        todo.filter_by_tag()
    elif choice == "5":
        break
    else:
        print("Invalid Choice")