import time

class Bank:
    def __init__(self):
        self.accounts = {"1001": 5000, "1002": 3000, "1003": 4000, "1004": 7000}

    def transfer(self):
        try:
            from_acc = input("From Account: ")
            to_acc = input("To Account: ")
            amount = float(input("Enter amount: "))

            if from_acc not in self.accounts or to_acc not in self.accounts:
                raise KeyError("Incorrect account number")

            if self.accounts[from_acc] < amount:
                raise ValueError("Overdraft not allowed")

            print("Processing transaction...")
            time.sleep(2)

            if amount > 10000:
                raise TimeoutError("Transaction timeout")

            self.accounts[from_acc] -= amount
            self.accounts[to_acc] += amount

            print("Transaction successful")

        except ValueError as e:
            print("Error:", e)
        except KeyError as e:
            print("Error:", e)
        except TimeoutError as e:
            print("Error:", e)

    def show_accounts(self):
        for acc, bal in self.accounts.items():
            print(acc, ":", bal)


bank = Bank()

while True:
    print("\n1.Transfer 2.Show Accounts 3.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        bank.transfer()
    elif choice == "2":
        bank.show_accounts()
    elif choice == "3":
        break
    else:
        print("Invalid choice")