'''Freelancer Marketplace'''
class Freelancer:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill


class Client:
    def __init__(self, name):
        self.name = name


class Project:
    def __init__(self, title, budget):
        self.title = title
        self.budget = budget
        self.freelancer = None


freelancers = []
clients = []
projects = []

while True:
    print("\n1.Register Freelancer")
    print("2.Register Client")
    print("3.Create Project")
    print("4.Assign Freelancer")
    print("5.Process Payment")
    print("6.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Freelancer name: ")
        skill = input("Skill: ")
        freelancers.append(Freelancer(name, skill))
        print("Freelancer registered.")

    elif choice == "2":
        name = input("Client name: ")
        clients.append(Client(name))
        print("Client registered.")

    elif choice == "3":
        title = input("Project title: ")
        budget = float(input("Budget: "))
        projects.append(Project(title, budget))
        print("Project created.")

    elif choice == "4":
        pname = input("Enter project title: ")
        fname = input("Enter freelancer name: ")
        for p in projects:
            if p.title == pname:
                for f in freelancers:
                    if f.name == fname:
                        p.freelancer = f
                        print("Freelancer assigned.")
                        break

    elif choice == "5":
        pname = input("Enter project title: ")
        for p in projects:
            if p.title == pname and p.freelancer:
                print("Payment of", p.budget, "paid to", p.freelancer.name)

    elif choice == "6":
        break