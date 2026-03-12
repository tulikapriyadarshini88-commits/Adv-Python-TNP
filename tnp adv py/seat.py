class SeatNotAvailableError(Exception):
    pass

class InvalidPassengerError(Exception):
    pass

class PaymentFailureError(Exception):
    pass

class FlightSystem:
    def __init__(self):
        self.seats = 5
        self.bookings = {}

    def search(self):
        print("Available seats:", self.seats)

    def book(self):
        try:
            name = input("Enter passenger name: ").strip()
            payment = input("Payment status (success/fail): ").lower()

            if name == "":
                raise InvalidPassengerError("Invalid passenger details")

            if self.seats <= 0:
                raise SeatNotAvailableError("Seat not available")

            if payment != "success":
                raise PaymentFailureError("Payment failed")

            booking_id = len(self.bookings) + 1
            self.bookings[booking_id] = name
            self.seats -= 1

            print("Booking successful. ID:", booking_id)

        except (SeatNotAvailableError, InvalidPassengerError, PaymentFailureError) as e:
            print("Error:", e)

    def cancel(self):
        try:
            bid = int(input("Enter booking ID: "))
            if bid not in self.bookings:
                raise ValueError("Invalid booking ID")

            del self.bookings[bid]
            self.seats += 1
            print("Booking cancelled")

        except ValueError as e:
            print("Error:", e)


flight = FlightSystem()

while True:
    print("\n1.Search Flights 2.Book Ticket 3.Cancel Ticket 4.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        flight.search()
    elif ch == "2":
        flight.book()
    elif ch == "3":
        flight.cancel()
    elif ch == "4":
        break
    else:
        print("Invalid choice")