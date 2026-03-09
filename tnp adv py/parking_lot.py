import time

class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.available_spots = total_spots
        self.vehicles = {}

    def entry(self, vehicle_no):
        if self.available_spots > 0:
            self.vehicles[vehicle_no] = time.time()
            self.available_spots -= 1
            print("Vehicle entered.")
        else:
            print("Parking Full")

    def exit(self, vehicle_no):
        if vehicle_no in self.vehicles:
            entry_time = self.vehicles.pop(vehicle_no)
            exit_time = time.time()
            hours = (exit_time - entry_time) / 3600
            fee = round(hours * 10, 2)
            self.available_spots += 1
            print("Vehicle exited.")
            print("Parking Fee:", fee)
        else:
            print("Vehicle not found")

    def show_spots(self):
        print("Available spots:", self.available_spots)


p = ParkingLot(3)

while True:
    print("\n1.Entry")
    print("2.Exit")
    print("3.Available Spots")
    print("4.Exit Program")

    choice = input("Enter choice: ")

    if choice == "1":
        v = input("Vehicle number: ")
        p.entry(v)

    elif choice == "2":
        v = input("Vehicle number: ")
        p.exit(v)

    elif choice == "3":
        p.show_spots()

    elif choice == "4":
        break

    else:
        print("Invalid choice")