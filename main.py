import json
import os


DB_FILE = "library.json"

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
    return []


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

