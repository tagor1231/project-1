import json
import os

def load_books():
    """Load books from a JSON file."""
    if os.path.exists("books.json"):
        with open("books.json", "r") as file:
            return json.load(file)
    return []

def save_books(books):
    """Save books to a JSON file."""
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)

def add_book(books):
    """Add a new book to the bookstore."""
    title = input("Enter book title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    genre = input("Enter genre: ")
    price = input("Enter price: ")
    quantity = input("Enter quantity: ")
    
    if any(book["ISBN"] == isbn for book in books):
        print("Book with this ISBN already exists!")
        return
    
    try:
        price = float(price)
        quantity = int(quantity)
        if price < 0 or quantity < 0:
            raise ValueError
    except ValueError:
        print("Invalid price or quantity. Please enter positive numbers.")
        return
    
    book = {"Title": title, "Author": author, "ISBN": isbn, "Genre": genre, "Price": price, "Quantity": quantity}
    books.append(book)
    save_books(books)
    print("Book added successfully!")

def view_books(books):
    """Display all books in the bookstore."""
    if not books:
        print("No books available.")
        return
    for book in books:
        print(f"Title: {book['Title']}, Author: {book['Author']}, ISBN: {book['ISBN']}, Genre: {book['Genre']}, Price: {book['Price']}, Quantity: {book['Quantity']}")

def search_book(books):
    """Search for a book by title or ISBN."""
    query = input("Enter book title or ISBN to search: ")
    found_books = [book for book in books if book["Title"].lower() == query.lower() or book["ISBN"] == query]
    if found_books:
        for book in found_books:
            print(f"Found: {book}")
    else:
        print("Book not found.")

def remove_book(books):
    """Remove a book by ISBN."""
    isbn = input("Enter ISBN of the book to remove: ")
    for book in books:
        if book["ISBN"] == isbn:
            books.remove(book)
            save_books(books)
            print("Book removed successfully!")
            return
    print("Book not found.")

def main():
    books = load_books()
    while True:
        print("\nBookstore Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            remove_book(books)
        elif choice == "5":
            save_books(books)
            print("Exiting program. Data saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()