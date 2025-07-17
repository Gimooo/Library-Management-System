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
