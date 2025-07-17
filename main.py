import json
import os


BOOKS_FILE = "library.json"

def list_available_books(books):
    """Displays all books that are currently available."""
    available_books = [book for book in books if book['status'] == 'available']

    if not available_books:
        print("📚 No available books at the moment.")
        return

    print("\n📘 Available Books:")
    print("-" * 50)
    for idx, book in enumerate(available_books, 1):
        print(f"{idx}. Title : {book['title']}")
        print(f"   Author: {book['author']}")
        print("-" * 50)



def return_book():
    books = load_books()

    try:
        book_id = int(input("Enter the ID of the book to return: "))
    except ValueError:
        print("❌ Invalid input. Please enter a numeric ID.\n")
        return

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Borrowed":
                book["status"] = "Available"
                save_books(books)
                print(f"\n✅ Book '{book['title']}' has been returned.\n")
                return
            else:
                print(f"⚠️ Book '{book['title']}' is not currently borrowed.\n")
                return

    print("❌ Book ID not found.\n")


def load_books():
    """Loads books from a JSON file. Returns a list of books."""
    if not os.path.exists(BOOKS_FILE):
        return []

    try:
        with open(BOOKS_FILE, 'r') as file:
            books = json.load(file)
            return books
    except (json.JSONDecodeError, IOError):
        print("Error: Could not load books from file.")
        return []

def save_books(books):
    """Saves the list of books to a JSON file."""
    try:
        with open(BOOKS_FILE, 'w') as file:
            json.dump(books, file, indent=4)
    except IOError:
        print("Error: Could not save books to file.")


def add_book():
    #hi ana noha
    books = load_books()

    # Get book details from user
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()

    # Generate a unique ID
    book_id = max((book["id"] for book in books), default=0) + 1

    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available"
    }

    books.append(new_book)
    # save_books(books)

    print(f"\n✅ Book '{title}' by {author} added with ID {book_id}.\n")

def lend_book(books):
    """Marks a book as borrowed if it is available."""
    title = input("Enter the title of the book to lend: ").strip()

    for book in books:
        if book['title'].lower() == title.lower():
            if book['status'] == 'available':
                book['status'] = 'borrowed'
                print(f"✅ '{book['title']}' has been successfully lent.")
                return
            else:
                print(f"⚠️ The book '{book['title']}' is already borrowed.")
                return

    print("❌ Book not found.")



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("=" * 50)
        print("📚 Welcome to the Library Management System 📚".center(50))
        print("=" * 50)
        print("Please choose an option:")
        print()
        print("1. View All Books")
        print("2. List Borrowed Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Add New Book")
        print("6. Remove Book")
        print("7. Exit")
        print("-" * 50)

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            view_all_books()
        elif choice == '2':
            list_borrowed_books()
        elif choice == '3':
            lend_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            add_book()
        elif choice == '6':
            remove_book()
        elif choice == '7':
            print("\nThank you for using the Library System. Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number from 1 to 7.")
            input("Press Enter to continue...")

def list_borrowed_books(books):
    borrowed_books = [book for book in books if book.get('borrowed', False)]

    if not borrowed_books:
        print("No books are currently borrowed.")
        return

    print(f"{'ID':<5} {'Title':<30} {'Borrower':<20}")
    print("-" * 60)
    for book in borrowed_books:
        print(f"{book['id']:<5} {book['title']:<30} {book.get('borrower', 'Unknown'):<20}")

def view_all_books(books):
    if not books:
        print("No books available.")
        return

    print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'Year':<6}")
    print("-" * 65)
    for book in books:
        print(f"{book['id']:<5} {book['title']:<30} {book['author']:<20} {book['year']:<6}")



def remove_book():
    with open(DB_FILE, "r") as file:
        books = json.load(file)

    try:
        book_id = int(input("Enter the ID of the book to remove: "))
    except ValueError:
        print("Invalid input. Please enter a valid book ID.")
        return

    updated_books = [book for book in books if book["id"] != book_id]

    if len(updated_books) == len(books):
        print("Book not found.")
    else:
        with open(DB_FILE, "w") as file:
            json.dump(updated_books, file, indent=4)
        print("Book removed successfully.")



DB_FILE = "library.json"

def search_book():
    with open(DB_FILE, "r") as file:
        books = json.load(file)

    keyword = input("Enter title or author to search: ").lower()
    found = False
    for book in books:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Status: {book['status']}")
            found = True

    if not found:
        print("No matching books found.")
