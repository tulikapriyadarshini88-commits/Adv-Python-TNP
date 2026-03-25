class Book:
    def __init__(self, name):
        self.name = name
        print("Book added")

    def __del__(self):
        print("Book removed")