import json
import os

BOOKS_FILE = "library.json"

def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    try:
        with open(BOOKS_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Error: Could not load books from file.")
        return []

def save_books(books):
    try:
        with open(BOOKS_FILE, 'w') as file:
            json.dump(books, file, indent=4)
    except IOError:
        print("Error: Could not save books to file.")

def view_all_books():
    books = load_books()
    if not books:
        print("No books available.")
        return

    print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'Status':<10}")
    print("-" * 70)
    for book in books:
        print(f"{book['id']:<5} {book['title']:<30} {book['author']:<20} {book['status']:<10}")

def list_borrowed_books():
    books = load_books()
    borrowed_books = [book for book in books if book['status'].lower() == 'borrowed']
    if not borrowed_books:
        print("No books are currently borrowed.")
        return

    print(f"{'ID':<5} {'Title':<30} {'Author':<20}")
    print("-" * 60)
    for book in borrowed_books:
        print(f"{book['id']:<5} {book['title']:<30} {book['author']:<20}")

def lend_book():
    books = load_books()
    title = input("Enter the title of the book to lend: ").strip()
    for book in books:
        if book['title'].lower() == title.lower():
            if book['status'].lower() == 'available':
                book['status'] = 'Borrowed'
                save_books(books)
                print(f"✅ '{book['title']}' has been successfully lent.")
                return
            else:
                print(f"⚠️ The book '{book['title']}' is already borrowed.")
                return
    print("❌ Book not found.")

def return_book():
    books = load_books()
    try:
        book_id = int(input("Enter the ID of the book to return: "))
    except ValueError:
        print("❌ Invalid input. Please enter a numeric ID.")
        return

    for book in books:
        if book["id"] == book_id:
            if book["status"].lower() == "borrowed":
                book["status"] = "Available"
                save_books(books)
                print(f"✅ Book '{book['title']}' has been returned.")
                return
            else:
                print(f"⚠️ Book '{book['title']}' is not currently borrowed.")
                return
    print("❌ Book ID not found.")

def add_book():
    books = load_books()
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    book_id = max((book["id"] for book in books), default=0) + 1
    new_book = {"id": book_id, "title": title, "author": author, "status": "Available"}
    books.append(new_book)
    save_books(books)
    print(f"✅ Book '{title}' by {author} added with ID {book_id}.")

def remove_book():
    books = load_books()
    try:
        book_id = int(input("Enter the ID of the book to remove: "))
    except ValueError:
        print("Invalid input. Please enter a valid book ID.")
        return

    updated_books = [book for book in books if book["id"] != book_id]
    if len(updated_books) == len(books):
        print("Book not found.")
    else:
        save_books(updated_books)
        print("Book removed successfully.")

def search_book():
    books = load_books()
    keyword = input("Enter title or author to search: ").lower()
    found = False
    for book in books:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Status: {book['status']}")
            found = True
    if not found:
        print("No matching books found.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print("=" * 50)
        print("📚 Welcome to the Library Management System 📚".center(50))
        print("=" * 50)
        print("1. View All Books")
        print("2. List Borrowed Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Add New Book")
        print("6. Remove Book")
        print("7. Search Book")
        print("8. Exit")
        print("-" * 50)
        choice = input("Enter your choice (1-8): ")

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
            search_book()
        elif choice == '8':
            print("Thank you for using the Library System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 8.")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
