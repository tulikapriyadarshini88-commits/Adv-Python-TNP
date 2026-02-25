#library management system
def add_book(book_list):
    book_name = input("Enter the name of the book to add: ")
    if book_name in book_list:
        print("Book already exists in the library.")
    else:
        book_list.append(book_name)
        print("Book added successfully.", book_name)
        
def remove_book(book_list):
    book_name = input("Enter the name of the book to remove: ")
    if book_name in book_list:
        book_list.remove(book_name)
        print("Book removed successfully.", book_name)
    else:
        print("Book not found in the library.")      
        
def display_books(book_list):
    if book_list:
        print("Books in the library:")
        for book in book_list:
            print(book)
    else:
        print("No books in the library.")
        
        
def borrow_book(book_list, borrowed_books):
    book_name = input("Enter the name of the book to borrow: ")
    if book_name in book_list:
        book_list.remove(book_name)
        borrowed_books.append(book_name)
        print("Book borrowed successfully.", book_name)
    else:
        print("Book not found in the library.")
        
def return_book(book_list, book_borrowed):
    book_name = input("enter the book name to return")
    if book_name in book_borrowed:
        book_borrowed.remove(book_name)
        book_list.append(book_name)
        print("Book returned successfully.", book_name)
    else:
        print("Book not found in the borrowed list.")
        
def main():
    book_list = []
    borrowed_books = []
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book(book_list)
        elif choice == '2':
            remove_book(book_list)
        elif choice == '3':
            display_books(book_list)
        elif choice == '4':
            borrow_book(book_list, borrowed_books)
        elif choice == '5':
            return_book(book_list, borrowed_books)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            
main()