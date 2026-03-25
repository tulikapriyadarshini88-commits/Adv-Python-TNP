class Vehicle:
    count = 0

    def rent(self):
        pass

class Car(Vehicle):
    def rent(self):
        Vehicle.count += 1
        return 1000

class Bike(Vehicle):
    def rent(self):
        Vehicle.count += 1
        return 500