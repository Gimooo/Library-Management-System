import json
import os

DB_FILE = "library.json"

def load_books():
    return []


def add_book():
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
