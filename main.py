import json
import os

BOOKS_FILE = 'library.json'

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