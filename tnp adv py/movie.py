class Movie:
    def __init__(self, name, showtimes):
        self.name = name
        self.showtimes = showtimes
        self.seats = {time: ["A1", "A2", "A3", "A4"] for time in showtimes}


class BookingSystem:
    def __init__(self):
        self.movies = {
            "1": Movie("Avengers", ["10AM", "2PM"]),
            "2": Movie("Inception", ["1PM", "6PM"]),
            "3": Movie("Pushpa", ["10PM", "12PM"]),
            "4": Movie("Bahubali", ["3PM", "7PM"]),
            "5": Movie("Hi Nanna", ["2PM", "7PM"])

        }

    def show_movies(self):
        print("\nAvailable Movies:")
        for code, movie in self.movies.items():
            print(code, "-", movie.name)

    def show_showtimes(self, movie_code):
        movie = self.movies[movie_code]
        print("Showtimes:", movie.showtimes)

    def book_ticket(self):
        self.show_movies()
        movie_code = input("Select movie code: ")

        if movie_code in self.movies:
            movie = self.movies[movie_code]
            self.show_showtimes(movie_code)

            time = input("Select showtime: ")

            if time in movie.showtimes:
                print("Available Seats:", movie.seats[time])
                seat = input("Select seat: ")

                if seat in movie.seats[time]:
                    movie.seats[time].remove(seat)
                    print("\n--- Booking Confirmed ---")
                    print("Movie:", movie.name)
                    print("Showtime:", time)
                    print("Seat:", seat)
                else:
                    print("Seat not available")
            else:
                print("Invalid showtime")
        else:
            print("Invalid movie code")


system = BookingSystem()

while True:
    print("\n1. Check Movies")
    print("2. Book Ticket")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.show_movies()
    elif choice == "2":
        system.book_ticket()
    elif choice == "3":
        break
    else:
        print("Invalid Choice")